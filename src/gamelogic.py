from typing import Optional
from .config import Player, Board

# =========================
# Game Logic
# =========================
class TicTacToe:
    def __init__(self):
        self.board: Board = [[None for _ in range(4)] for _ in range(4)]
        self.current_player: Player = "X"
        self.winner: Optional[Player] = None
        self.is_draw = False

    def make_move(self, row: int, col: int) -> bool:
        if self.winner or self.is_draw:
            return False

        if self.board[row][col] is not None:
            return False

        self.board[row][col] = self.current_player
        self._update_game_state()

        if not self.winner:
            self._switch_player()

        return True

    def _switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def _update_game_state(self):
        self.winner = self._check_winner()
        if not self.winner and all(cell is not None for row in self.board for cell in row):
            self.is_draw = True

    def _check_winner(self) -> Optional[Player]:
        lines = []

        lines.extend(self.board)
        lines.extend(zip(*self.board))
        lines.append([self.board[i][i] for i in range(4)])
        lines.append([self.board[i][2 - i] for i in range(4)])

        for line in lines:
            if line[0] is not None and all(cell == line[0] for cell in line):
                return line[0]

        return None

    def reset(self):
        self.__init__()
