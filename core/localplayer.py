from ..debug.mlog import log

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ._localplayer import (
        get_health,
        get_prayer_points,
        get_summoning_points
    )
    from ._scene import get_hero_animation
else:
    from cockbot5.localplayer import (
        get_health,
        get_prayer_points,
        get_summoning_points
    )
    from cockbot5.scene import get_hero_animation


class LocalPlayer:

    @property
    def health(self) -> int:
        """
        Get the player's current health.

        :return The player's current health.
        """
        return get_health()

    @property
    def prayer_points(self) -> int:
        """
        Get the player's current prayer points.

        :return The player's current prayer points.
        """
        return int(get_prayer_points() / 10)

    @property
    def summoning_points(self) -> int:
        """
        Get the player's current summoning points.

        :return The player's current summoning points.
        """
        return get_summoning_points()

    @property
    def animation(self) -> int:
        """
        Get the player's current animation.

        :return The player's current animation.
        """
        return get_hero_animation()
