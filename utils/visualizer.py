import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_results(iterations, logger):
        """
        Plots the results of the simulation, showing which system (System 1 or System 2) was used for each task.
        """
        x = list(range(1, iterations + 1))
        y = [1 if sys == "System 1" else 2 for sys in logger.system_usage]

        plt.figure(figsize=(10, 5))
        plt.scatter(x, y, c=['green' if sys == "System 1" else 'blue' for sys in logger.system_usage], alpha=0.6, s=10)
        plt.yticks([1, 2], ["System 1", "System 2"])
        plt.xlabel('Iteration')
        plt.ylabel('System Used')
        plt.ylim(0.5, 2.5)
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.title('System Usage over Iterations')
        plt.show()

        # Displaying metrics in the output
        print(f"\nSimulation Results:")
        print(f"System 1 Solved: {logger.metrics['system1_solved_count']} tasks")
        print(f"System 2 Solved: {logger.metrics['system2_solved_count']} tasks")
        print(f"Average Time for System 1: {logger.metrics['avg_time_system1']:.2f} seconds")
        print(f"Average Time for System 2: {logger.metrics['avg_time_system2']:.2f} seconds")
