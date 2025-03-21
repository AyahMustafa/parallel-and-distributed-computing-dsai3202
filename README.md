# parallel-and-distributed-computing-dsai3202
*Explanation of the Program in genetic_algorithm_trial.py:

The genetic_algorithm_trial.py script implements a genetic algorithm to optimize delivery routes in a city. The main components of the script are as follows:

Imports: The script imports necessary libraries, including NumPy and Pandas, as well as functions from the genetic_algorithms_functions.py file.

Load Distance Matrix: It loads the distance matrix from city_distances.csv, which contains the distances between delivery nodes.

Parameters: Several parameters are defined, including:

population_size: The number of routes in the population.
num_tournaments: The number of tournaments for selection.
mutation_rate: The probability of mutation.
num_generations: The number of generations to run the algorithm.
infeasible_penalty: A penalty for infeasible routes.
stagnation_limit: The number of generations without improvement before regenerating the population.
Generate Initial Population: An initial population of unique routes is generated, starting from node 0.

Main Genetic Algorithm Loop: The loop runs for a specified number of generations, performing the following steps:

Evaluate the fitness of each route.
Check for stagnation and regenerate the population if necessary.
Select individuals using tournament selection.
Perform crossover and mutation to create offspring.
Replace the worst individuals in the population with the new offspring.
Ensure the population remains unique.
Output: After the loop, the best solution found and its total distance are printed.

Running and Timing the Execution:
To run and time the execution of the script, I used the following command in the terminal:

"time python3 genetic_algorithm_trial.py"
This command provided the execution time, including user time, system time, and elapsed real time.
Which were" 
real    0m8.780s
user    0m8.661s
sys     0m0.116s"

*Parts to be Distributed and Parallelized:
The main parts of the algorithm that can be parallelized include:

Fitness Evaluation: Each route's fitness can be calculated independently, making it suitable for parallel execution.
Selection: The tournament selection process can be run in parallel, as each tournament is independent.
Crossover and Mutation: The operations for generating offspring can also be performed in parallel.
Parallelization Implementation:
I used the mpi4py library to parallelize the fitness evaluation and selection processes. The script was modified to distribute the population across multiple processes, allowing each process to evaluate the fitness of its subset of routes concurrently.

*Enhance the Algorithm
Distributing the Algorithm Over Multiple Machines:
I set up the algorithm to run across two or more machines using MPI. This involved ensuring that the machines could communicate and that the necessary libraries were installed on each machine. I executed the parallel code using:

mpirun -np 4 -host machine1,machine2 python3 genetic_algorithm_trial.py
Proposed Improvements:
I proposed several enhancements to the algorithm, including:

Adaptive Mutation Rate: Implementing an adaptive mutation rate that changes based on the generation or fitness improvement.
Elitism: Retaining a certain number of the best individuals in each generation to ensure that the best solutions are not lost.
Diverse Selection Methods: Experimenting with different selection methods (e.g., roulette wheel selection) to see which yields better results.
Recomputing Performance Metrics:
After implementing the enhancements, I ran the improved algorithm and measured the performance metrics again. I compared the execution time and the quality of solutions (total distance) before and after the enhancements.
real    0m16.583s
user    0m16.150s
sys     0m0.432s

*Large Scale Problem
Running the Program Using the Extended City Map:
I executed the program using the extended city map city_distances_extended.csv to test the algorithm's performance on a larger dataset. The program ran successfully within a feasible time frame.

Adding More Cars to the Problem:
To add more cars to the problem, I would modify the genetic algorithm to handle multiple routes simultaneously. Each car could be represented as a separate individual in the population, and the fitness function would need to be adjusted to account for the total distance traveled by all cars. Additionally, I would ensure that each delivery node is visited exactly once across all routes, which may require additional constraints in the fitness evaluation.



