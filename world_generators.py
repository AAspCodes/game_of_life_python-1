import random
from cell import new_cell, birth
def init_loaded_world(init_world_array, height=100, width=100):
    world_cells = []
    for col_pos in range(0, height - 1):
        world_row = []
        for row_pos in range(0, width - 1):
            cell = new_cell(row_pos, col_pos)
            loadup_value = init_world_array[col_pos][row_pos]
            if loadup_value:
                birth(cell)
            world_row.append(cell)
        world_cells.append(world_row)
    return world_cells


def init_fresh_world( height=100, width=100):
    world_cells = []
    for col_pos in range(0, height - 1):
        world_row = []
        for row_pos in range(0, width - 1):
            cell = new_cell(row_pos, col_pos)
            if bool(random.randint(0, 1)):
                birth(cell)
            world_row.append(cell)
        world_cells.append(world_row)
    return world_cells


def init_dead_world(height=100, width=100):
    dead_world = [[new_cell(row_pos, col_pos)
                   for row_pos in range(0, width - 1)]
                  for col_pos in range(0, height - 1)]
    return dead_world
