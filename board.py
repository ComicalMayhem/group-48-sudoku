import pygame
from cell import Cell
from sudoku_generator import generate_sudoku, SudokuGenerator
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        if difficulty == "easy":
            removed_cells=1
        elif difficulty == "medium":
            removed_cells=40
        elif difficulty == "hard":
            removed_cells=50
        self.board_values= generate_sudoku(9, removed_cells)
        self.cells = [
            [Cell(self.board_values[r][c], r, c, screen) for c in range(9)]
            for r in range(9)
        ]
        self.original_board = [[self.board_values[r][c] for c in range(9)] for r in range(9)]
        self.selected_cell=None
    def draw (self):
        for r  in range(9):
            for c in range(9):
                self.cells[r][c].draw()
        cell_size=self.width//9
        for i in range (10):
            if i % 3 == 0:
                line_width=3
            else:
                line_width=1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * cell_size), (self.width, i * cell_size), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, self.height), line_width)
    def select(self, row, col):
        for r in range (9):
            for c in range (9):
                self.cells[r][c].selected=False
        self.cells[row][col].selected = True
        self.selected_cell = (row, col)
    def click(self, x, y):
        if x< self.width and y<self.height:
            cell_size=self.width//9
            row=y//cell_size
            col=x//cell_size
            return (row,col)
        return None

    def clear(self):
        if self.selected_cell:
            r, c = self.selected_cell
            if self.original_board[r][c] == 0:
                self.cells[r][c].set_cell_value(0)
                self.cells[r][c].set_sketched_value(0)
                self.update_board()
    def sketch(self,value):
        if self.selected_cell:
            r,c= self.selected_cell
            if self.original_board[r][c] == 0:
                self.cells[r][c].set_sketched_value(value)
    def place_number(self, value):
        if self.selected_cell:
            r, c = self.selected_cell
            if self.original_board[r][c] == 0:
                self.cells[r][c].set_cell_value(value)
                self.update_board()
    def reset_to_original(self):
        for r in range(9):
            for c in range(9):
                if self.original_board[r][c] == 0:
                    self.cells[r][c].set_cell_value(0)
                    self.cells[r][c].set_sketched_value(0)
        self.update_board()
    def is_full(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return False
        return True
    def update_board(self):
        for r in range(9):
            for c in range(9):
                self.board_values[r][c] = self.cells[r][c].value
    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return (r, c)
        return None
    def check_board(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value != SudokuGenerator.solution[r][c]:
                    return False
        return True
