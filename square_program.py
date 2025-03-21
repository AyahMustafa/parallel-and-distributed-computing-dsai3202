from multiprocessing import Semaphore, Process, current_process
import time
import random

class ConnectionPool:
    def __init__(self, size):
        self.semaphore = Semaphore(size)
        self.connections = [f"Connection {i}" for i in range(size)]
    
    def get_connection(self):
        self.semaphore.acquire()
        connection = self.connections.pop()
        return connection

    def release_connection(self, connection):
        print(f"{current_process().name} released {connection}")
        self.connections.append(connection)
        self.semaphore.release()

def access_database(pool):
    print(f"{current_process().name} is waiting for a connection")
    connection = pool.get_connection()
    print(f"{current_process().name} acquired {connection}")
    time.sleep(random.uniform(0.5, 2))
    pool.release_connection(connection)

if __name__ == "__main__":
    pool = ConnectionPool(size=5)  #ex size 5
    processes = [Process(target=access_database, args=(pool,)) for _ in range(10)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
