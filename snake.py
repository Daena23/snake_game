from math import floor

from configuration import COORD_VARS, WADS, WALL, SNAKE_TAIL, DEAD_SNAKE, field_size


class Snake:
    def __init__(self):
        self.length = 3
        self.alive = True
        self.increase_length = False
        self.direction = 'd'
        self.tail_symbol = SNAKE_TAIL
        self.head_symbol = COORD_VARS[WADS.index(self.direction)][3]
        self.coordinates = []
        # a = (list(filter(lambda x: x == COORD_VARS[3], COORD_VARS))[0][3])
        self.find_init_coordinates()

    def find_init_coordinates(self):
        center = floor(field_size / 2)
        self.coordinates = [[center, center - i] for i in range(self.length)]
        return

    def move(self, field):
        new_coordinates = []
        row_dir, column_dir = COORD_VARS[WADS.index(self.direction)][1], COORD_VARS[WADS.index(self.direction)][2]
        self.head_symbol = COORD_VARS[WADS.index(self.direction)][3]
        row_shuttle, column_shuttle = self.coordinates[0]
        row_end, column_end = self.coordinates[len(self.coordinates) - 1]
        if field[row_shuttle + row_dir][column_shuttle + column_dir] == WALL:
            self.hits_wall()
            return self.coordinates
        else:
            new_coordinates.append([row_shuttle + row_dir, column_shuttle + column_dir])  # head moves
            for coordinates in range(len(self.coordinates[1:])):  # tail catches up
                previous_coord = self.coordinates[1:][coordinates]
                new_coordinates.append([row_shuttle, column_shuttle])
                row_shuttle, column_shuttle = previous_coord
            if self.increase_length:
                new_coordinates.append([row_end, column_end])
                self.length += 1
                self.increase_length = False
            print(self.coordinates, 'af')
            print(new_coordinates, 'n')
            if self.if_crushes_into_itself(new_coordinates):
                return self.coordinates
            return new_coordinates

    def hits_wall(self):
        self.alive = False

    def if_crushes_into_itself(self, new_coordinates):
        overlay_coordinates_list = []
        for coord in new_coordinates:
            if coord in overlay_coordinates_list:
                self.alive = False
                return
            overlay_coordinates_list.append(coord)

    def act_if_died(self):
        if not self.alive:
            self.tail_symbol = self.head_symbol = DEAD_SNAKE
