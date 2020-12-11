from flask import Flask,render_template
from puzzle_generator import Sudoku_generator
from puzzle_solver import Sudoku_solver

app=Flask(__name__)

generator=Sudoku_generator()
solver=Sudoku_solver()

@app.route('/sudoku_game')
def game_page():
    generator.create_new_sudoku()
    sudoku =generator.return_generated_puzzle()
    return render_template('game_page.html', sudoku=sudoku)

@app.route('/sudoku_game/solution')
def show_solution():
    sudoku=generator.return_generated_puzzle()
    sudoku_solution=solver.return_solution(sudoku)
    return render_template('game_page.html', sudoku=sudoku_solution)

if __name__=="__main__":
    app.run(debug=True)