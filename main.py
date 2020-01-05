import random
import subprocess as sp
from time import sleep

from file_handle import save_text_file, load_text_file
from user_input import get_int_input
from better_output import newlined_print


# TODO: add food function
# TODO: change_environment_variables function
# TODO: replace some for loops with .map and list constructors
# TODO: display world should output a 2d grid or 3 values. alive, dead, food.


class Game:

    def __init__(self):
        self.world_width = 100
        self.world_height = 100
        self.life_cycles = 0
        self.life_cycle_limit = 10
        self.world = self.make_new_world()
        self.save_file_name = "saved_world.txt"
        self.cycle_time = .01
        self.main()

    def main(self):
        while True:
            self.cycle()

    def make_new_world(self):
        return self.init_fresh_world()

    def cycle(self):
        Game.display_world(self.world)
        self.display_lifecycles()
        self.update_world()
        sleep(self.cycle_time)
        sp.call('clear', shell=True)
        self.life_cycles += 1
        if self.life_cycles >= self.life_cycle_limit:
            self.do_what_next()

    def display_lifecycles(self):
        print(f'Life Cycles: {self.life_cycles}')

    def do_what_next(self):
        options = [self.go_on_living, self.stop_living, self.add_food,
                   self.save_life, self.load_life, self.restart_life,
                   self.change_environment_variables]
        prompt = """What would you like to do next?
[1] go on living
[2] stop living
[3] add food
[4] save this life
[5] load a saved life
[6] restart life 
[7] change environmental variables

enter the number of your choice: """

        choice = options[get_int_input(1, len(options), prompt) - 1]
        choice()

    def go_on_living(self):
        # ask user how many more life cycles they want
        answer = get_int_input(1, 1_000_000,
                               "\nHow many more life cycles would you like?\
                               \nEnter a number between 1 and 1 million: ")
        self.life_cycle_limit += answer

    def stop_living(self):
        newlined_print("goodbye")
        exit()

    def add_food(self):
        """this function is soooo ugly"""

        # temporary
        max_food = 1000
        prompt = """How much food do you want to add?
Enter a number between 0 and {0}: """.format(max_food)
        # ask user how much food they want to add.
        amount_of_food = get_int_input(0, max_food, prompt)
        intended_food = amount_of_food
        # add food in random places if the cell there is dead.
        attempts_to_add_food = 0
        while True:
            if amount_of_food <= 0:
                print(f'{intended_food} was added.')
                break

            random_x = random.randint(0, self.world_width - 2)
            random_y = random.randint(0, self.world_height - 2)
            cell = self.world[random_y][random_x]
            if (not cell['alive']) and (not cell['has-food']):
                cell['has-food'] = True
                amount_of_food -= 1

            # if more food is trying to be added than there is space availble for,
            # prevent that
            attempts_to_add_food += 1
            if attempts_to_add_food > intended_food * 5:
                message = """ after {0} attempts to add food
and {1} food added
the world gave up looking for places to add food.""".format(
                    attempts_to_add_food, intended_food - amount_of_food)

                break

        self.do_what_next()

    def save_life(self):
        boolean_world = Game.world_to_booleans(self.world)
        save_text_file(self.save_file_name, boolean_world, self.life_cycles)
        newlined_print("This World has been saved.")
        self.do_what_next()

    def load_life(self):
        self.life_cycles, world_from_memory = load_text_file(
            self.save_file_name)
        self.world_width = len(world_from_memory[0])
        self.world_height = len(world_from_memory)
        self.world = self.init_loaded_world(world_from_memory)
        self.life_cycle_limit = self.life_cycles
        newlined_print("The World has been loaded.")
        self.do_what_next()

    def restart_life(self):
        self.life_cycles = 0
        self.life_cycle_limit = self.life_cycles
        self.world = self.init_fresh_world()
        newlined_print("The World has restarted.")
        self.do_what_next()

    def change_environment_variables(self):
        pass

    @staticmethod
    def new_cell(x_value, y_value):
        return {
            'alive': False,
            'x-value': x_value,
            'y-value': y_value,
            'alive-neighbor-count': 0,
            'has-food': False,
            'neighbor-has-food': False
        }

    @staticmethod
    def kill(cell):
        cell['alive'] = False

    @staticmethod
    def birth(cell):
        cell['alive'] = True

    def update_neighbors(self, cell):
        neighbor_locations = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]
        alive_neighbors = 0
        found_food = False
        for coordinate in neighbor_locations:
            x = cell['x-value'] + coordinate[0]
            y = cell['y-value'] + coordinate[1]
            if len(self.world[0]) > x > -1 and len(self.world) > y > -1:
                neighbor = self.world[y][x]
                if neighbor['alive']:
                    alive_neighbors += 1
                if neighbor['has-food']:
                    found_food = True
        cell['alive-neighbor-count'] = alive_neighbors
        cell['neighbor-has-food'] = found_food

    def update_world(self):
        for row in self.world:
            for cell in row:
                self.update_neighbors(cell)
        for row in self.world:
            for cell in row:
                self.evaluate_cell(cell)

    def evaluate_cell(self, cell):
        neighbors = cell['alive-neighbor-count']
        neighbors_have_food = cell['neighbor-has-food']
        if cell['alive']:
            if neighbors not in [2, 3]:
                self.kill(cell)
        else:
            if neighbors == 3 or neighbors_have_food:
                self.birth(cell)
        cell['has-food'] = False

    @staticmethod
    def world_to_booleans(world_array):
        return [[cell["alive"] for cell in row]
                for row in world_array]

    @staticmethod
    def display_world(world_array):
        display = [["*" if cell['alive'] else " " for cell in row]
                   for row in world_array]
        joined_rows = [(" ".join(row)) for row in display]
        output = "\n".join(joined_rows)
        print(output)

    # I know the following two functions are WET, but I'm not sure
    # how to put them into one function with out being much less efficient.
    def init_loaded_world(self, init_world_array):
        world_cells = []
        for col_pos in range(0, self.world_height - 1):
            world_row = []
            for row_pos in range(0, self.world_width - 1):
                cell = self.new_cell(row_pos, col_pos)
                loadup_value = init_world_array[col_pos][row_pos]
                if loadup_value:
                    self.birth(cell)
                world_row.append(cell)
            world_cells.append(world_row)
        return world_cells

    def init_fresh_world(self):
        world_cells = []
        for col_pos in range(0, self.world_height - 1):
            world_row = []
            for row_pos in range(0, self.world_width - 1):
                cell = self.new_cell(row_pos, col_pos)
                if bool(random.randint(0, 1)):
                    self.birth(cell)
                world_row.append(cell)
            world_cells.append(world_row)
        return world_cells


if __name__ == "__main__":
    game = Game()
