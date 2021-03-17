# import statement
import pygame, sys
import numpy as np

# initializing pygame
pygame.init()

# constnt
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE =  WIDTH//BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLES_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4

# color
BG_COLOR = (28, 170, 156)
BLACK = (0, 0, 0)
RED = (255,0,0)
LINE_COLOR = (23, 145 ,135)
CIRCLE_COLOR = (200, 194, 187)
CROSS_COLOR = (66 ,34, 21)

# setting screen caption and color
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Tic-Tac-Toe' )
screen.fill(BG_COLOR)

# board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
# print(board)

# pygame.draw.line( screen , BLACK, (10,10), (300,250), 10)

# defining functions
def draw_lines():
    # 1 horizontal
    pygame.draw.line( screen, LINE_COLOR, (0,SQUARE_SIZE), (WIDTH ,SQUARE_SIZE), LINE_WIDTH )
    # 2 horizotal
    pygame.draw.line( screen, LINE_COLOR, (0,2*SQUARE_SIZE), (WIDTH ,2*SQUARE_SIZE), LINE_WIDTH )

    # 1 vertical
    pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE,0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
    # 2 vertical
    pygame.draw.line( screen, LINE_COLOR, (2*SQUARE_SIZE,0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH )

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2) ) , CIRCLE_RADIUS, CIRCLES_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), ( col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), ( col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
    if board[row][col]==0:
        return True
    else:
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True            

def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_line(col, player)
            return True

    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_line(row, player)
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_line(player)
        return True

    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_line(player)
        return True

    return False

def draw_vertical_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def draw_horizontal_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color , (15, posY), ( WIDTH - 15, posY), 15)


def draw_asc_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color , (15, HEIGHT - 15), ( WIDTH - 15, 15), 15)

def draw_desc_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color , (15, 15), ( WIDTH - 15, HEIGHT - 15), 15)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()

player = 1 
game_over = False

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square( clicked_row,clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over = True
                    player = 1   

                draw_figures()    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart()
                game_over = False

# setting update function
        pygame.display.update()
