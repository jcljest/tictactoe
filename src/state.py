# src/state.py
from typing import List, Optional

Player = str
Board = List[List[Optional[Player]]]

class GameState:
    def __init__(self, board: Board, winner: Optional[Player], is_draw: bool):
        self.board = board
        self.winner = winner
        self.is_draw = is_draw
