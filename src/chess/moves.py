class Move:
    def __init__(self, start_position : tuple, end_position : tuple):
        self.start = start_position
        self.end = end_position

class Direction:
    UP = -1
    DOWN = 1