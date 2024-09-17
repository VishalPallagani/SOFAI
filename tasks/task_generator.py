class Task:
    """
    A generic task base class that any user can extend to define specific tasks.
    """

    def __init__(self, task_name):
        self.task_name = task_name

    def generate_task(self):
        """
        Abstract method to generate a task. Must be implemented by specific task classes.
        """
        raise NotImplementedError("Each specific task must implement its own generate_task method.")

    def validate_task(self, task):
        """
        Abstract method to validate the task. Must be implemented by specific task classes.
        """
        raise NotImplementedError("Each specific task must implement its own validate_task method.")
