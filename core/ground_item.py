from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._scene import (
        GroundItem,
        ActionType,
        Vec2i,
        Entity,
        GroundItem,
        get_hero_position
    )
else:
    from cockbot5.core import log
    from cockbot5.scene import Vec2i, GroundItem, ActionType, get_hero_position


class MGroundItem(GroundItem):
    id: int
    name: str
    price: int
    position: Vec2i

    def __init__(self):
        """
        No initialization needed.

        Don't touch this.
        """
        super().__init__()

    @classmethod
    def from_ground_item(cls, ground_item):
        if not isinstance(ground_item, GroundItem):
            raise ValueError("Expected an ground_item instance")

        moriarty_item = cls()
        moriarty_item.name = ground_item.get_name()
        moriarty_item.price = ground_item.get_price()
        moriarty_item.position = ground_item.get_position()
        moriarty_item.id = ground_item.get_id()
        return moriarty_item

    def do_action(self, action: ActionType) -> None:
        """
        Perform an action on the GroundItem.

        :param action: The action to perform.
        """
        self._do_action(self.id, self.position.x, self.position.y, action)

    def distance(self) -> int:
        """
        Calculates the distance between you and the GroundItem.

        :return The distance between you and the GroundItem.
        """
        pos = get_hero_position()
        return int(
            ((self.position.x - pos.x) ** 2 + (self.position.y - pos.y) ** 2) ** 0.5
        )
