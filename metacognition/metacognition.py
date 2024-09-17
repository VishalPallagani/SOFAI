import random

class Metacognition:
    def __init__(self, system1_solver, system2_solver, probability_repeat, confidence_threshold=0.7):
        """
        Initialize the Metacognition module with System 1 and System 2 solvers.

        Parameters:
        - system1_solver: The System 1 solver object
        - system2_solver: The System 2 solver object
        - probability_repeat: Probability of repeating tasks
        - confidence_threshold: The confidence threshold for System 1. If System 1's confidence
                                exceeds this threshold, System 1's solution is returned.
        """
        self.system1 = system1_solver
        self.system2 = system2_solver
        self.probability_repeat = probability_repeat
        self.confidence_threshold = confidence_threshold
        self.repeat_task_pool = []

    def solve_task(self, task):
        # Step 1: System 1 tries to solve the task
        solution, time_taken, from_case_base = self.system1.solve(task)

        # Get confidence estimation from System 1
        confidence = self.system1.confidence_estimation(task)

        # Step 2: If confidence exceeds the threshold, return System 1's solution
        if confidence >= self.confidence_threshold:
            return solution, time_taken, "System 1"

        # Step 3: Otherwise, use System 2 to solve the task
        solution, time_taken = self.system2.solve(task)
        self.system1.update_case_base(task, solution)  # Optionally update System 1 with System 2's solution
        return solution, time_taken, "System 2"

    def repeat_or_new_task(self, task_generator):
        """
        Generate a task based on probability of repetition. Either repeat an old task or generate a new one.

        Parameters:
        - task_generator: A function to generate new tasks
        """
        if random.random() < self.probability_repeat and self.repeat_task_pool:
            return random.choice(self.repeat_task_pool)
        else:
            task = task_generator()
            self.repeat_task_pool.append(task)
            return task
