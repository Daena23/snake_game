import random
from typing import List

from configurations import COORD_VARS, WADS, WALL
from snake import Snake
from yummy import Yummy


def yummy_loop(all_yummies: List[Yummy], game_counter: int, snake: Snake, field: List[List]) -> List[Yummy]:
    if random.random() < Yummy.probability and len(all_yummies) < Yummy.max_number:
        all_yummies.append(Yummy(field, game_counter))
    for yummy in all_yummies:
        yummy.exists = (game_counter != yummy.counter + Yummy.lifespan)  # yummy disappears
        yummy.check_if_eaten(snake)
        yummy_row, yummy_column = yummy.coordinates
        if field[yummy_row][yummy_column] != snake.head_symbol:
            field[yummy_row][yummy_column] = yummy.symbol
    return list(filter(lambda yummy_yummy: yummy.exists, all_yummies))


def snake_loop(snake: Snake, field: List[List]) -> None:
    snake.direction = snake.command()
    snake.coordinates = move_snake(snake, field)
    snake.act_if_died()
    put_snake(snake, field)


def move_snake(snake: Snake, field: List[List]) -> List[List[int]]:
    new_coordinates = []
    sn_dir = WADS.index(snake.direction)
    row_dir, column_dir, snake.head_symbol = COORD_VARS[sn_dir][1], COORD_VARS[sn_dir][2], COORD_VARS[sn_dir][3]
    row_shuttle, column_shuttle = snake.coordinates[0]
    row_end, column_end = snake.coordinates[len(snake.coordinates) - 1]
    if field[row_shuttle + row_dir][column_shuttle + column_dir] == WALL:
        snake.hits_wall()
        return snake.coordinates
    else:
        new_coordinates.append([row_shuttle + row_dir, column_shuttle + column_dir])  # head moves
        for coordinates in range(len(snake.coordinates[1:])):  # tail catches up
            previous_coord = snake.coordinates[1:][coordinates]
            new_coordinates.append([row_shuttle, column_shuttle])
            row_shuttle, column_shuttle = previous_coord
        if snake.increase_length:
            new_coordinates.append([row_end, column_end])
            snake.length += 1
            snake.increase_length = False
        if snake.if_crushes_into_itself(new_coordinates):
            return snake.coordinates
        return new_coordinates


def put_snake(snake: Snake, field: List[List]) -> List[List]:
    head_row, head_column = snake.coordinates[0]
    field[head_row][head_column] = snake.head_symbol
    for coordinates in snake.coordinates[1:]:
        row, column = coordinates
        field[row][column] = snake.tail_symbol
    return field
