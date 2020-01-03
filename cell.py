class Cell:

    def __init__(self, x_val, y_val):
        self.x_val = x_val
        self.y_val = y_val
        self.is_alive = False
        self.alive_neighbors = 0
