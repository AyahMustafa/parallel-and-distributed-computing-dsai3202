from mpi4py import MPI
import numpy as np
import time

def square(n):
    """Function to compute squares of numbers from 1 to n"""
    return np.array([i**2 for i in range(1, n+1)])

def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Parameters
    n = 10000000  # Modify as needed, for example, up to 1e8 as requested
    chunk_size = n // size

    # Each process computes part of the result
    start = rank * chunk_size + 1
    end = (rank + 1) * chunk_size if rank != size - 1 else n + 1
    partial_result = square(end - start + 1)

    # Gather all partial results at root process
    all_results = comm.gather(partial_result, root=0)

    if rank == 0:
        # Combine all results into a final array
        final_result = np.concatenate(all_results)
        print(f"Size of final array: {final_result.size}")
        print(f"Last square: {final_result[-1]}")
        print(f"Time taken: {time.time() - start_time} seconds")

if __name__ == "__main__":
    start_time = time.time()  # Start timing the execution
    main()
