from configuration import EMPTY_CELL, field_size


def find_empty_cells(field: list[list]) -> list[list[int]]:
    empty_cells = []
    for row in range(field_size):
        for column in range(field_size):
            if field[row][column] == EMPTY_CELL:
                empty_cells.append([row, column])
    return empty_cells


def visualize_field(field: list[list]) -> None:
    for row in range(field_size):
        for column in range(field_size):
            print(field[row][column], end='  ')
        print()
    print()
