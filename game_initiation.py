import copy
from typing import Tuple, List

from configurations import EMPTY_CELL, WALL, FIELD_SIZE
from loop_functions import put_snake
from snake import Snake


def field_init() -> Tuple[List[List], List[List[str]]]:
    field = create_basic_field(FIELD_SIZE)
    return field, create_basic_field(FIELD_SIZE)


def create_basic_field(size: int) -> List[List[str]]:
    empty_field = [[EMPTY_CELL for _ in range(size)] for _ in range(size)]
    wall_coordinates = define_wall_coordinates(size)
    basic_field = copy.deepcopy(empty_field)
    for row, column in wall_coordinates:
        basic_field[row][column] = WALL
    return basic_field


def define_wall_coordinates(size: int) -> List[List[int]]:
    border = [0, size - 1]
    walls_coordinates = []
    for i in range(size):
        for j in range(size):
            if i in border and [i, j] not in walls_coordinates:
                walls_coordinates.append([i, j])
            if j in border and [i, j] not in walls_coordinates:
                walls_coordinates.append([i, j])
    return walls_coordinates


def snake_init(field: List[List]) -> tuple[Snake, List[List]]:
    snake = Snake()
    field = put_snake(snake, field)
    return snake, field
