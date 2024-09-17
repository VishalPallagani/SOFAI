import random
from .task_generator import Task

class OddEvenTask(Task):
    """
    A task for generating random numbers and determining whether they are odd or even.
    Inherits from the generic Task class.
    """
    
    def __init__(self):
        super().__init__(task_name="Odd-Even Task")
    
    def generate_task(self):
        """
        Generates a random integer between 1 and 100 for the odd-even task.
        """
        return random.randint(1, 100)

    def validate_task(self, task):
        """
        Validates whether the task is correctly structured for the odd-even task.
        In this case, just checks if the task is an integer.
        """
        if isinstance(task, int):
            return True
        return False
