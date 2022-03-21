import pygame
from constants import *
pygame.init()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    


class Button():
    def __init__(self, x, y, image, hover_image):
        width = image.get_width()
        height = image.get_height()
        self.image = image
        self.hover_image = hover_image
        #self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.normal_image = image
        

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        mouse_pos = pygame.mouse.get_pos()
        pressed = False
        if self.rect.collidepoint(mouse_pos):
            self.image = self.hover_image
            if pygame.mouse.get_pressed()[0] == 1:
                if self.clicked == False:
                    self.clicked = True
                    pressed = True
        else:
            self.image = self.normal_image
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return pressed



class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None





    def draw_cubes(self, screen, grid, rows, cols):
        screen.fill(GREY)      
        
        for row in range(rows):
            for col in range(cols):
                SQUARE_SIZE = BOARD_HEIGHT//cols
                inside_box_text = font.render("S | O", 1, (0, 0, 0))
                text_width, text_height = inside_box_text.get_width(), inside_box_text.get_height()

                green_square = pygame.Rect((row * SQUARE_SIZE, col* SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                green_square_pos = green_square.topleft
                grid[row][col] = green_square_pos
                text_pos_x = green_square.centerx
                text_pos_y = green_square.centery
                text_pos = (text_pos_x, text_pos_y)
                
                pygame.draw.rect(screen, WHITE,green_square)
                pygame.draw.rect(screen, GREEN, (row * SQUARE_SIZE+2, col* SQUARE_SIZE+2, SQUARE_SIZE-5, SQUARE_SIZE-5))
                
                screen.blit(inside_box_text, (text_pos_x - text_width//2, text_pos_y - text_height//2))


             

