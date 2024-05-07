from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._scene import Node, ActionType, Vec2i, get_hero_position
else:
    from cockbot5.core import log
    from cockbot5.scene import Vec2i, Node, ActionType, get_hero_position


class MNode(Node):
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
    def from_node(cls, node):
        if not isinstance(node, Node):
            raise ValueError("Expected a Node instance")

        moriarty_node = cls()
        moriarty_node.name = node.get_name()
        moriarty_node.position = node.get_position()
        moriarty_node.id = node.get_id()
        moriarty_node.hidden = node.is_hidden()
        moriarty_node.options = []
        for i in range(1, 4):
            moriarty_node.options.append(node.get_option(i))
        return moriarty_node

    def do_action(self, action: ActionType) -> None:
        """
        Perform an action on the node.

        :param action: The action to perform.
        """
        self._do_action(self.id, self.position.x, self.position.y, action)

    def distance(self) -> int:
        """
        Calculates the distance between you and the node.

        :return The distance between you and the entity.
        """
        pos = get_hero_position()
        return int(
            ((self.position.x - pos.x) ** 2 + (self.position.y - pos.y) ** 2) ** 0.5
        )
