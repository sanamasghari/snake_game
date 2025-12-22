from snake import Snake, Food, Game
import pygame
import shelve
import random


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
      
        
def main():
    # pygame setup
    pygame.init()
    pygame.mixer.init()

    map_width = 17
    map_height = 17
    unit = 50

    board = [[0 for _ in range(map_width)] for _ in range(map_height)]
        
    #initial snake location:
    snake_body = [[7, 5], [7, 6], [7, 7]] 
    snake_direction = "left" 
    snake = Snake(snake_body, snake_direction)

    #initial apple location:    
    apple = Food()
    apple.random_location(map_width, map_height)
    while apple.food_location in snake_body:
        apple.random_location(map_width, map_height)

    #initialize Game
    game = Game(board, snake, apple, map_width, map_height)

    key_direction = {pygame.K_UP: "up", 
                    pygame.K_DOWN: "down",
                    pygame.K_RIGHT: "right",
                    pygame.K_LEFT: "left"
                    }

    screen = pygame.display.set_mode((map_width*unit, (map_height+1)*unit))
    clock = pygame.time.Clock()

    move_timer = 0
    move_delay = 200

    welcome_page = pygame.image.load('welcome.jpg')
    welcome_page = pygame.transform.scale(welcome_page, (map_width*unit, (map_height+1)*unit))

    head_img = pygame.image.load('head.png').convert()
    head_img = pygame.transform.scale(head_img, (50, 50))

    apple_img = pygame.image.load('fruits/apple.jpg').convert_alpha()
    apple_img = pygame.transform.scale(apple_img, (50, 50))
    
    eating_sound = pygame.mixer.Sound('apple_crunch.wav')
    pygame.mixer.music.load('Game-Over.mp3')

    running = True
    game_start = False
    game_over_music_played = False
            
    while running:
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:   
                      
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
                if event.key == pygame.K_r and game.game_over:
                    game_start = True
                    game.game_over = False
                    game_over_music_played = False
                    game.initial_setting()
                # game does not started
                elif not game_start and event.key == pygame.K_RETURN:
                    game_start = True
                    
                elif event.key in key_direction:
                        snake.update_direction(key_direction[event.key])

        # Menu page: consist backgrand, High score, Enter key
        if not game_start:
            # Backgrand
            screen.blit(welcome_page,(1,1))
            
            # Welcome Text
            add_text(screen, ' Welcome to Snake Game', "freesansbold.ttf", 55, (250,250,250), 400, 50, center=True)
            add_text(screen, 'Press Enter to Start', "freesansbold.ttf", 30, (150,150,50), map_height*unit/20, 11.5*map_width*unit/20)

            # Read High score From file
            d = shelve.open('best_score.txt')  
            best_score = d['best_score']            
            d.close()
            
            add_text(screen, f'High Score:{best_score} ', "freesansbold.ttf", 30, (150,150,50), 14 * map_height*unit/20, 11.5*map_width*unit/20)

            pygame.display.flip()

        else:
            current_time = pygame.time.get_ticks()
                        
            # automatic movement of snake when ther is no new direction and game not over yet.
            if current_time - move_timer > move_delay and not game.game_over:

                if game.control_eat() == "food-eaten":
                    game.tail_addition = True
                    eating_sound.play()
                
                snake.move(tail_addition=game.tail_addition)
                game.tail_addition = False  
                
                game.control_hit()
                move_timer = current_time
                
            if game.game_over:
                if not game_over_music_played:
                    pygame.mixer.music.play(0)
                    game_over_music_played = True
                    
                # Background
                screen.fill((170,170,170))
                grid(screen,  map_width+1, map_height+1, unit, 200, 200, 200)

                add_text(screen, 'GAME OVER!', "freesansbold.ttf", 64, (255,0,0), 400, 300, center=True)
                add_text(screen, 'Press R to Retry or Press ESC to Quit', "freesansbold.ttf", 25, (255,255,255), 400, 550, center=True)
                add_text(screen, f'Final Score:{game.score} ', "freesansbold.ttf", 40, (250,250,250), 400, 400, center=True)
                
                # Read High score From file
                d = shelve.open('best_score.txt')  
                best_score = d['best_score']            
                d.close()
                
                if game.score > best_score: 
                    # Update Best Score in File
                    d = shelve.open('best_score.txt')  
                    d['best_score'] = game.score
                    d.close()
                    
                    add_text(screen, f'Best Score:{game.score} ', "freesansbold.ttf", 40, (250,250,250), 400, 460, center=True)

                else:        
                    add_text(screen, f'Best Score:{best_score} ', "freesansbold.ttf", 40, (250,250,250), 400, 460, center=True)

                pygame.display.flip()
                clock.tick(8)    

                continue
  
            screen.fill((245,245,245))
            grid(screen, map_width, map_height+1, unit, 255, 255, 255)


            pygame.draw.rect(screen, (200, 210, 200), (0, map_width*unit, map_width*unit, map_height*unit))

            add_text(screen, f'Score:{game.score}', "freesansbold.ttf", 32, (80,80,80), 10, map_height*unit + 10)

            for i, (r,c) in enumerate(snake.body):
                if i == 0 :
                    if game.snake.direction == "down":
                        copy_head = head_img 
                        screen.blit(copy_head,(c*unit, r*unit))
                        
                    elif game.snake.direction == "up":
                        copy_head = pygame.transform.rotate(head_img, 180)
                        screen.blit(copy_head,(c*unit, r*unit))
                                    
                    elif game.snake.direction == "left":
                        copy_head = pygame.transform.rotate(head_img, 270)
                        screen.blit(copy_head,(c*unit, r*unit))
                        
                    elif game.snake.direction == "right":
                        copy_head = pygame.transform.rotate(head_img, 90)
                        screen.blit(copy_head,(c*unit, r*unit))   
                else:
                    pygame.draw.circle(screen, (0,190,120), (c*unit + unit/2, r*unit + unit/2),  unit/2)
                
            apple_row, apple_col = apple.food_location

            screen.blit(apple_img,(apple_col*unit ,apple_row*unit))

            pygame.display.flip()
            clock.tick(8)

    pygame.quit()
            
if __name__ == "__main__":
    main()