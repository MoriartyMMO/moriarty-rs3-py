from typing import Union, TYPE_CHECKING

from .node import MNode
from ..debug.mlog import log

if TYPE_CHECKING:
    from ._scene import Animation, ActionType, Vec2i, get_hero_position
else:
    from cockbot5.core import log
    from cockbot5.scene import Vec2i, Animation, ActionType, get_hero_position


class MAnimation(Animation):
    name: str
    position: Vec2i
    id: int
    options: list[str]

    def __init__(self):
        """
        No initialization needed.

        Don't touch this.
        """
        super().__init__()

    @classmethod
    def from_animation(cls, animation):
        if not isinstance(animation, Animation):
            raise ValueError("Expected a Animation instance")

        moriarty_animation = cls()
        moriarty_animation.position = animation.get_position()
        # moriarty_animation.id = animation.get_id()
        return moriarty_animation

    def distance(self) -> int:
        """
        Calculates the distance between you and the animation.

        :return The distance between you and the entity.
        """
        pos = get_hero_position()
        return int(
            ((self.position.x - pos.x) ** 2 + (self.position.y - pos.y) ** 2) ** 0.5
        )

    def get_node(self, node_list) -> Union[MNode, None]:
        """
        Get the node of the animation.

        :return The node of the animation.
        """
        nodes = [
            node for node
            in node_list
            if node.position.x == self.position.x
            and node.position.y == self.position.y
        ]
        results = len(nodes)

        if results == 0:
            return None

        if results > 1:
            log("More than one node found for animation. This is odd.")

        return nodes.pop()
