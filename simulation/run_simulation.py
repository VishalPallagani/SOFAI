from utils.logger import Logger
from utils.visualizer import Visualizer
from metacognition.metacognition import Metacognition

def run_simulation(system1_solver, system2_solver, task_generator, iterations, probability_repeat, confidence_threshold=0.7):
    """
    Run a simulation of task solving using Metacognition to decide between System 1 and System 2.

    Parameters:
    - system1_solver: A System 1 solver object
    - system2_solver: A System 2 solver object
    - task_generator: A task generator function (for generating new tasks)
    - iterations: Number of iterations to run the simulation
    - probability_repeat: Probability that a task will be repeated
    - confidence_threshold: Confidence threshold for deciding when to use System 1's solution
    """
    # Initialize Metacognition with confidence threshold
    metacognition = Metacognition(system1_solver, system2_solver, probability_repeat, confidence_threshold)
    logger = Logger()

    # Initialize counters and timers
    system1_time_taken = 0
    system2_time_taken = 0
    system1_solved_count = 0
    system2_solved_count = 0

    # Iterate over the number of simulations
    for i in range(iterations):
        # Generate a task by calling task_generator()
        task = metacognition.repeat_or_new_task(task_generator)
        solution, time_taken, system_used = metacognition.solve_task(task)

        # Log the task and which system was used
        logger.log_task(task, system_used, time_taken)

        # Update the time and count based on the system used
        if system_used == "System 1":
            system1_time_taken += time_taken
            system1_solved_count += 1
        else:
            system2_time_taken += time_taken
            system2_solved_count += 1

    # Calculate average time taken by each system
    avg_time_system1 = system1_time_taken / system1_solved_count if system1_solved_count > 0 else 0
    avg_time_system2 = system2_time_taken / system2_solved_count if system2_solved_count > 0 else 0

    # Log the final metrics
    logger.log_metrics(system1_time_taken, system2_time_taken, system1_solved_count, system2_solved_count, avg_time_system1, avg_time_system2)

    # Use visualizer to display the results
    Visualizer.plot_results(iterations, logger)
