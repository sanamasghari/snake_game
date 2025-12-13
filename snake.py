""" 
This file consists features and logic of the game using OOP (classes) 

"""


class Snake:
    # body: The coordinates of snake body 
    # direction: The movment direction of snake Up, Down, Left, Right
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction

    # Move snake one step to selected direction 
    def move(self):
        pass

    # Add one more unit to tail of snake after eating food 
    def grow(self):
        pass


class Food:
    def __init__(self, location):
        # location: coordinate of the food
        self.location = location

    # Choose random food location and put it on a coordinate of the map
    def random_location(self):
        pass


class Game:
    #controls the Game logic
    def __init__(self, board, snake, food):
        self.board = board
        self.snake = snake
        self.food = food
        self.game_over = False

    def control_eat(self):
        # Check head location with food location to check if it ate the food
        pass

    def control_hit(self):
        # Check head location with location of walls around the region or its body 
        pass

    def control_end(self):
        # Check whether the game should end
        pass
