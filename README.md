# DSAI3202
# Work Environment for the Parallel and Distributed Computing Course

## **Question 1: Overview of the Automated Maze Explorer**

- The maze explorer in this project operates using a fundamental technique known as the **right-hand rule**. This approach mimics a person navigating through a maze while keeping their right hand against the wall. At each junction, the explorer assesses its options to turn right, move forward, turn left, or backtrack, in that specific order, to successfully locate the exit.

- To avoid looping back on itself, the explorer keeps track of its last three movements. If it identifies a repetitive pattern (for instance, making three consecutive right turns), it assumes it is trapped in a loop and initiates backtracking.

- The backtracking process relies on a history of visited paths, enabling the explorer to remember previously traversed cells and retrace its steps when necessary.

- At the end of each exploration, the explorer provides several important statistics:
  - Total duration of the exploration: **0.0025 seconds**
  - Total number of moves made: **1279 moves**
  - Count of backtrack operations: **0 backtracks**
  - Average speed of movement: *633055.80**

- For example, in one of my trials, the explorer successfully navigated the static maze in **1279 moves**, did not require any backtracking, and completed the task in **0.0025 seconds**.

- Overall, this algorithm is straightforward yet effective for navigating the maze.

---

## **Question 2: Executing Multiple Explorers Concurrently**

- To improve the exploration process, I developed a function that allows a single maze explorer to operate on the static maze and return results such as moves, time, and backtracks. I then utilized Python’s `multiprocessing` module to run **four explorers** simultaneously.

- Each explorer independently tackled the same static maze, achieving the solution in **1279 moves** with **no backtracking**. The slight variations in time taken, measured in milliseconds, highlight the algorithm's consistency and efficiency.

- Here’s a summary of the results:

| Explorer | Moves | Backtracks | Time (s) |
|---|---|---|---|
| 1 | 494 | 0 | 0.0021 |
| 2 | 563 | 0 | 0.0023 |
| 3 | 92 | 0 | 0.002 |
| 4 | 1279 | 0 | 0.0022 |

The differences in timing can be attributed to the scheduling of tasks by the multiprocessing module, but all explorers demonstrated similar effectiveness in pathfinding.

---

## **Question 3: Performance Evaluation of Explorers**

I executed four explorers in parallel on the same static maze, collecting data on their performance regarding moves, time taken, and backtracking.

All explorers completed the maze in exactly 1279 moves, which is expected given they utilized the same algorithm. Notably, none required backtracking, indicating the effectiveness of the right-hand rule.

Minor differences in time taken were observed, likely due to the nature of multiprocessing, where each process is scheduled differently by the operating system.

To visualize the comparison, I created bar charts illustrating the number of moves, backtracks, and time for each explorer. Since all backtracks were zero, I labeled the bars accordingly.

![Performance Visualization](image)

Overall, the results indicate that the explorer is consistent and performs well on the static maze, but further testing on more complex mazes is warranted.

**Summary Table – Explorer Performance (Static Maze)**

| Explorer | Moves | Backtracks | Time (s) |
|---|---|---|---|
| 1 | 1279 | 0 | 0.0023 |
| 2 | 1279 | 0 | 0.0029 |
| 3 | 1279 | 0 | 0.0042 |
| 4 | 1279 | 0 | 0.0021 |

All explorers completed the maze with identical path lengths and zero backtracking. Timing differences are due to parallel processing overhead.

---

## **Question 4: Upgrading the Maze Explorer**

The initial maze explorer utilized the right-hand rule, which, while effective, lacks intelligence regarding the goal's location. This can lead to unnecessarily long routes even when the exit is nearby.

To address this limitation, I introduced a new method in the Explorer class called `bfs_solve()` that implements Breadth-First Search (BFS). This algorithm systematically explores all potential paths and guarantees the shortest path in a grid-like maze.

With this enhancement:

- The explorer becomes goal-aware, knowing the exit's location.
- It avoids unnecessary turns and loops.
- It finds the shortest path without backtracking.
- It operates more efficiently than the original method.

Testing on the static maze revealed a significant improvement, with the BFS explorer solving the maze in just 128 moves, compared to 1279 moves for the right-hand rule.

This enhancement greatly increases the explorer's effectiveness.

---

## **Question 5: Comparing the Enhanced Explorer (BFS) to the Original**

To evaluate performance, I ran both the original right-hand rule explorer and the new BFS-based explorer on the same static maze.

Here are the results:

| Algorithm | Moves | Backtracks | Time (s) |
|---|---|---|---|
| Right-Hand Rule | 1279 | 0 | ~0.0025 |
| BFS | 128 | 0 | 0.0013 |

The results clearly show that BFS found a significantly shorter path (128 moves vs 1279 moves). Both algorithms completed the maze without backtracking, but BFS was more efficient due to its ability to calculate the shortest path.

**Trade-offs**

The right-hand rule is straightforward and does not require prior knowledge of the goal, making it useful in unfamiliar environments.

Conversely, BFS is goal-aware and optimal but necessitates access to the entire maze structure beforehand.

In this case, BFS is the superior choice, being faster, more intelligent, and yielding a shorter, more direct route to the exit.
