from dataclasses import dataclass

BOARD_SIZE = 19

@dataclass
class Stone:
    x: int
    y: int
    color: bool
    group: "Group" = None
    prev: int = BOARD_SIZE * x + y

    def __str__(self):
        return f"{self.x} {self.y} {"black" if self.color else "white"}"


class Group:
    def __init__(self, stone: Stone):
        self.first_stone = (stone.x, stone.y)
        self.stones: set = set({stone})
        stone.group = self
        
    
    def add_stone(self, stone: "Stone"):
        self.stones.add(stone)

    
    def unite(self, group1: "Group", group2: "Group") -> "Group":
        ...

    def __del__():
        ...

    
class Pole:
    ...

class Game:
    ...

