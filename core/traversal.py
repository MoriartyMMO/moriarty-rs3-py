from typing import TYPE_CHECKING

from time import sleep

if TYPE_CHECKING:
    from ._scene import (
        get_hero_position,
        walk,
    )
else:
    from cockbot5.core import log, key_press
    from cockbot5.scene import Vec2i, GroundItem, ActionType, get_hero_position, walk


def walk_to(x: int, y: int) -> None:
    """
    Walk to the specified tile.

    :param x: The x coordinate to walk to.
    :param y: The y coordinate to walk to.
    """
    walk(x, y)
    while get_hero_position().x != x or get_hero_position().y != y:
        sleep(0.6)
