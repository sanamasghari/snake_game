from snake import Snake, Food, Game
import pygame
import shelve


def grid(screen, map_width, map_height, unit, R, G, B):
    #grid:
    for i in range(0, map_width*unit, unit):
        for j in range(0, map_height*unit, unit):
            pygame.draw.line(screen, (R,G,B), (i, 0), (i, map_width*unit), 1)
            pygame.draw.line(screen, (R,G,B), (0, j), (map_height*unit, j), 1)
            
def main():
    # pygame setup
    pygame.init()

    map_width = 17
    map_height = 17
    unit = 50

    board = [[0 for _ in range(map_width)] for _ in range(map_height)]
        
    #initial snake location:
    snake_body = [[7, 5], [7, 6], [7, 7]] 
    snake_direction = "left" 
    snake = Snake(snake_body, snake_direction)
    # game.initial_setting()

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

    screen = pygame.display.set_mode((map_width*unit, map_height*unit))
    clock = pygame.time.Clock()
    running = True

    # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    move_timer = 0
    move_delay = 125
    # img = pygame.image.load('_.jpg')
    # img = pygame.transform.scale(img, (850, 850))

    welcome_page = pygame.image.load('welcome.jpg')
    welcome_page = pygame.transform.scale(welcome_page, (map_width*unit, map_height*unit))

    head_img = pygame.image.load('head.png').convert()
    head_img = pygame.transform.scale(head_img, (50, 50))
    # head_img.set_colorkey((255, 255, 255))

    apple_img = pygame.image.load('apple.jpg').convert_alpha()
    apple_img = pygame.transform.scale(apple_img, (50, 50))

    game_start = False

    # best_score = 0
    # d = shelve.open('best_score.txt')  
    # d['best_score'] = best_score           
    # d.close()
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
            font = pygame.font.Font('freesansbold.ttf', 55)            
            text = font.render(' Welcome to Snake Game', True, (250,250,250))
            textRect = text.get_rect()
            textRect.center = (400, 50)
            screen.blit(text, textRect)
            
            # Enter Key Guide
            font = pygame.font.Font('freesansbold.ttf', 30)            
            text = font.render('Press Enter to Start', True, (150,150,150))
            screen.blit(text, (map_height*unit/20, 11.5*map_width*unit/20))
            
            # Read High score From file
            d = shelve.open('best_score.txt')  
            best_score = d['best_score']            
            d.close()
            
            text = font.render(f'High Score:{best_score} ', True, (150,150,150))
            screen.blit(text, (14 * map_height*unit/20, 11.5 * map_width*unit/20))
            
            pygame.display.flip()


        else:
            current_time = pygame.time.get_ticks()
            
            food_eaten = game.control_eat()
            
            # automatic movement of snake when ther is no new direction and game not over yet.
            if current_time - move_timer > move_delay and not game.game_over:

                if game.control_eat() == "food-eaten":
                    game.tail_addition = True
                
                snake.move(tail_addition=game.tail_addition)
                game.tail_addition = False  
                
                game.control_hit()
                move_timer = current_time
                
            if game.game_over:
                # Background
                screen.fill((170,170,170))
                grid(screen,  map_width, map_height, unit, 200, 200, 200)
                
                # Game Over Display
                font = pygame.font.Font('freesansbold.ttf', 64)
                text = font.render('GAME OVER!', True, (255,0,0))
                textRect = text.get_rect()
                textRect.center = (400, 300)
                screen.blit(text, textRect)
                
                # Retry Key Guide Display
                font = pygame.font.Font('freesansbold.ttf', 25)
                text = font.render('Press R to Retry or Press ESC to Quit', True, (255,255,255))
                textRect = text.get_rect()
                textRect.center = (400, 550)
                screen.blit(text, textRect)
                
                # Final Score Display
                font = pygame.font.Font('freesansbold.ttf', 40)            
                text = font.render(f'Final Score:{game.score} ', True, (250,250,250))
                textRect = text.get_rect()
                textRect.center = (400, 400)
                screen.blit(text, textRect)
                
                # Read High score From file
                d = shelve.open('best_score.txt')  
                best_score = d['best_score']            
                d.close()
                
                if game.score > best_score: 
                    # Update Best Score in File
                    d = shelve.open('best_score.txt')  
                    d['best_score'] = game.score
                    d.close()
                    
                    font = pygame.font.Font('freesansbold.ttf', 40)            
                    text = font.render(f'Best Score:{game.score} ', True, (250,250,250))
                    textRect = text.get_rect()
                    textRect.center = (400, 460)
                    screen.blit(text, textRect)

                else:        
                    font = pygame.font.Font('freesansbold.ttf', 40)            
                    text = font.render(f'Best Score:{best_score} ', True, (250,250,250))
                    textRect = text.get_rect()
                    textRect.center = (400, 460)
                    screen.blit(text, textRect)
                    
                
                pygame.display.flip()
                clock.tick(8)    

                continue
            
  
            screen.fill((245,245,245))
            grid(screen, map_width, map_height, unit, 255, 255, 255)
            
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(f'Score:{game.score} ', True, (30,30,30))
            # textRect = text.get_rect()
            screen.blit(text, (10,10))

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
    
    