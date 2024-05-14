from enum import Enum


class Vec2i:
    x: int = ...
    y: int = ...


class ActionType(Enum):
    OBJECT_ONE = 1,
    OBJECT_TWO = 2,
    OBJECT_THREE = 3,
    LOC_ONE = 4,
    ENTITY_ONE = 5,
    ENTITY_TWO = 6,
    ENTITY_THREE = 7,
    ENTITY_FOUR = 8,
    ENTITY_FIVE = 9,
    ENTITY_SIX = 10,
    OBJECT_FOUR = 11,
    OBJECT_FIVE = 12,
    OBJECT_SIX = 13,
    GROUND_ITEM_ONE = 14,
    GROUND_ITEM_TWO = 15,
    #
    # These are temporary for personal use.
    # They are to interact with scene objects which are
    # currently unsupported.
    #
    PRESET = 69,
    HARVEST = 70
    REPAIR_ALL = 71


class ObjectType(Enum):
    NPC = 1,
    PLAYER = 2,
    GROUND_ITEM = 3,
    ANIMATION = 4,
    LOCATION = 12


class Node:
    def __init__(self) -> None: ...
    def get_name(self) -> str: ...
    def get_position(self) -> Vec2i: ...
    def get_type(self) -> int: ...
    def get_id(self) -> int: ...
    def get_option(self, option_index: int) -> str: ...

    def _do_action(
        self,
        id: int,
        x: int,
        y: int,
        action_type: ActionType
    ) -> None: ...


class Entity:
    def __init__(self) -> None: ...
    def get_name(self) -> str: ...
    def get_position(self) -> Vec2i: ...
    def get_type(self) -> int: ...
    def get_id(self) -> int: ...
    def _do_action(self, id: int, action_type: ActionType) -> None: ...
    def get_combat_level(self) -> int: ...
    def get_animation(self) -> int: ...


class GroundItem:
    def __init__(self) -> None: ...
    def get_name(self) -> str: ...
    def get_price(self) -> int: ...
    def get_position(self) -> Vec2i: ...
    def get_type(self) -> int: ...
    def get_id(self) -> int: ...

    def _do_action(
        self, id: int, x: int, y: int, action_type: ActionType
    ) -> None: ...


class Animation:
    def __init__(self) -> None: ...
    def get_position(self) -> Vec2i: ...
    # def get_id(self) -> int: ...


def get_hero_position() -> Vec2i: ...
def get_hero_animation() -> int: ...
def get_entities(object_type: ObjectType) -> list: ...
def walk(x: int, y: int) -> None: ...
