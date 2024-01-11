# Symbols
EMPTY_CELL = ' '
WALL = '□'
# Snake's symbols
SNAKE_TAIL = 'о'
SNAKE_HEAD_LEFT = '◄'  # ▲ ► ▼ ◄
SNAKE_HEAD_UP = '▲'
SNAKE_HEAD_RIGHT = '►'
SNAKE_HEAD_DOWN = '▼'
DEAD_SNAKE = '҈'

YUMMY = '♣'  # 🎂'

field_size = 9

COORD_VARS = [
    ['w', -1, 0, SNAKE_HEAD_UP],
    ['d', 0, 1, SNAKE_HEAD_RIGHT],
    ['s', 1, 0, SNAKE_HEAD_DOWN],
    ['a', 0, -1, SNAKE_HEAD_LEFT]
]
WADS = [COORD_VARS[i][0] for i in range(len(COORD_VARS))]
