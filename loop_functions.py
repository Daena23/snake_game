import random
import copy
from configuration import WADS, field_size
from yummy import Yummy
from field_utils import visualize_field, find_empty_cells


def field_loop(field, basic_field):
    visualize_field(field)
    # find_empty_cells(field)
    return copy.deepcopy(basic_field)


def yummy_loop(yummy_list, yummy, game_counter, snake, field):
    if random.random() < yummy.probability and len(yummy_list) < yummy.max_number:
        yummy_list.append(Yummy(field, game_counter))
    for yummy in yummy_list:
        # yummy disappears
        yummy.exists = (game_counter != yummy.counter + yummy.lifespan)
        yummy.check_if_eaten(snake)
        # put yummy
        yummy_row, yummy_column = yummy.coordinates
        if field[yummy_row][yummy_column] != snake.head_symbol:
            field[yummy_row][yummy_column] = yummy.symbol
    return list(filter(lambda yummy: yummy.exists, yummy_list))


def snake_loop(snake, field):
    snake.direction = command()
    snake.coordinates = snake.move(field)
    snake.act_if_died()
    put_snake(snake, field)


def command():
    event = input('Print w, a, s or d')
    while True:
        if event in WADS:
            return event
        else:
            event = input('Wrong input. Print w, a, s or d')


def put_snake(snake, field):
    head_row, head_column = snake.coordinates[0]
    field[head_row][head_column] = snake.head_symbol
    for coordinates in snake.coordinates[1:]:
        row, column = coordinates
        field[row][column] = snake.tail_symbol
    return field

