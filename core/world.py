from ..debug.mlog import log
from .node import MNode
from .entity import MEntity
from .ground_item import MGroundItem

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ._scene import (
        ActionType,
        ObjectType,
        Entity,
        Node,
        GroundItem,
        Vec2i,
        get_hero_position,
        get_entities
    )
else:
    from cockbot5.core import log
    from cockbot5.scene import (
        Vec2i,
        Entity,
        Node,
        GroundItem,
        ActionType,
        ObjectType,
        get_hero_position,
        get_entities,
    )


class World:
    @property
    def nodes(self) -> list[MNode]:
        """
        Get all nodes in the world.

        :return A list of all nodes in the world.
        """
        nodes = get_entities(ObjectType.LOCATION)
        return [
            MNode.from_node(node)
            for node in nodes
            if isinstance(node, Node)
        ]

    @property
    def npcs(self) -> list[MEntity]:
        """
        Get all NPCs in the world.

        :return A list of all NPCs in the world.
        """
        npcs = get_entities(ObjectType.NPC)
        return [
            MEntity.from_entity(npc)
            for npc in npcs
            # There's some black magig oscillating crystal shit going on
            # with Pybind11. We need to ensure we are actually only getting
            # Entities here.
            # It is not a problem with the native code I wrote.
            # This only happens when get_entities is called from Python.
            # Kill yourself @pybind11
            if isinstance(npc, Entity)
        ]

    @property
    def ground_items(self) -> list[MGroundItem]:
        """
        Get all ground items in the world.

        :warning When passing into functions like min, max, sorted, etc,
        ensure that a populated list was returned. Otherwise you will crash.

        :return A list of all ground items.
        """
        ground_items = get_entities(ObjectType.GROUND_ITEM)
        return [
            MGroundItem.from_ground_item(ground_item)
            for ground_item in ground_items
            if isinstance(ground_item, GroundItem)
        ]
