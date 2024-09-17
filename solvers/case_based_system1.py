import time
from solvers.system1_solver import System1Solver

class CaseBasedSolver(System1Solver):
    def __init__(self, solver_id="case-based"):
        super().__init__(solver_id)
        self.case_base = {}

    def solve(self, task):
        # Check if the task is in the case base
        start_time = time.time()
        if task in self.case_base:
            elapsed_time = time.time() - start_time
            return self.case_base[task], elapsed_time, True
        return None, time.time() - start_time, False

    def update_case_base(self, task, solution):
        self.case_base[task] = solution

    def confidence_estimation(self, task):
        # Return high confidence if task is in case base
        if task in self.case_base:
            return 1
        return 0

# have case size, if case size limit is reached throw away cases - case policy
# keep track of frequency usage of cases