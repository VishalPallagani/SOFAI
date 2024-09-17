import sys
import inspect
from .utils.logger import Logger
from .utils.visualizer import Visualizer
from .metacognition.metacognition import Metacognition
from .tasks.oddeven_task import OddEvenTask

class SOFAI:
    def __init__(self):
        self.system1 = None
        self.system2 = None
        self.task = None
        self.logger = Logger()
        self.confidence_threshold = 0.7  # Default confidence threshold
        self.probability_repeat = 0.5  # Default probability of repeating tasks
        self.iterations = 100  # Default number of iterations

    def _dynamic_solver_import(self, solver_id):
        """
        Dynamically imports the solver class based on the provided solver ID (class name).
        Assumes that the solvers are defined in `solvers` package and named accordingly.
        """
        # Get all classes in the solvers module dynamically
        solvers_module = sys.modules.get('solvers.system1_solver') or sys.modules.get('solvers.system2_solver')
        all_classes = dict(inspect.getmembers(solvers_module, inspect.isclass))

        if solver_id in all_classes:
            return all_classes[solver_id]()  # Dynamically instantiate the class
        else:
            raise ValueError(f"Solver ID '{solver_id}' not found.")

    def set_system1(self, solver_id):
        """Dynamically set the System 1 solver based on the solver ID."""
        self.system1 = self._dynamic_solver_import(solver_id)

    def set_system2(self, solver_id):
        """Dynamically set the System 2 solver based on the solver ID."""
        self.system2 = self._dynamic_solver_import(solver_id)

    def set_task(self, task_id="OddEvenTaskGenerator"):
        """Set the task generator (currently static with odd-even task)"""
        if task_id == "OddEvenTaskGenerator":
            self.task = OddEvenTask.generate_task
        else:
            raise ValueError(f"Task ID '{task_id}' not recognized.")

    def set_confidence_threshold(self, threshold):
        self.confidence_threshold = threshold

    def set_iterations(self, iterations):
        self.iterations = iterations

    def solve(self):
        """Run the metacognition-based solver on the task, logging and printing everything."""
        if not self.system1 or not self.system2 or not self.task:
            raise ValueError("System 1 solver, System 2 solver, and task must be set before solving.")

        # Instantiate Metacognition with confidence threshold
        metacognition = Metacognition(self.system1, self.system2, self.probability_repeat, self.confidence_threshold)

        # Run the simulation for the defined number of iterations
        for i in range(self.iterations):
            task_instance = metacognition.repeat_or_new_task(self.task)
            solution, time_taken, system_used = metacognition.solve_task(task_instance)

            # Log the task, system used, and time taken
            self.logger.log_task(task_instance, system_used, time_taken)

        # Visualize and print the results
        Visualizer.plot_results(self.iterations, self.logger)

# Create a global instance of the SOFAI class for easy access
sofai = SOFAI()
