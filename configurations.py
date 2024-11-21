from random import randint

# Symbols
EMPTY_CELL = ' '
WALL = '□'
# Snake's symbols
SNAKE_TAIL = 'о'
SNAKE_HEAD_LEFT = '◄'  # ▲ ► ▼ ◄
SNAKE_HEAD_UP = '▲'
SNAKE_HEAD_RIGHT = '►'
SNAKE_HEAD_DOWN = '▼'
DYING_SNAKE = '҈'
YUMMY = '♣'  # 🎂

# Game parameters
FIELD_SIZE = 9
YUMMY_PROBABILITY = 0.25
YUMMY_MAX_NUM = 3
YUMMY_LIFESPAN = randint(5, 10)

COORD_VARS = [
    ['w', -1, 0, SNAKE_HEAD_UP],
    ['d', 0, 1, SNAKE_HEAD_RIGHT],
    ['s', 1, 0, SNAKE_HEAD_DOWN],
    ['a', 0, -1, SNAKE_HEAD_LEFT]
]

WADS = [COORD_VARS[i][0] for i in range(len(COORD_VARS))]