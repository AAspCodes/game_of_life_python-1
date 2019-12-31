from time import sleep
import random
import subprocess as sp


class Game:

    def __init__(self):
        self.main()

    @staticmethod
    def newCell(x_val, y_val):
        return {
            'alive': False,
            'x-value': x_val,
            'y-value': y_val,
            'alive-neighbor-count': 0
        }

    @staticmethod
    def kill(cell):
        cell['alive'] = False

    @staticmethod
    def birth(cell):
        # print(cell)
        cell['alive'] = True

    @staticmethod
    def update_x(cell, value):
        cell['x-value'] = value

    @staticmethod
    def update_y(cell, value):
        cell['y-value'] = value

    @staticmethod
    def update_neighbors(cell, world):
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
            x = cell['x-value'] + coordinate[0]
            y = cell['y-value'] + coordinate[1]
            if len(world[0]) > x > -1 and len(world) > y > -1:
                if world[y][x]['alive']:
                    alive_neighbors += 1
        cell['alive-neighbor-count'] = alive_neighbors

    def updateWorld(self, world):
        for row in world:
            for cell in row:
                self.update_neighbors(cell, world)
        for row in world:
            for cell in row:
                self.evaluateCell(cell)

    def evaluateCell(self, cell):
        neighbors = cell['alive-neighbor-count']
        if cell['alive']:
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
    def displayWorld(world_array):
        display = [["*" if cell['alive'] else " " for cell in row]
                   for row in world_array]

        [print(" ".join(row)) for row in display]

    @staticmethod
    def loadTextFile(file):
        load_worldfile = open(file).read()
        return load_worldfile.split('\n')

    def genRandomWorld(width, height):
        world = []
        for i in range(0, height):
            row_array = []
            for j in range(0, width):
                isAlive = random.randint(0, 1)
                row_array.append(isAlive)
            world.append(row_array)
        return world

    @staticmethod
    def ask_user_to_continue():
        while True:
            answer = input("would you like to continue? y/n: ")
            if answer == "y":
                while True:
                    answer = input("how may more cycles would you like?: ")
                    try:
                        answer = int(answer)
                    except:
                        print("Try a whole number.")
                    else:
                        return answer
            elif answer == "n":
                print("goodbye")
                exit()
            else:
                print("'y' or 'n'")

    def main(self):
        # loaded_world_array = loadTextFile('world.txt')
        loaded_world_array = Game.genRandomWorld(100, 100)
        world = self.init_world(loaded_world_array)
        life_cycles = 0
        life_cycle_limit = 100
        while True:
            self.displayWorld(world)
            self.updateWorld(world)
            sleep(.01)
            sp.call('clear', shell=True)
            life_cycles += 1
            if life_cycles > life_cycle_limit:
                life_cycle_limit = self.ask_user_to_continue()
                life_cycles = 0


if __name__ == "__main__":
    game = Game()
