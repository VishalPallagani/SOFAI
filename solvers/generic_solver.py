class GenericSolver:
    def __init__(self, solver_id):
        self.solver_id = solver_id  # Each solver will have a unique ID or name

    def solve(self, task):
        """
        The base solve method that all solvers must implement.
        """
        raise NotImplementedError("Each solver must implement the 'solve' method.")
