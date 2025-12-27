""" 
This file consists features and rendering of pygame and graphic design.

"""

import pygame
import shelve

 

def read_high_score():
    # Read High score From file
    d = shelve.open('best_score.txt')  
    best_score = d['best_score']            
    d.close()    
    
    return best_score


def grid(screen, map_width, map_height, unit, R, G, B):
    #grid:
    for i in range(0, map_width*unit, unit):
        for j in range(0, map_height*unit, unit):
            pygame.draw.line(screen, (R,G,B), (i, 0), (i, map_width*unit), 1)
            pygame.draw.line(screen, (R,G,B), (0, j), (map_height*unit, j), 1)



def add_text(screen, text, font, size, color, x, y, center=False):
    edited_font = pygame.font.Font(font, size)            
    edited_text = edited_font.render(text, True, color)
    
    if center:
        textRect = edited_text.get_rect()
        textRect.center = (x, y)
        screen.blit(edited_text, textRect)
    else:
        screen.blit(edited_text, (x,y))
      

def draw_menu(screen, best_score, background, map_width, map_height, unit):
    # Backgrand
    screen.blit(background,(1,1))
    
    # Welcome Text
    add_text(screen, ' Welcome to Snake Game', "freesansbold.ttf", 55, (250,250,250), 400, 50, center=True)
    add_text(screen, 'Press Enter to Start', "freesansbold.ttf", 30, (150,150,50), map_height*unit/20, 11.5*map_width*unit/20)
    add_text(screen, f'High Score:{best_score} ', "freesansbold.ttf", 30, (150,150,50), 14 * map_height*unit/20, 11.5*map_width*unit/20)
    
    
def draw_game_over(screen, map_width, map_height, unit, game):
    # Background
    screen.fill((170,170,170))
    grid(screen,  map_width+1, map_height+1, unit, 200, 200, 200)

    add_text(screen, 'GAME OVER!', "freesansbold.ttf", 64, (255,0,0), 400, 300, center=True)
    add_text(screen, 'Press Enter to Retry or Press ESC to Quit', "freesansbold.ttf", 25, (255,255,255), 400, 550, center=True)
    add_text(screen, f'Final Score:{game.score} ', "freesansbold.ttf", 40, (250,250,250), 400, 400, center=True)

    # Read High score From file
    best_score = read_high_score()
    
    if game.score > best_score: 
        # Update Best Score in File
        d = shelve.open('best_score.txt')  
        d['best_score'] = game.score
        d.close()
        
        add_text(screen, f'Best Score:{game.score} ', "freesansbold.ttf", 40, (250,250,250), 400, 460, center=True)
    else:        
        add_text(screen, f'Best Score:{best_score} ', "freesansbold.ttf", 40, (250,250,250), 400, 460, center=True)

      
def draw_board(screen, map_width, map_height, unit, game):    
    screen.fill((255,255,255))
    grid(screen, map_width, map_height+1, unit, 230, 230, 230)
    pygame.draw.rect(screen, (200, 210, 200), (0, map_width*unit, map_width*unit, map_height*unit))
    add_text(screen, f'Score:{game.score}', "freesansbold.ttf", 32, (80,80,80), 10, map_height*unit + 10)


       
def draw_snake(screen, snake,game, head_img, unit):
    head_angle = {"down": 0, "right":90, "up":180, "left": 270}
    snake_direction = game.snake.direction
    
    for i, (r,c) in enumerate(snake.body):
        if i == 0 and snake_direction in head_angle:
            copy_head = pygame.transform.rotate(head_img, head_angle[snake_direction])

            screen.blit(copy_head,(c*unit, r*unit))   
        else:
            pygame.draw.circle(screen, (128,198,88), (c*unit + unit/2, r*unit + unit/2),  unit/2)
        
    
def draw_fruit(screen, fruit, unit):
    fruit_row, fruit_col = fruit.food_location
    screen.blit(fruit.selected_fruit, (fruit_col*unit + 1 ,fruit_row*unit+1))
 
 
 
def load_images(map_width, map_height, unit):
    
    welcome_page = pygame.image.load('images/welcome.jpg')
    welcome_page = pygame.transform.scale(welcome_page, (map_width*unit, (map_height+1)*unit))

    head_img = pygame.image.load('images/head.jpg').convert()
    head_img = pygame.transform.scale(head_img, (49, 49))

    apple_img = pygame.image.load('images/fruits/apple.jpg').convert_alpha()
    apple_img = pygame.transform.scale(apple_img, (49, 49))
    
    banana_img = pygame.image.load('images/fruits/banana.jpg').convert_alpha()
    banana_img = pygame.transform.scale(banana_img, (49, 49))
    
    blueberry_img = pygame.image.load('images/fruits/blueberry.jpg').convert_alpha()
    blueberry_img = pygame.transform.scale(blueberry_img, (49, 49))
    
    carrot_img = pygame.image.load('images/fruits/carrot.jpg').convert_alpha()
    carrot_img = pygame.transform.scale(carrot_img, (49, 49))
    
    grapes_img = pygame.image.load('images/fruits/grapes.jpg').convert_alpha()
    grapes_img = pygame.transform.scale(grapes_img, (49, 49))
    
    orange_img = pygame.image.load('images/fruits/orange.jpg').convert_alpha()
    orange_img = pygame.transform.scale(orange_img, (49, 49))
    
    avacado_img = pygame.image.load('images/fruits/avacado.jpg').convert_alpha()
    avacado_img = pygame.transform.scale(avacado_img, (49, 49))
    
    pineapple_img = pygame.image.load('images/fruits/pineapple.jpg').convert_alpha()
    pineapple_img = pygame.transform.scale(pineapple_img, (49, 49))
    
    rasberry_img = pygame.image.load('images/fruits/rasberry.jpg').convert_alpha()
    rasberry_img = pygame.transform.scale(rasberry_img, (49, 49))

    strawberry_img = pygame.image.load('images/fruits/strawberry.jpg').convert_alpha()
    strawberry_img = pygame.transform.scale(strawberry_img, (49, 49))

    tomato_img = pygame.image.load('images/fruits/tomato.jpg').convert_alpha()
    tomato_img = pygame.transform.scale(tomato_img, (49, 49))
    
    coconut_img = pygame.image.load('images/fruits/coconut.jpg').convert_alpha()
    coconut_img = pygame.transform.scale(coconut_img, (49, 49))
    
    fruits = [apple_img, banana_img, blueberry_img, carrot_img, grapes_img, orange_img, avacado_img, pineapple_img, rasberry_img, strawberry_img, tomato_img, coconut_img]

    return [welcome_page, head_img, fruits]

 
def load_sounds(sound):
    if sound == "eating_sound":
        eating_sound = pygame.mixer.Sound('sounds/apple_crunch.wav')
        eating_sound.play()
    elif sound == "game-over":
        pygame.mixer.music.load('sounds/Game-Over.mp3')
        pygame.mixer.music.play()
     
 