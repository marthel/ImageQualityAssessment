from enum import Enum


class shift(Enum):
    up = [-1, 0]
    down = [1, 0]
    right = [1, 1]
    left = [-1, 1]
