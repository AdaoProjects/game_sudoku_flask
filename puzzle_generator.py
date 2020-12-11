from puzzle_solver import Sudoku_solver
import random
class Sudoku_generator():
    original_sudoku=[[0,0,0,6,0,0,1,0,7],[6,8,0,9,5,1,3,0,0],[0,0,3,0,0,2,5,6,8],[0,4,0,8,1,0,0,2,0],[0,0,0,0,0,0,8,5,0],[0,9,0,0,6,5,0,7,3],[4,0,9,0,0,3,0,8,5],[1,6,2,0,0,9,0,3,0],[5,0,0,7,0,6,0,0,0]]
    sudoku=[[0,0,0,6,0,0,1,0,7],[6,8,0,9,5,1,3,0,0],[0,0,3,0,0,2,5,6,8],[0,4,0,8,1,0,0,2,0],[0,0,0,0,0,0,8,5,0],[0,9,0,0,6,5,0,7,3],[4,0,9,0,0,3,0,8,5],[1,6,2,0,0,9,0,3,0],[5,0,0,7,0,6,0,0,0]]
    def create_new_sudoku(self):
        self.rotate_puzzle(self.sudoku)
        self.swap_two_numbers()
    def rotate_puzzle(self,sudoku):
        x=random.randint(1,4)
        for t in range(0,x):
            for i in range(0,9):
                for j in range(0,9):
                    sudoku[i][j]=self.original_sudoku[8-j][i]
            for i in range(0,9):
                for j in range(0,9):
                    self.original_sudoku[i][j]=sudoku[i][j]
    def swap_two_numbers(self):
        num1=random.randint(1,9)
        num2=random.randint(1,9)
        while num1==num2:
            num2=random.randint(1,9)
        for i in range(0,9):
            for j in range(0,9):
                if self.original_sudoku[i][j]==num1:
                    self.sudoku[i][j]=num2
        for i in range(0,9):
            for j in range(0,9):
                if self.original_sudoku[i][j]==num2:
                    self.sudoku[i][j]=num1
        for i in range(0,9):
            for j in range(0,9):
                self.original_sudoku[i][j]=self.sudoku[i][j]
    def return_generated_puzzle(self):
        return self.sudoku