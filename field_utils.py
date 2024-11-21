from typing import List

from configurations import EMPTY_CELL, FIELD_SIZE


def find_empty_cells(field: List[List]) -> List[List[int]]:
    empty_cells = []
    for row in range(FIELD_SIZE):
        for column in range(FIELD_SIZE):
            if field[row][column] == EMPTY_CELL:
                empty_cells.append([row, column])
    return empty_cells


def visualize_field(field: List[List]) -> None:
    for row in range(FIELD_SIZE):
        for column in range(FIELD_SIZE):
            print(field[row][column], end='  ')
        print()
    print()
