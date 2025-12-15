import pygame
import os
from typing import Optional, List

# =========================
# Configuration
# =========================
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS
FPS = 60

BG_COLOR = (25, 25, 25)
GRID_COLOR = (220, 220, 220)
TEXT_COLOR = (240, 240, 240)

Player = str  # "X" or "O"
Board = List[List[Optional[Player]]]

# =========================
# Game Logic
# =========================
class TicTacToe:
    def __init__(self):
        self.board: Board = [[None for _ in range(3)] for _ in range(3)]
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
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0] is not None and all(cell == line[0] for cell in line):
                return line[0]

        return None

    def reset(self):
        self.__init__()

# =========================
# Renderer
# =========================
class Renderer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 64)

        base_dir = os.path.dirname(__file__)
        assets_dir = os.path.join(base_dir, "assets")

        self.x_img = pygame.image.load(
            os.path.join(assets_dir, "x.png")
        ).convert_alpha()

        self.o_img = pygame.image.load(
            os.path.join(assets_dir, "o.png")
        ).convert_alpha()

        self.x_img = pygame.transform.smoothscale(
            self.x_img, (CELL_SIZE, CELL_SIZE)
        )
        self.o_img = pygame.transform.smoothscale(
            self.o_img, (CELL_SIZE, CELL_SIZE)
        )

    def draw_board(self):
        self.screen.fill(BG_COLOR)

        for i in range(1, ROWS):
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (0, i * CELL_SIZE),
                (WIDTH, i * CELL_SIZE),
                4,
            )
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (i * CELL_SIZE, 0),
                (i * CELL_SIZE, HEIGHT),
                4,
            )

    def draw_pieces(self, board: Board):
        for r in range(ROWS):
            for c in range(COLS):
                piece = board[r][c]
                if piece == "X":
                    self.screen.blit(self.x_img, (c * CELL_SIZE, r * CELL_SIZE))
                elif piece == "O":
                    self.screen.blit(self.o_img, (c * CELL_SIZE, r * CELL_SIZE))

    def draw_status(self, game: TicTacToe):
        message = None
        if game.winner:
            message = f"{game.winner} wins! Press R to reset"
        elif game.is_draw:
            message = "It's a draw! Press R to reset"

        if not message:
            return

        text_surf = self.font.render(message, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        padding = 20
        bg_rect = text_rect.inflate(padding * 2, padding * 2)
        pygame.draw.rect(self.screen, BG_COLOR, bg_rect)
        pygame.draw.rect(self.screen, GRID_COLOR, bg_rect, 2)
        self.screen.blit(text_surf, text_rect)

# =========================
# Main Loop
# =========================
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")
    clock = pygame.time.Clock()

    game = TicTacToe()
    renderer = Renderer(screen)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                game.make_move(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()

        renderer.draw_board()
        renderer.draw_pieces(game.board)
        renderer.draw_status(game)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
