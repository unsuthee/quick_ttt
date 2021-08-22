import random

class RandomAgent:

    def __init__(self):
        pass

    def get_name(self):
        return "RND"

    def next_move(self, board):
        positions = board.get_empty_grids()
        random.shuffle(positions)
        return positions[0]
