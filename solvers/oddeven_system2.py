import time
from solvers.system2_solver import System2Solver

class LogicBasedOddEvenSolver(System2Solver):
    def __init__(self, solver_id="Logic-Based Odd-Even Solver"):
        super().__init__(solver_id)

    def solve(self, task):
        start_time = time.time()
        solution = "even" if task % 2 == 0 else "odd"
        elapsed_time = time.time() - start_time
        return solution, elapsed_time
