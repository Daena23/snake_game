import copy

from field_utils import visualize_field
from game_initiation import field_init, snake_init
from loop_functions import snake_loop, yummy_loop


def main():  # TODO почему юми выше змеи/ не сьедается?
    # initial parameters
    field, basic_field = field_init()
    snake, field = snake_init(field)
    game_counter = 0
    yummy_list = []
    visualize_field(field)
    # game loop
    while snake.alive:
        field = copy.deepcopy(basic_field)
        yummy_list = yummy_loop(yummy_list, game_counter, snake, field)
        snake_loop(snake, field)
        visualize_field(field)
        game_counter += 1
    print('Game over')


if __name__ == '__main__':
    main()
