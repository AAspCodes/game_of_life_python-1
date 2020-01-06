from cell import evaluate_cell


def update_neighbors(cell, index_width, index_height, world):
    neighbor_locations = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                          (1, -1), (1, 0), (1, 1)]
    alive_neighbors = 0
    found_food = False
    for coordinate in neighbor_locations:
        x = cell['x-value'] + coordinate[0]
        y = cell['y-value'] + coordinate[1]
        if index_width > x > -1 and index_height > y > -1:
            neighbor = world[y][x]
            alive_neighbors += neighbor['alive']
            if neighbor['has-food']:
                found_food = True
    cell['alive-neighbor-count'] = alive_neighbors
    cell['neighbor-has-food'] = found_food


def update_world(width, height, world):
    index_width = width - 1
    index_height = height - 1
    for row in world:
        for cell in row:
            update_neighbors(cell, index_width, index_height, world)
    for row in world:
        for cell in row:
            evaluate_cell(cell)
