import random
from board import *

class MinMaxAgent:

    def __init__(self, turn, opponent_turn):
        self.turn = turn
        self.opponent_turn = opponent_turn
        self.board = None
        self.num_visited_nodes = 0

    def set_board(self, board):
        self.board = Board()
        self.board.copy_board(board)

    def get_name(self):
        return "MinMax"

    def compute_action_score(self, input_r, input_c, turn, depth):
        self.num_visited_nodes += 1

        self.board.set(input_r, input_c, turn)

        ret_score = None
        if self.board.check_is_win(self.turn):
            ret_score = 100.
        elif self.board.check_is_win(self.opponent_turn):
            ret_score = -100.
        else:
            positions = self.board.get_empty_grids()
            if len(positions) == 0:
                ret_score = 0. # draw
            else:
                next_turn = self.opponent_turn if turn == self.turn else self.turn
                score_action_list = []
                for r, c in positions:
                    score = self.compute_action_score(r, c, next_turn, depth+1)
                    score_action_list.append((score, (r, c)))

                if next_turn == self.turn:
                    ret_score = max(score_action_list)
                    ret_score = ret_score[0]
                    ret_score -= 1.0 # penalty for using more steps
                else:
                    ret_score = min(score_action_list)
                    ret_score = ret_score[0]
                    ret_score += 1.0 # penalty for using more steps

        #ret_score += self.board.evaluation(turn)
        self.board.unset(input_r, input_c)
        return ret_score

    def next_move(self):
        self.num_visited_nodes = 0

        positions = self.board.get_empty_grids()

        score_action_list = []
        for r, c in positions:
            score = self.compute_action_score(r, c, self.turn, 1)
            score_action_list.append((score, (r,c)))

        max_score = max(score_action_list)
        max_score = max_score[0]
        print("best score: {}".format(max_score))

        actions = [a for s, a in score_action_list if s == max_score]
        print("num actions = {}".format(len(actions)))
        print("num visited nodes = {}".format(self.num_visited_nodes))
        random.shuffle(actions)
        return actions[0]


