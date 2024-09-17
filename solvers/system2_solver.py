from solvers.generic_solver import GenericSolver
import time

class System2Solver(GenericSolver):
    def __init__(self, solver_id):
        super().__init__(solver_id)

    def solve(self, task):
        raise NotImplementedError("Each System 2 solver must implement the 'solve' method.")
