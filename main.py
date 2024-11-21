import copy

from field_utils import visualize_field
from game_initiation import field_init, snake_init
from loop_functions import snake_loop, yummy_loop


def main():
    # Initial parameters
    field, basic_field = field_init()
    snake, field = snake_init(field)
    game_counter = 0
    all_yummies = []
    visualize_field(field)
    # Game loop
    while snake.alive:
        field = copy.deepcopy(basic_field)
        all_yummies = yummy_loop(all_yummies, game_counter, snake, field)
        snake_loop(snake, field)
        visualize_field(field)
        game_counter += 1
    print('Game over')


if __name__ == '__main__':
    main()
