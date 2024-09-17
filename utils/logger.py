class Logger:
    def __init__(self):
        self.task_history = []
        self.system_usage = []
        self.metrics = {}

    def log_task(self, task, system_used, time_taken):
        """
        Logs the task, which system was used (System 1 or System 2), and the time taken to solve it.
        """
        self.task_history.append((task, system_used, time_taken))
        self.system_usage.append(system_used)

    def log_metrics(self, system1_time_taken, system2_time_taken, system1_solved, system2_solved, avg_time_s1, avg_time_s2):
        """
        Logs the overall metrics after simulation is completed.
        """
        self.metrics = {
            'system1_time_taken': system1_time_taken,
            'system2_time_taken': system2_time_taken,
            'system1_solved_count': system1_solved,
            'system2_solved_count': system2_solved,
            'avg_time_system1': avg_time_s1,
            'avg_time_system2': avg_time_s2
        }

    def save_logs(self, filename="logs.txt"):
        """
        Saves the log information to a file (optional).
        """
        with open(filename, 'w') as f:
            f.write(f"Task History: {self.task_history}\n")
            f.write(f"System Usage: {self.system_usage}\n")
            f.write(f"Metrics: {self.metrics}\n")
