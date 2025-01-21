import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Courier New', 40)
window_size = (450, 500)
cell_size = 150

running = True
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Noughts and Crosses')

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
            self._message()
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    if self.taking_move:
                        self._move(self.event.pos)
            
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

    def _change_player(self):
        self.player = "O" if self.player == "X" else "X"

    # Processes the move
    def _move(self, pos):
        try:
            x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
            if self.table[x][y] == "-":
                self.table[x][y] = self.player
                self._draw_char(x, y, self.player)
                self._game_check()
                self._change_player()
        except:
            print("You may only click inside the table area")
    
    def _draw_char(self, x, y, player):
        if player == "O":
            img = pygame.image.load("images/o.png")
        elif player == "X":
            img = pygame.image.load("images/x.png")
        img = pygame.transform.scale(img, (self.cell_size, self.cell_size))
        screen.blit(img, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
    
    # Display instructions and game state messages
    def _message(self):
        if self.winner is not None:
            screen.fill(self.game_over_bg_color, (130, 445, 193, 35))
            msg = self.font.render(f'{self.winner} wins!', True, self.game_over_color)
            screen.blit(msg, (144, 445))
        elif not self.taking_move:
            screen.fill(self.game_over_bg_color, (130, 445, 193, 35))
            instructions = self.font.render('DRAW!!', True, self.game_over_color)
            screen.blit(instructions, (165, 445))
        else:
            screen.fill(self.background_color, (130, 445, 193, 35))
            instructions = self.font.render(f'{self.player} to move', True, self.instructions_color)
            screen.blit(instructions, (135, 445))

    def _game_check(self):
        # Vertical check
        for x_index, col in enumerate(self.table):
            win = True
            pattern_list = []
            for y_index, content in enumerate(col):
                if content != self.player:
                    win = False
                    break
                else:
                    pattern_list.append((x_index, y_index))
            if win == True:
                self._pattern_strike(pattern_list[0], pattern_list[-1], "ver")
                self.winner = self.player
                self.taking_move = False
                self._message()
                break
        
        # Horizontal check
        for row in range(len(self.table)):
            win = True
            pattern_list = []
            for col in range(len(self.table)):
                if self.table[col][row] != self.player:
                    win = False
                    break
                else:
                    pattern_list.append((col, row))

            if win == True:
                self._pattern_strike(pattern_list[0], pattern_list[-1], "hor")
                self.winner = self.player
                self.taking_move = False
                self._message()
                break
        
        # Left diagonal check
        for index, row in enumerate(self.table):
            win = True
            if row[index] != self.player:
                win = False
                break
        if win == True:
            self._pattern_strike((0, 0), (2, 2), "left-diag")
            self.winner = self.player
            self.taking_move = False
            self._message()
        
        # Right diagonal check
        for index, row in enumerate(self.table[::-1]):
            win = True
            if row[index] != self.player:
                win = False
                break
        if win == True:
            self._pattern_strike((2, 0), (0, 2), "right_diag")
            self.winner = self.player
            self.taking_move = False
            self._message()
        
        # Blank table cells check
        blank_cells = 0
        for row in self.table:
            for cell in row:
                if cell == "-":
                    blank_cells += 1
        if blank_cells == 0:
            self.taking_move = False
            self._message()


if __name__ == '__main__':
    g = TicTacToe(window_size[0])
    g.main()