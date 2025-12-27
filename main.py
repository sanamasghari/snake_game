from handle import  draw_menu, draw_game_over, draw_board, draw_snake, draw_fruit, read_high_score, load_images, load_sounds
from snake import Snake, Food, Game
import pygame
import shelve

map_width = 17
map_height = 17
unit = 50
  
def main():
    # pygame setup
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((map_width*unit, (map_height+1)*unit))
    clock = pygame.time.Clock()

    board = [[0 for _ in range(map_width)] for _ in range(map_height)]
    
    images = load_images(map_width, map_height, unit)  
    
    #initial snake location:
    snake_body = [[7, 5], [7, 6], [7, 7]] 
    snake_direction = "left" 
    snake = Snake(snake_body, snake_direction)

    #initial fruit location:    
    fruit = Food()
    fruit.random_location(map_width, map_height)
    fruit.random_fruit(images[2])

    #initialize Game
    game = Game(board, snake, fruit, map_width, map_height, images[2])

    key_direction = {pygame.K_UP: "up", 
                    pygame.K_DOWN: "down",
                    pygame.K_RIGHT: "right",
                    pygame.K_LEFT: "left"
                    }

    move_timer = 0
    move_delay = 200

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
                    
                if event.key == pygame.K_RETURN and game.game_over:
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
            best_score = read_high_score()
            draw_menu(screen, best_score, images[0], map_width, map_height, unit)
            pygame.display.flip()

        else:
            current_time = pygame.time.get_ticks()
                        
            # automatic movement of snake when ther is no new direction and game not over yet.
            if current_time - move_timer > move_delay and not game.game_over:

                if game.control_eat() == "food-eaten":
                    game.tail_addition = True
                    load_sounds("eating_sound")

                snake.move(tail_addition=game.tail_addition)
                game.tail_addition = False  
                
                game.control_hit()
                move_timer = current_time
                
            if game.game_over:
                if not game_over_music_played:
                    load_sounds("game-over")
                    game_over_music_played = True
                    
                draw_game_over(screen, map_width, map_height, unit, game)
                pygame.display.flip()
                clock.tick(8)    

                continue

            draw_board(screen, map_width, map_height, unit, game)
            draw_snake(screen, snake, game, images[1], unit)
            draw_fruit(screen, fruit, unit)
            pygame.display.flip()
            clock.tick(8)

    pygame.quit()


def head_angle(direction):
    angles = {"down": 0, "right":90, "up":180, "left": 270}
    return angles[direction]

def vali_snake_direction(direction):
    if direction in ['up', 'down', 'right', 'down']:
        return True
    else:
        return False

def valid_fruit_location(food_row, food_col):    
    if food_row > map_height or food_col > map_width:
        return "out side of the map"
    
    elif food_row == map_height or food_col == map_width:
        return "food is on the margin"

    else:
        return "right place"


if __name__ == "__main__":
    main()