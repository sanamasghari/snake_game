""" 
This file consists features and logic of the game using OOP (classes) 

"""

import random

class Snake:
    # body: The coordinates of snake body 
    # direction: The movment direction of snake Up, Down, Left, Right
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction


    def check_direction(self, new_direction):
        opposite_direction = {"up":"down", "down":"up", "right":"left", "left":"right"}
        
        if new_direction != opposite_direction[self.direction]:
            self.direction = new_direction
        
        
    def update_direction(self, key):
        opposite = {"up":"down", "down":"up", "left":"right", "right":"left"}
        if key not in ["up","down","left","right"]:
            return
        if key != opposite[self.direction]:
            self.direction = key
        
    # Move snake one step to selected direction 
    def move(self, tail_addition = False):
        row, col = self.body[0]
        
        match self.direction:
            case "right":
                col = col + 1
            case "up":
                row = row - 1
            case "left":
                col = col - 1
            case "down":
                row = row + 1
                
        new_head = [row, col] 
        self.body.insert(0, new_head)
            
        # Add one more unit to tail of snake after eating food 
        if not tail_addition:
            self.body.pop()
            

class Food:
    def __init__(self, food_location = None):
        # location: coordinate of the food
        self.food_location = food_location

    # Choose random food location and put it on a coordinate of the map
    def random_location(self, map_width, map_height):
        food_row = random.randint(0, map_width - 1)
        food_col = random.randint(0, map_height - 1)
        
        self.food_location = [food_row, food_col]


class Game:
    #controls the Game logic
    def __init__(self, board, snake, food, map_width, map_height, score = 0):
        self.board = board
        self.snake = snake
        self.food = food
        self.game_over = False
        self.map_width = map_width
        self.map_height = map_height
        self.score = score
        self.tail_addition = False


    def control_eat(self):
        # Check head location with food location to check if it ate the food
        if self.food.food_location == self.snake.body[0]:
            self.score += 1
            self.tail_addition = True

            while True:
                self.food.random_location(self.map_width, self.map_height)
                if self.food.food_location in self.snake.body:
                    continue
                else:
                    break         
            return "food-eaten"
        return None  



    def control_hit(self):
        # Check head location with location of walls around the region or its body 
        # 1. Self-Collision:
        for i in self.snake.body[1:]:
            if i == self.snake.body[0]:
                self.game_over = True
             
        
        # 2. Wall-collision
        row_head, col_head = self.snake.body[0]
        if row_head >= self.map_height or row_head < 0 or col_head >= self.map_width or col_head < 0:
            self.game_over = True
        
