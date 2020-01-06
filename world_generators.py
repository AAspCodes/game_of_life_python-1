from random import randint
from cell import new_cell


def init_world(fresh=False, dead=False, loaded_world=None, height=100, width=100):
    """master world init function"""

    cell_action = cell_decider(fresh, dead, loaded_world)

    world_cells = []
    for col_pos in range(0, height - 1):
        world_row = []
        for row_pos in range(0, width - 1):
            cell = cell_action(row_pos=row_pos,
                               col_pos=col_pos,
                               loaded_world=loaded_world)
            world_row.append(cell)
        world_cells.append(world_row)
    return world_cells


def cell_decider(fresh, dead, loaded_world):
    if fresh:
        return fresh_init
    elif dead:
        return dead_init
    elif loaded_world:
        return load_init
    else:
        raise Exception('this should not have happened')


def fresh_init(**kwargs):
    return new_cell(kwargs['row_pos'],
                    kwargs['col_pos'],
                    alive=bool(randint(0, 1)))


def dead_init(**kwargs):
    return new_cell(kwargs['row_pos'], kwargs['col_pos'])


def load_init(**kwargs):
    row_pos = kwargs['row_pos']
    col_pos = kwargs['col_pos']
    return new_cell(row_pos,
                    col_pos,
                    alive=kwargs['loaded_world'][row_pos][col_pos])
