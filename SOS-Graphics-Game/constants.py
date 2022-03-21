from asyncore import close_all
import pygame
import ctypes
pygame.init()


user32 = ctypes.windll.user32
WIDTH = user32.GetSystemMetrics(0) //1.5
SCALE = 448/ user32.GetSystemMetrics(0)
HEIGHT =(11/16) * WIDTH
HEIGHT = int(HEIGHT)
BOARD_WIDTH, BOARD_HEIGHT =  int(HEIGHT//1.3), int(HEIGHT//1.3)
#WIDTH, HEIGHT = 900, 600
ROWS, COLS = 4,4
ROWS_5, COLS_5 = 5,5
SQUARE_SIZE = BOARD_HEIGHT//COLS
SQUARE_SIZE_5 = BOARD_HEIGHT// COLS_5


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


#Colours
GREY = (70, 70, 70)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255,140,0)
GREEN = (50, 70, 50)
YELLOW = (255, 100, 0)
CYAN = (0,255,255)


FPS = 60

font = pygame.font.SysFont('comicsans', 30)
letter_font = pygame.font.SysFont('consolas', 70)
small_font = pygame.font.SysFont('comicsans', 10)