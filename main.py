import time, pygame

def get_neighbors(row_index, col_index, grid, grid_len):
    neighbor_count = 0
    for i in range(row_index-1, row_index+2):
        for j in range(col_index-1, col_index+2):
            if i == row_index and j == col_index:
                    continue
            if 0 <= i < grid_len and 0 <= j < grid_len:
                neighbor_count += grid[i][j]

    return neighbor_count


def update(board):
    to_remove = []
    to_add = []
    grid_len = len(board)
    for i, row in enumerate(board):
        for j, col in enumerate(board[i]):
            neighbors = get_neighbors(i, j, board, grid_len)

            if board[i][j] and not 1 < neighbors < 4:
                 to_remove.append((i, j))

            elif not board[i][j] and neighbors >= 3:
                 to_add.append((i, j))

    for spot in to_remove:
         board[spot[0]][spot[1]] = 0

    for spot in to_add:
         board[spot[0]][spot[1]] = 1

    return board
        
def display(board):
     """made for displaying a board"""
     grid_len = len(board)

     window.fill('black')
     for i, row in enumerate(board):
        for j, col in enumerate(row):
             if col:
                  pygame.draw.rect(window, (255, 255, 255), pygame.Rect(j*pixel_width, i*pixel_height, pixel_width, pixel_height))

     for i in range(0, height):
          row = i*(height/grid_len)
          pygame.draw.line(window, (100, 100, 100), (0, row), (width, row), 1)
     for j in range(0, width):
          col = j*(width/grid_len)
          pygame.draw.line(window, (100, 100, 100), (col, 0), (col, height), 1)


     pygame.display.update()


def user_draw():
     if pygame.mouse.get_pressed():
          x, y = pygame.mouse.get_pos()
          print(f"{x, y = }")
          row, col = x//pixel_width, y//pixel_height
          print(f"{row, col = }")
          board[row][col] = 1

pygame.init()
clock = pygame.time.Clock()
width, height = 800, 800
window = pygame.display.set_mode((width, height))
board_size = 20
pixel_width = width//board_size
pixel_height = height//board_size

board = [[0 for _ in range(board_size)] for _ in range(board_size)]
board[board_size//2][board_size//2] = 1
board[board_size//2][board_size//2-1] = 1
board[board_size//2][board_size//2+1] = 1

while True:
     clock.tick(10)
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()

     user_draw()
     update(board)
     display(board)