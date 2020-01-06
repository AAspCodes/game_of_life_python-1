
def new_cell(x_value, y_value, alive=False):
    return {
        'alive': alive,
        'x-value': x_value,
        'y-value': y_value,
        'alive-neighbor-count': 0,
        'has-food': False,
        'neighbor-has-food': False
    }


def kill(cell):
    cell['alive'] = False


def birth(cell):
    cell['alive'] = True


def evaluate_cell(cell):
    neighbors = cell['alive-neighbor-count']
    neighbors_have_food = cell['neighbor-has-food']
    if cell['alive']:
        if neighbors not in [2, 3]:
            kill(cell)
    else:
        if neighbors == 3 or neighbors_have_food:
            birth(cell)
    cell['has-food'] = False
