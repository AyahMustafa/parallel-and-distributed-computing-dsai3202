# src/parallel_runner.py

import multiprocessing
from .maze import create_maze
from .explorer import Explorer

def explorer_task(maze_type, width, height):
    """Task to run one explorer."""
    maze = create_maze(width, height, maze_type)
    explorer = Explorer(maze)
    explorer.solve()

def run_parallel_explorers(num_explorers, maze_type, width, height):
    """Run multiple explorers in parallel."""
    with multiprocessing.Pool(processes=num_explorers) as pool:
        # Map
        pool.starmap(explorer_task, [(maze_type, width, height)] * num_explorers)

    print(f"Ran {num_explorers} explorers in parallel.")
