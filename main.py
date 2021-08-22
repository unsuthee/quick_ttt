from board import *
from random_agent import *
from min_max_agent import *

turn = 'x'
cpu = 'x'
human = 'o'

board = Board()
board.print()

agent = MinMaxAgent(cpu, human)
agent.set_board(board)
agent_name = agent.get_name()

while board.is_in_progress():
    if turn == cpu:
        r, c = agent.next_move()
        print(f'Agent {agent_name} moves to pos: {r},{c}')
    else:
        input_str = input("enter position:")
        r, c = input_str.split(',')
        r = int(r)
        c = int(c)
        while not board.is_grid_empty(r, c):
            input_str = input("enter position:")
            r, c = input_str.split(',')
            r = int(r)
            c = int(c)

    board.set(r, c, turn)
    board.print()

    agent.set_board(board)

    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'

print(board.get_status())

