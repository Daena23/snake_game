from math import floor

from configuration import COORD_VARS, DEAD_SNAKE, SNAKE_TAIL, WADS, field_size


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

    def find_init_coordinates(self) -> None:
        center = floor(field_size / 2)
        self.coordinates = [[center, center - i] for i in range(self.length)]
        return

    @staticmethod
    def command() -> str:
        event = input('Input w, a, s or d')
        while True:
            if event in WADS:
                return event
            else:
                event = input('Wrong input. Print w, a, s or d')

    def hits_wall(self) -> None:
        self.alive = False

    def if_crushes_into_itself(self, new_coordinates: list[list[int]]):
        shuttle_set = set()
        for coordinates in new_coordinates:
            coordinates_tuple = tuple(coordinates)
            if coordinates_tuple in shuttle_set:
                self.alive = False
                return self.coordinates
            shuttle_set.add(coordinates_tuple)

    def act_if_died(self) -> None:
        if not self.alive:
            self.tail_symbol = self.head_symbol = DEAD_SNAKE
