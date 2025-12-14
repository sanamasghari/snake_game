from snake import Snake, Food, Game
import sys


def main():
    # Board-Map:
    map_width = 17
    map_height = 15
    
    # board = []
    # for _ in range(map_height):
    #     length = []
    #     for _ in range(map_width):
    #         length.append(0)
    #     board.append(length)
        
    board = [[0 for _ in range(map_height)] for _ in range(map_height)]
        
    #initial snake location:
    snake_body = [[6,0], [6,1], [6,2]]
    snake_direction = "right"
    snake = Snake(snake_body, snake_direction)
    
    #initial apple location:    
    apple = Food()
    apple.random_location(map_width, map_height)
    while apple.food_location in snake_body:
        apple.random_location(map_width, map_height)

    #initialize Game
    game = Game(board, snake, apple, map_width, map_height)

        
    while not game.game_over:
        
        board = [[0 for _ in range(map_height)] for _ in range(map_height)]

        apple_row, apple_col = apple.food_location
        board[apple_row][apple_col] = "🍎"

        for r,c in snake_body:
            board[r][c] = "🐍"
            
        #input
        user_direction = input()
        #check direction
        snake.check_direction(user_direction)
        # check eaten food 
        if game.control_eat() == "food-eaten":
            snake.move(tail_addition=True)
            game.tail_addition=False
            print("score:", game.score)
        else:
        # move (flag)
            snake.move(tail_addition=False)        
            
        # check collision
        game.control_hit()
        if game.game_over:
            break
        
        print(board)
            
        
    
if __name__ == "__main__":
    main()
    
    