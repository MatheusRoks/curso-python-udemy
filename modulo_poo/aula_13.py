# enum
import enum


class Direction(enum.Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
# Direction = enum.Enum("Direction", ['NORTH', 'SOUTH', 'EAST', 'WEST'])


def move(direction: Direction):
    if not isinstance(direction, Direction):
        raise ValueError("Invalid direction")
    print(f'Movendo para {direction}')


move(Direction.NORTH)
move(Direction.EAST)
