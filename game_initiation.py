import copy

from configuration import EMPTY_CELL, WALL, field_size
from loop_functions import put_snake
from snake import Snake


def field_init() -> tuple[list[list], list[list[str]]]:
    field = create_basic_field(field_size)
    return field, create_basic_field(field_size)


def create_basic_field(size: int) -> list[list[str]]:
    empty_field = [[EMPTY_CELL for _ in range(size)] for _ in range(size)]
    walls_coordinates = define_walls_coordinates(size)
    basic_field = copy.deepcopy(empty_field)
    for row, column in walls_coordinates:
        basic_field[row][column] = WALL
    return basic_field


def define_walls_coordinates(size: int) -> list[list[int]]:
    border = [0, size - 1]
    walls_coordinates = []
    for i in range(size):
        for j in range(size):
            if i in border and [i, j] not in walls_coordinates:
                walls_coordinates.append([i, j])
            if j in border and [i, j] not in walls_coordinates:
                walls_coordinates.append([i, j])
    return walls_coordinates


def snake_init(field: list[list]) -> tuple[Snake, list[list]]:
    snake = Snake()
    field = put_snake(snake, field)
    return snake, field
