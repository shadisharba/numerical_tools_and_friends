modified from: https://towardsdatascience.com/multithreading-and-multiprocessing-in-10-minutes-20d9b3c6a867
multithreading refers to the ability of a processor to execute multiple threads concurrently, where each thread runs a process. Whereas multiprocessing refers to the ability of a system to run multiple processors in parallel, where each processor can run one or more threads.

multiple threads share the same code, data, and files but run on a different register and stack. Multiprocessing multiplies a single processor — replicating the code, data, and files, which incurs more overhead.

Multithreading is useful for IO-bound processes, such as reading files from a network or database since each thread can run the IO-bound process concurrently. Multiprocessing is useful for CPU-bound processes, such as computationally heavy tasks since it will benefit from having multiple processors; similar to how multicore computers work faster than computers with a single core.

Note: There is a difference between concurrency and parallelism. Parallelism allows multiple tasks to execute at the same time, whereas concurrency allows multiple tasks to execute one at a time in an interleaving manner.

Note: Due to Python Global Interpreter Lock (GIL), only one thread can be executed at a time. Therefore, multithreading only achieves concurrency and not parallelism for IO-bound processes. On the other hand, multiprocessing achieves parallelism.
