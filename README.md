Question 1: How the Automated Maze Explorer Works
Algorithm Used:
The explorer uses the right-hand rule, which means it keeps its right hand on the wall while navigating the maze.

Handling Loops:
It tracks its last three moves to avoid getting stuck in loops. If it detects repeated moves, it backtracks.

Backtracking Strategy:
The explorer remembers the cells it has visited, allowing it to backtrack when it hits a dead end.

Statistics Provided:
At the end of the run, it shows:

Total time taken (0.00 seconds)
Total moves made (154 for random maze, 1279 for static maze)
Number of backtracks (0)
Average moves per second (varies by run)
Question 2: Running Multiple Explorers Simultaneously
Parallel Execution:
I modified the program to run multiple explorers at once using multiprocessing. Each explorer works independently on the same maze.

Collecting Statistics:
I gathered stats for each explorer, including total moves and time taken, and created a summary table to compare their performance.

Question 3: Performance Analysis of Explorers
Running Explorers:
I ran four explorers on the static maze, and they all made 1279 moves with no backtracking, showing the right-hand rule was effective.

Observations:
The random maze runs varied in moves, indicating different paths were taken, while the static maze was consistent.

Question 4: Enhancements to the Maze Explorer
Identifying Limitations:
The right-hand rule can lead to longer paths and isn’t always optimal.

Proposed Improvements:
I suggest implementing Breadth-First Search (BFS) for finding the shortest path and adding a heuristic to prioritize paths closer to the exit.

Implementation:
I’ll modify the explorer.py file to include these enhancements and document the changes.

Question 5: Performance Comparison of Enhanced Explorer
Running Both Versions:
After implementing the enhancements, I’ll run both the original and enhanced explorers on the static maze.

Metrics Comparison:
I’ll compare total moves and time taken for both versions.

Visualizations:
I plan to create charts to show the performance differences.

Trade-offs Discussion:
I’ll discuss any trade-offs from the enhancements, like increased complexity or resource usage.
