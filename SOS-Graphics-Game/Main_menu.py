import pygame, sys
from game_4x4 import *
from game_5x5 import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("SOS Game")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawWindow()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)


def fade_in(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    alpha = 300
    #for alpha in range(300, 0):
    while alpha > 0:
        fade.set_alpha(alpha)
        redrawWindow()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)
        alpha -= 1



def redrawWindow():
    screen.fill(GREY)
    pygame.draw.rect(buttons_rect, WHITE, button_1)
    pygame.draw.rect(buttons_rect, WHITE, button_2)




buttons_rect = pygame.Surface((300, 80))
#buttons_rect.set_alpha(10)
button_1 = pygame.Rect(0, 0, 100, 80)
button_2 = pygame.Rect(buttons_rect.get_width() - 100, 0, 100, 80)



def main_menu():
    buttons_rect.fill(GREY)
    

    while True:
        clock.tick(60)
        screen.fill(GREY)
    
        
        screen.blit(buttons_rect, (WIDTH//2 -150, HEIGHT//2))
        
        

        draw_text("SOS Game", font, ORANGE, screen, WIDTH//2 - 70 , HEIGHT//10)

        

        pygame.draw.rect(buttons_rect, WHITE, button_1)
        pygame.draw.rect(buttons_rect, WHITE, button_2)
        draw_text("4x4", font, BLACK, buttons_rect, button_1.x + 20, button_1.y + 20)
        draw_text("5x5", font, BLACK, buttons_rect, button_2.x + 20, button_2.y + 20)

        	
        mouse = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH//2 -150 <= mouse[0] <= WIDTH//2 -150 + 100 and HEIGHT//2 <= mouse[1] <= HEIGHT//2 +80:
                    #draw_text("It Works!", font, RED, screen, WIDTH//2 - 70, HEIGHT// 4)
                    fade(WIDTH,HEIGHT)
                    fade_in(WIDTH,HEIGHT)
                    game_4x4()
                if WIDTH//2 +50 <= mouse[0] <= WIDTH//2 +150 and HEIGHT//2 <= mouse[1] <= HEIGHT//2 +80:
                    fade(WIDTH,HEIGHT)
                    fade_in(WIDTH,HEIGHT)
                    game_5x5()
                    

        pygame.display.update()
        

if __name__ == "__main__":
    main_menu()


