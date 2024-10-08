from typing import TYPE_CHECKING

from ..debug.mlog import log
if TYPE_CHECKING:
    from ._scene import ActionType, Vec2i, Entity, get_hero_position
else:
    from cockbot5.scene import Vec2i, Entity, ActionType, get_hero_position


class MEntity(Entity):
    name: str
    combat_level: int
    position: Vec2i
    id: int
    # We need this or Pybind11 just fucking nukes it.
    # Because apparently they didn't think about
    # inheritance too much.
    obj: Entity

    def __init__(self):
        """
        No initialization needed.

        Don't touch this.
        """
        super().__init__()

    @classmethod
    def from_entity(cls, entity):
        """
        Takes in an instance of the native-defined `Entity`
        and returns a Python-defined `MEntity`.

        :return MEntity
        """
        if not isinstance(entity, Entity):
            log("Expected an Entity instance, got {}".format(type(entity)))

        moriarty_entity = cls()
        moriarty_entity.name = entity.get_name()
        moriarty_entity.combat_level = entity.get_combat_level()
        moriarty_entity.position = entity.get_position()
        moriarty_entity.id = entity.get_id()
        moriarty_entity.obj = entity
        return moriarty_entity

    def get_animation(self) -> int:
        """
        return: The current animation id of the Entity.
        """
        return self.obj.get_animation()

    def log_animation(self):
        """
        Logs the entity's current animation.
        """
        log(f"{self.name} animation: {str(self.obj.get_animation())}")

    def do_action(self, action: ActionType) -> None:
        """
        Perform an action on the entity.

        :param action: The action to perform.
        """
        self._do_action(self.id, action)

    def distance(self) -> int:
        """
        Calculates the distance between you and the entity.

        :return The distance between you and the entity.
        """
        pos = get_hero_position()
        return int(
            ((self.position.x - pos.x) ** 2 + (self.position.y - pos.y) ** 2) ** 0.5
        )
