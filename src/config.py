# =========================
# Configuration
# =========================
from typing import Optional, List


WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
CELL_SIZE = WIDTH // COLS
FPS = 60

BG_COLOR = (25, 25, 25)
GRID_COLOR = (220, 220, 220)
TEXT_COLOR = (240, 240, 240)

Player = str  # "X" or "O"
Board = List[List[Optional[Player]]]

##############