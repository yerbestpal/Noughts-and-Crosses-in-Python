import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Courier New', 40)
window_size = (450, 500)
cell_size = 150

running = True
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Tic Tac Toe')

class TicTacToe():

    def __init__(self, table_size):
        self.table_size = table_size
        self.cell_size = table_size // 3
        self.table_space = 20
        self.table = []

        for col in range(3):
            self.table.append([])
            for row in range(3):
                self.table[col].append("-")
        
        self.player = "X"
        self.winner = None
        self.taking_move = True
        self.running = True

        self.background_color = (255, 174, 66)
        self.table_color = (50, 50, 50)
        self.line_color = (190, 0, 10)
        self.instructions_color = (17, 53, 165)
        self.game_over_bg_color = (47, 98, 162)
        self.game_over_color = (255, 179, 1)
        self.font = pygame.font.SysFont('Courier New', 35)
        self.FPS = pygame.time.Clock()

    def main(self):
        screen.fill(self.background_color)
        self._draw_table()

        while self.running:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
            
            pygame.display.flip()
            self.FPS.tick(60)
    
    # Draws the game board
    def _draw_table(self):
        tb_space_point = (self.table_space, self.table_size - self.table_space)
        cell_space_point = (self.cell_size, self.cell_size * 2)
        row_1 = pygame.draw.line(
            screen, 
            self.table_color, 
            [
                tb_space_point[0],
                cell_space_point[0]
            ],
            [
                tb_space_point[1],
                cell_space_point[0]
            ],
            8
        )

        column_1 = pygame.draw.line(
            screen,
            self.table_color,
            [
                cell_space_point[0],
                tb_space_point[0]
            ],
            [
                cell_space_point[0],
                tb_space_point[1]
            ],
            8
        )

        row_2 = pygame.draw.line(
            screen,
            self.table_color,
            [
                tb_space_point[0],
                cell_space_point[1]
            ],
            [
                tb_space_point[1],
                cell_space_point[1]
            ],
            8
        )

        column_2 = pygame.draw.line(
            screen,
            self.table_color,
            [
                cell_space_point[1],
                tb_space_point[0]
            ],
            [
                cell_space_point[1],
                tb_space_point[1]
            ],
            8
        )

    def _move(self, pos):
        try:
            x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
            if self.table[x][y] == "-":
                self.table[x][y] = self.player
                self._draw_char(x, y, self.player)
                self._game_check()
                self._change_player()
        except:
            print("You can only click inside the table area")

if __name__ == '__main__':
    g = TicTacToe(window_size[0])
    g.main()