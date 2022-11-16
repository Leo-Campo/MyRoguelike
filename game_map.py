import numpy as np
from tcod.console import Console

import tile_types


class GameMap:
    """
    Class used to create the game map using tiles
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Returns true if x and y are inside the bounds of this map
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """Renders the tiles on the console using the dark visualisation"""
        console.tiles_rgb[0 : self.width, 0 : self.height] = self.tiles["dark"]