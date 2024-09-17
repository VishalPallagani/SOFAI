from solvers.generic_solver import GenericSolver

class System1Solver(GenericSolver):
    def __init__(self, solver_id):
        super().__init__(solver_id)

    def solve(self, task):
        """
        Each System 1 solver must implement its specific solve method.
        """
        raise NotImplementedError("Each System 1 solver must implement the 'solve' method.")

    def confidence_estimation(self, task):
        """
        Each System 1 solver must implement its own confidence estimation method.
        """
        raise NotImplementedError("Each System 1 solver must implement the 'confidence_estimation' method.")
