import numpy as np
import utils
import pygame
import sys

def create_board():
    board = np.zeros((utils.ROW_COUNT, utils.COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[utils.ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(utils.ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(utils.COLUMN_COUNT-3):
        for r in range(utils.ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(utils.COLUMN_COUNT):
        for r in range(utils.ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(utils.COLUMN_COUNT-3):
        for r in range(utils.ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(utils.COLUMN_COUNT-3):
        for r in range(3, utils.ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(utils.COLUMN_COUNT):
        for r in range(utils.ROW_COUNT):
            pygame.draw.rect(screen, utils.BLUE, (c*utils.SQUARESIZE, r*utils.SQUARESIZE+utils.SQUARESIZE, utils.SQUARESIZE, utils.SQUARESIZE))
            pygame.draw.circle(screen, utils.BLACK, (int(c*utils.SQUARESIZE+utils.SQUARESIZE/2), int(r*utils.SQUARESIZE+utils.SQUARESIZE/2)), utils.RADIUS)

board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()
width = utils.COLUMN_COUNT * utils.SQUARESIZE
height = (utils.ROW_COUNT +1) * utils.SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            continue

            # # Ask for Player 1 input
            # if turn == 0:
            #     col = int(input("Player 1 - make your selection (0-6):"))
            #
            #     if is_valid_location(board, col):
            #         row = get_next_open_row(board, col)
            #         drop_piece(board, row, col, 1)
            #
            #         if winning_move(board, 1):
            #             print("PLAYER 1 WINS!")
            #             game_over = True
            #
            # # Ask for Player 2 input
            # else:
            #     col = int(input("Player 2 - make your selection (0-6):"))
            #
            #     if is_valid_location(board, col):
            #         row = get_next_open_row(board, col)
            #         drop_piece(board, row, col, 2)
            #
            #         if winning_move(board, 2):
            #             print("PLAYER 2 WINS!")
            #             game_over = True
            #             break
            #
            # print_board(board)
            #
            # turn += 1
            # turn = turn % 2
