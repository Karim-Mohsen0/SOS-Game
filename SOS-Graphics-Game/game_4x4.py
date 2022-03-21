import sys
import pygame
from board import *
from subprocess import call
pygame.init()

ROWS, COLS = 4, 4
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("SOS 4x4")

rounds = 0
def change_square_color(i, j):
    global rounds
    if rounds % 2 == 0:
        square.fill(RED)
        board_surface.blit(square, (grid[i][j][0]+2, grid[i][j][1] +2))
        rounds += 1 
    else:
        square.fill(BLUE)
        board_surface.blit(square, (grid[i][j][0]+2, grid[i][j][1] +2))
        rounds += 1


def choose_letter(i, j):
    mouse = pygame.mouse.get_pos()
    if mouse[0] < grid[i][j][0] + SQUARE_SIZE//2 + (WIDTH - BOARD_WIDTH)//2:
        draw_text("S", letter_font, BLACK, board_surface, grid[i][j][0] + SQUARE_SIZE//2 - 20, grid[i][j][1] + SQUARE_SIZE//2 - 20)
        return "S"
    else:
        draw_text("O", letter_font, BLACK, board_surface, grid[i][j][0] + SQUARE_SIZE//2 - 20, grid[i][j][1] + SQUARE_SIZE//2 - 20)
        return "O"
    
    


def check_square(i, j):
    if grid[i][j] == "S" or grid[i][j] == "O":
        return False
    else:
        return True


blue_score, red_score =0, 0


def check_o_points(col, row):
    play_again = False
    global blue_score, red_score
    if ROWS -1> row > 0 and 0 <= col < COLS:
        if grid[col][row] == "O" and grid[col][row-1] == "S" and grid[col][row+1] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if COLS-1> col > 0 and 0 <= row < ROWS:     
        if grid[col][row] == "O" and grid[col-1][row] == "S" and grid[col+1][row] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if 0 < row <ROWS-1 and 0< col < COLS-1:
        if grid[col][row] == "O" and grid[col +1][row-1] == "S" and grid[col-1][row+1] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
        if grid[col][row] == "O" and grid[col -1][row-1] == "S" and grid[col+1][row+1] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    return play_again
            
            
                
                



def check_s_points(col, row):
    play_again = False
    global blue_score, red_score
    if 0<= col <COLS-2:
        if grid[col + 1][row] == "O" and grid[col+2][row] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if 1< col <COLS:
        if grid[col - 1][row] == "O" and grid[col-2][row] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if 0<= row <ROWS-2:
        if grid[col][row+1] == "O" and grid[col][row+2] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if 1< row <ROWS:
        if grid[col][row - 1] == "O" and grid[col][row - 2] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if ROWS>row >1 and 0 <= col <ROWS-2:
        if grid[col+1][row - 1] == "O" and grid[col+2][row - 2] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if ROWS -2>row >=0 and 0 <= col <ROWS-2:
        if grid[col+1][row+1] == "O" and grid[col+2][row+2] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if ROWS -2>row >=0 and 1 < col <ROWS:
        if grid[col-1][row+1] == "O" and grid[col-2][row+2] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    if ROWS>row >1 and 1 < col <ROWS:
        if grid[col-1][row-1] == "O" and grid[col-2][row-2] == "S":
            if rounds %2 == 0:
                blue_score += 1
            else:
                red_score += 1
            play_again = True
    return play_again




def build_matrix(rows, cols):
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])

    return matrix

grid = build_matrix(4,4)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)






def game_over():
    game_over = 0
    for idx, i in enumerate(grid):
        for idx2, j in enumerate(i):
            if grid[idx][idx2] == "S" or grid[idx][idx2] == "O":
                game_over +=1
    return game_over


board_surface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
square = pygame.Surface((SQUARE_SIZE-5, SQUARE_SIZE-5))
end_surface = pygame.Surface((WIDTH, HEIGHT))

play_img = pygame.image.load('Pictures/PlayButton.png')
play_hover_img = pygame.image.load('Pictures/PlayButtonHighlight.png')
quit_img = pygame.image.load('Pictures/QuitButton.png')
quit_hover_img = pygame.image.load('Pictures/QuitButtonHighlight.png')
play_img = pygame.transform.scale(play_img, (int(play_img.get_width()*SCALE), int(play_img.get_height() * SCALE)))
quit_img = pygame.transform.scale(quit_img, (int(quit_img.get_width()*SCALE), int(quit_img.get_height() * SCALE)))
quit_hover_img = pygame.transform.scale(quit_hover_img, (int(quit_hover_img.get_width()*SCALE), int(quit_hover_img.get_height() * SCALE)))
play_hover_img = pygame.transform.scale(play_hover_img, (int(play_hover_img.get_width()*SCALE), int(play_hover_img.get_height() * SCALE)))

play_button = Button(WIDTH //4 - play_img.get_width()//2, HEIGHT//2 , play_img, play_hover_img)
quit_button = Button(WIDTH //1.25 - quit_img.get_width()//2, HEIGHT//2 , quit_img, quit_hover_img)



def game_4x4():
    global rounds
    board_surface.fill(RED)
    board = Board()
    end_surface.fill(BLACK)

    test = False
    play = True

    delay_time = 400

    board.draw_cubes(board_surface, grid, ROWS, COLS)
    while play:
        current_time = pygame.time.get_ticks()
        global blue_score, red_score
        screen.fill(GREY)
        

        screen.blit(board_surface, ((int(WIDTH - BOARD_WIDTH)// 2), int((HEIGHT- BOARD_HEIGHT)//2) + 50))

        letter_s = font.render("S", 1, (0, 0, 0))

        mouse = pygame.mouse.get_pos() 
        
        draw_text(str(blue_score), font, BLUE,screen, WIDTH//2 + 50, HEIGHT//10)
        draw_text(str(red_score), font, RED,screen, WIDTH//2 - 50, HEIGHT//10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    i = (mouse[0] - int((WIDTH - BOARD_WIDTH)// 2))//SQUARE_SIZE
                    j = (mouse[1]- int((HEIGHT- BOARD_HEIGHT)//2) -50)//SQUARE_SIZE
                    if 0 <= i < 4 and 0 <= j < 4 and check_square(i, j):
                        change_square_color(i, j)
                        
                        grid[i][j] = choose_letter(i, j)
                        if grid[i][j] == "S":
                            if check_s_points(i, j):
                                rounds -= 1
                                
                        elif grid[i][j] == "O":
                            if check_o_points(i, j):
                                rounds -= 1
                        if game_over() == 16:
                            start_time = current_time + delay_time
                            test = True
                            

        if test:
            if current_time >= start_time:
                end_surface.set_alpha(200)
                screen.blit(end_surface, (0, 0))
                player = "Blue Won!" if blue_score > red_score else "Red Won!"
                text_color = BLUE if blue_score > red_score else RED
                if blue_score == red_score:
                    text_color = YELLOW
                    draw_text("It's A Draw!", letter_font, text_color,screen, WIDTH //2 - 220, HEIGHT//5 - 25)
                else:
                    draw_text(player, letter_font, text_color,screen, WIDTH //2 - 150, HEIGHT//5 - 25)


                if play_button.draw():
                    blue_score, red_score = 0,0
                    play = False
                if quit_button.draw():
                    pygame.quit()
                    sys.exit()
            
                    

        
        pygame.display.update()
 
        clock.tick(60)


if __name__ == "__main__":
    game_4x4()