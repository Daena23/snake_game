import copy
from loop_functions import put_snake
from configuration import field_size, EMPTY_CELL, WALL
from snake import Snake
from yummy import Yummy


def field_init():
    return basic_field_creation(field_size), basic_field_creation(field_size)


def basic_field_creation(field_size):
    empty_field = [[EMPTY_CELL for _ in range(field_size)] for _ in range(field_size)]
    walls_coordinates = define_walls_coordinates(field_size)
    return create_basic_field(empty_field, walls_coordinates)


def define_walls_coordinates(field_size):
    # border
    border = [0, field_size - 1]
    walls_coordinates = []
    for i in range(field_size):
        for j in range(field_size):
            if i in border and [i, j] not in walls_coordinates:  # TODO edit
                walls_coordinates.append([i, j])
            if j in border and [i, j] not in walls_coordinates:
                walls_coordinates.append([i, j])
    return walls_coordinates


def create_basic_field(empty_field, walls_coordinates):
    basic_field = copy.deepcopy(empty_field)
    for row, column in walls_coordinates:
        basic_field[row][column] = WALL
    return basic_field


def snake_init(field):
    snake = Snake()
    field = put_snake(snake, field)
    return snake, field


def yummy_init(field, game_counter):
    yummy = Yummy(field, game_counter)
    yummy_list = []
    return yummy, yummy_list
