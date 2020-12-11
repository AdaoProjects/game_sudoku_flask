
class Sudoku_solver:
    list_of_empty_positions=[[],[]]
    list_of_possibilites=[[]]
    def create_list_of_empty_positions(self,sudoku):
        self.list_of_empty_positions=[[],[]]
        for i in range(0,9):
            for j in range(0,9):
                if sudoku[i][j]==0:
                    self.list_of_empty_positions[0].append(i)
                    self.list_of_empty_positions[1].append(j)
    def is_possible_in_row(self,row,num,sudoku):
        is_possible=True
        for i in range(0,9):
            if sudoku[row][i]==num:
                is_possible=False
        return is_possible
    def is_possible_in_column(self,column,num,sudoku):
        is_possible=True
        for i in range(0,9):
            if sudoku[i][column]==num:
                is_possible=False
        return is_possible
    def is_possible_Box(self,row,column,num,sudoku):
        is_possible=True
        for i in range(1,4):
            for j in range(1,4):
                if row/3<i and row/3>i-1 and column/3<j and column/3>j-1:
                    for t in range(0,3):
                        for r in range(0,3):
                            if sudoku[(i-1)*3+t][(j-1)*3+r]==num:
                                is_possible=False
        return is_possible
    def find_possibilites_to_empty(self,sudoku):
        self.list_of_possibilites=[[]]
        for j in range (0, len(self.list_of_empty_positions[0])):
            self.list_of_possibilites.append([])
            for i in range(1,10):
                if self.is_possible_in_row(self.list_of_empty_positions[0][j],i,sudoku) and self.is_possible_in_column(self.list_of_empty_positions[1][j],i,sudoku) and self.is_possible_Box(self.list_of_empty_positions[0][j],self.list_of_empty_positions[1][j],i,sudoku):
                    self.list_of_possibilites[j].append(i)
    def fill_unique_possibilite(self,sudoku):
        for i in range(0,82):
            self.create_list_of_empty_positions(sudoku)
            self.find_possibilites_to_empty(sudoku)
            for j in range (0, len(self.list_of_empty_positions[0])):
                if len(self.list_of_possibilites[j])==1:
                    sudoku[self.list_of_empty_positions[0][j]][self.list_of_empty_positions[1][j]]=self.list_of_possibilites[j][0]
    def return_solution(self,sudoku):
        self.fill_unique_possibilite(sudoku)
        return sudoku

