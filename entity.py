from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc
    """

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]) -> None:
        """
        Creates an entity object with the given properties (color, char to use, position, etc.)
        """
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int):
        """
        Lets entity move in the given direction
        """
        self.x += dx
        self.y += dy
