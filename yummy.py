from random import choice
from typing import List

from configurations import YUMMY, YUMMY_PROBABILITY, YUMMY_MAX_NUM, YUMMY_LIFESPAN
from field_utils import find_empty_cells
from snake import Snake


class Yummy:
    probability = YUMMY_PROBABILITY
    max_number = YUMMY_MAX_NUM
    lifespan = YUMMY_LIFESPAN
    def __init__(self, field: List[List], game_counter: int) -> None:
        self.symbol = YUMMY
        self.counter = game_counter
        self.coordinates = choice(find_empty_cells(field))
        self.exists = True

    def check_if_eaten(self, snake: Snake) -> None:
        if self.coordinates == snake.coordinates[0]:
            self.exists = False
            snake.increase_length = True
