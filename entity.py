from __future__ import annotations
from typing import Tuple, TypeVar, TYPE_CHECKING

import copy

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound="Entity")

class Entity:
    """
    A generic object to represent objects in the world, like the player, enemies, items, etc...
    """

    def __init__(
        self, 
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        blocks_movement: bool = False,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
    
    def spawn(self: T, game_map: GameMap, x: int, y: int) -> T:
        """Spawns a copy of this instance at the given location."""

        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        game_map.entities.add(clone)
        return clone