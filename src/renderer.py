import pygame
import os
from .config import WIDTH, CELL_SIZE, BG_COLOR, ROWS, HEIGHT, GRID_COLOR, TEXT_COLOR, COLS, Board
from .gamelogic import TicTacToe

# =========================
# Renderer
# =========================
class Renderer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 64)

        base_dir = os.path.dirname(__file__)
        assets_dir = os.path.join(base_dir, "../assets")

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