from time import sleep
import random
import subprocess as sp
from user_input import get_int_input
from cell import Cell
from file_handle import save_text_file

# TODO: stop annoying code completions
# TODO: load world function
# TODO: restart life function
# TODO: add food function
# TODO: change_enviroment_variables function
# TODO: replace some for loops with .map and list constructors
# TODO: displayWorld should be made more flexable
# TODO: display world should output a 2d grid or 3 values. alive, dead, food.


class Game:

    def __init__(self):
        self.world_width = 100
        self.world_height = 100
        self.life_cycles = 0
        self.life_cycle_limit = 10
        self.world = self.make_new_world()
        self.save_file_name = "saved_world.txt"
        self.main()

    def main(self):
        while True:
            self.cycle()

    def make_new_world(self):
        return self.init_world(
            Game.genRandomWorld(self.world_width, self.world_height))

    def cycle(self):
        Game.displayWorld(self.world)
        self.display_lifecycles()
        self.updateWorld()
        sleep(.01)
        sp.call('clear', shell=True)
        self.life_cycles += 1
        if self.life_cycles > self.life_cycle_limit:
            self.do_what_next()

    def display_lifecycles(self):
        print(f'Life Cycles: {self.life_cycles}')

    def do_what_next(self):
        options = [self.go_on_living, self.stop_living, self.add_food,
                   self.save_life, self.load_life, self.restart_life,
                   self.change_enviroment_variables]
        prompt = """
        What would you like to do next?
        [1] go on living
        [2] stop living
        [3] add food
        [4] save this life
        [5] load a saved life
        [6] restart life 
        [7] change enviromental variables

        enter the number of your choice.
        """
        while True:
            try:
                choice = options[get_int_input(1, len(options), prompt) - 1]
            except IndexError:
                # probably won't ever be used.. but feels like good practice...
                print("That's not in the availble options.")
            except Exception:
                print("Try a Whole number.")
            else:
                break

        choice()

    def go_on_living(self):
        # ask user how many more life cycles they want
        answer = get_int_input(1, 1_000_000,
                               "How many more life cycles would you like?\
                               \nEnter a number between 1 and 1 million: ")
        self.life_cycle_limit += answer

    def stop_living(self):
        print("goodbye")
        exit()

    def add_food(self):
        pass

    def save_life(self):
        boolean_world = Game.world_to_booleans(self.world)
        save_text_file(self.save_file_name, boolean_world)
        print("This world has been saved")
        self.do_what_next()

    def load_life(self):
        pass

    def restart_life(self):
        pass

    def change_enviroment_variables(self):
        pass

    @staticmethod
    def newCell(x_val, y_val):
        return Cell(x_val, y_val, is_alive=False, alive_neighbors=0)

    @staticmethod
    def kill(cell):
        cell.is_alive = False

    @staticmethod
    def birth(cell):
        cell.is_alive = True

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
        for coordinate in neighbor_locations:
            x = cell.x_val + coordinate[0]
            y = cell.y_val + coordinate[1]
            if len(self.world[0]) > x > -1 and len(self.world) > y > -1:
                if self.world[y][x].is_alive:
                    alive_neighbors += 1
        cell.alive_neighbors = alive_neighbors

    def updateWorld(self):
        for row in self.world:
            for cell in row:
                self.update_neighbors(cell)
        for row in self.world:
            for cell in row:
                self.evaluateCell(cell)

    def evaluateCell(self, cell):
        neighbors = cell.alive_neighbors
        if cell.is_alive:
            if neighbors not in [2, 3]:
                self.kill(cell)
        else:
            if neighbors == 3:
                self.birth(cell)

    def init_world(self, init_world_array):
        world_height = len(init_world_array)
        world_width = len(init_world_array[0])
        world_cells = []
        for col_pos in range(0, world_height - 1):
            world_row = []
            for row_pos in range(0, world_width - 1):
                cell = self.newCell(row_pos, col_pos)
                loadup_value = init_world_array[col_pos][row_pos]
                if int(loadup_value) == 1:
                    self.birth(cell)
                world_row.append(cell)
            world_cells.append(world_row)
        return world_cells

    @staticmethod
    def world_to_booleans(world_array):
        return [[True if cell.is_alive else False for cell in row]
                for row in world_array]

    @staticmethod
    def displayWorld(world_array):
        display = [["*" if cell.is_alive else " " for cell in row]
                   for row in world_array]
        joined_rows = [(" ".join(row)) for row in display]
        output = "\n".join(joined_rows)
        print(output)

    def genRandomWorld(width, height):
        world = []
        for i in range(0, height):
            row_array = []
            for j in range(0, width):
                isAlive = random.randint(0, 1)
                row_array.append(isAlive)
            world.append(row_array)
        return world


if __name__ == "__main__":
    game = Game()
