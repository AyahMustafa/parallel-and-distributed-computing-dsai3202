# parallel-and-distributed-computing-dsai3202

Observations on Process Synchronization with Semaphores

1. What Happens if More Processes Try to Access the Pool Than There Are Available Connections?
If more processes try to access the pool than there are connections, the extra processes will be blocked and will wait until a connection is released. This can lead to delays as they queue up for access.
2. How Does the Semaphore Prevent Race Conditions and Ensure Safe Access to the Connections?
The semaphore controls access by allowing only a limited number of processes to use the connections at the same time. When a process calls acquire(), it checks the semaphore count. If it's zero, the process waits. This prevents race conditions by ensuring that only one process can modify the shared resource at a time, keeping everything safe and orderly.
