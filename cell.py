class Cell:

    def __init__(self, x_val, y_val, is_alive, alive_neighbors):
        self.x_val = x_val
        self.y_val = y_val
        self.is_alive = is_alive
        self.alive_neighbors = alive_neighbors
