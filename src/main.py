import pygame
from .config import WIDTH, HEIGHT, CELL_SIZE, FPS
from .renderer import Renderer
from .gamelogic import TicTacToe

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