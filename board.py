import copy

class Board(object):

    def __init__(self):
        self.nrows = 3
        self.ncols = 3
        self.grids = [[0 for _ in range(self.ncols)] for _ in range(self.nrows)]
        #print(self.grids)

    def copy_board(self, board):
        self.grids = board.grids.copy()

    def evaluate_helper(self, v):
        # check for number of repeated items
        v_id = self.symbol_to_id(v)

        vert_score = 0
        for r in range(self.nrows):
            cnt = 0
            for c in range(self.ncols):
                if self.grids[r][c] == v_id:
                    cnt += 1
            vert_score = max(vert_score, cnt)

        horz_score = 0
        for c in range(self.ncols):
            cnt = 0
            for r in range(self.nrows):
                if self.grids[r][c] == v_id:
                    cnt += 1
            horz_score = max(horz_score, cnt)

        return (vert_score + horz_score) / 1.

    def evaluation(self, turn):
        opp_turn = 'o' if turn == 'x' else 'x'
        my_score = self.evaluate_helper(turn)
        opp_score = self.evaluate_helper(opp_turn)
        return my_score - opp_score

    def get_board_str(self):
        boardstr = ""
        for r in range(self.nrows):
            rowstr = "|"
            for c in range(self.ncols):
                if self.grids[r][c] == 0:
                    rowstr += "-|"
                elif self.grids[r][c] == 1:
                    rowstr += "X|"
                elif self.grids[r][c] == 2:
                    rowstr += "O|"

            boardstr += rowstr
            boardstr += "\n"

        return boardstr

    def set(self, r, c, v):
        assert v in ['x', 'o', '-']
        self.grids[r][c] = self.symbol_to_id(v)

    def unset(self, r, c):
        self.grids[r][c] = 0

    def symbol_to_id(self, v):
        if v == 'x':
            return 1
        elif v == 'o':
            return 2
        elif v == '-':
            return 0
        else:
            return -1

    def check_is_win(self, v):
        assert v in ['x', 'o', '-']

        v_id = self.symbol_to_id(v)
        # check if v wins
        for r in range(self.nrows):
            cnt = 0
            for c in range(self.ncols):
                if self.grids[r][c] == v_id:
                    cnt += 1
            if cnt == 3:
                return True

        for c in range(self.ncols):
            cnt = 0
            for r in range(self.nrows):
                if self.grids[r][c] == v_id:
                    cnt += 1
            if cnt == 3:
                return True

        if self.grids[0][0] == self.grids[1][1] == self.grids[2][2] == v_id:
            return True

        if self.grids[0][2] == self.grids[1][1] == self.grids[2][0] == v_id:
            return True
        return False

    def has_empty(self):
        for r in range(self.nrows):
            if 0 in self.grids[r]:
                return True
        return False

    def is_in_progress(self):
        return self.get_status() == "in progress"

    def get_status(self):
        for v in ['x', 'o']:
            if self.check_is_win(v):
                return f"{v} wins"
        if self.has_empty():
            return "in progress"
        return "draw"

    def is_grid_empty(self, r, c):
        return self.grids[r][c] == 0

    def get_empty_grids(self):
        pos_list = []
        for r in range(self.nrows):
            for c in range(self.ncols):
                if self.grids[r][c] == 0:
                    pos_list.append((r,c))
        return pos_list

    def print(self):
        print(self.get_board_str())