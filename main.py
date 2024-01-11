from game_initiation import field_init, snake_init, yummy_init
from loop_functions import field_loop, snake_loop, yummy_loop


def main():
    # initial parameters
    game_counter = 0
    field, basic_field = field_init()
    snake, field = snake_init(field)
    yummy, yummy_list = yummy_init(field, game_counter)
    # game loop
    while snake.alive:
        field = field_loop(field, basic_field)
        snake_loop(snake, field)
        yummy_list = yummy_loop(yummy_list, yummy, game_counter, snake, field)
        game_counter += 1
    field = field_loop(field, basic_field)
    print('Game over')
# если в себя назад, то хвостик успеет подтянцться ??? in move


if __name__ == '__main__':
    main()
