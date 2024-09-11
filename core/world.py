from time import sleep

from .node import MNode
from .entity import MEntity
from .ground_item import MGroundItem
from .animation import MAnimation

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ._scene import (
        ActionType,
        ObjectType,
        Entity,
        Node,
        GroundItem,
        Animation,
        Vec2i,
        get_hero_position,
        get_entities,
    )
else:
    from cockbot5.scene import (
        Vec2i,
        Entity,
        Node,
        GroundItem,
        Animation,
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
        m_nodes = [MNode.from_node(node) for node in nodes if isinstance(node, Node)]
        return [node for node in m_nodes if len(node.name) > 1]

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
            # There's some black magic oscillating crystal shit going on
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

    @property
    def animations(self) -> list[MAnimation]:
        animations = get_entities(ObjectType.ANIMATION)
        return [
            MAnimation.from_animation(animation)
            for animation in animations
            if isinstance(animation, Animation)
        ]

    def get_node_blocking(
        self, name, limit=0, iteration_delay=0.1
    ) -> Union[MNode, None]:
        """
        Filters nodes by name. Case-insensitive.
        Blocks until the node is found.

        :param name: The name of the node to find.
        :param limit: The maximum number of nodes to search for. 0 for no limit.
        :param iteration_delay: The delay between attempts to find node in seconds.
        """
        nodes = [n for n in self.nodes if n.name.lower() == name.lower()]
        iterations = 0
        while len(nodes) == 0 and iterations <= limit:
            nodes = [n for n in self.nodes if n.name.lower() == name.lower()]
            iterations += 1
            if iteration_delay > 0:
                sleep(iteration_delay)

        try:
            return nodes.pop()
        except IndexError:
            return None

    def npc_with_name(self, name) -> Union[MEntity, None]:
        """
        Filters NPCs by name. Case-insensitive.
        """
        entities = [e for e in self.npcs if e.name.lower() == name.lower()]
        if len(entities) == 0:
            return None
        return entities.pop()

    def npc_with_name_contains(self, name_substr) -> Union[MEntity, None]:
        """
        Filters NPCs by name substr. Case-insensitive.
        """
        entities = [e for e in self.npcs if name_substr.lower() in e.name.lower()]
        if len(entities) == 0:
            return None
        return entities.pop()

    def node_with_name(self, name) -> Union[MNode, None]:
        """
        Filters nodes by name. Case-insensitive.
        """
        nodes = [n for n in self.nodes if n.name.lower() == name.lower()]
        if len(nodes) == 0:
            return None
        return nodes.pop()

    def nodes_with_name(self, name):
        nodes = [n for n in self.nodes if n.name.lower() == name.lower()]
        return nodes
