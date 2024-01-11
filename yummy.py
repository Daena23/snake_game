from random import choice
from field_utils import find_empty_cells
from configuration import YUMMY


class Yummy:
    def __init__(self, field, game_counter):
        self.symbol = YUMMY
        self.counter = game_counter
        self.coordinates = choice(find_empty_cells(field))
        self.lifespan = 6
        self.probability = 0.25
        self.max_number = 3
        self.exists = True

    def check_if_eaten(self, snake):
        if self.coordinates == snake.coordinates[0]:
            self.exists = False
            snake.increase_length = True
