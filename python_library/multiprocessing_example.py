import multiprocessing
import os
import time


def task_sleep(sleep_duration, task_number):
    time.sleep(sleep_duration)
    print(f"Task {task_number} done (slept for {sleep_duration}s)! "
          f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    time_start = time.time()

    # Create process
    p1 = multiprocessing.Process(target=task_sleep, args=(2, 1))
    p2 = multiprocessing.Process(target=task_sleep, args=(2, 2))

    # Start task execution
    p1.start()
    p2.start()

    # Wait for process to complete execution
    p1.join()
    p2.join()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")

# The pool method is used to break a function into multiple small parts using map or starmap, running the same function with different input arguments. Whereas the Process method is used to run different functions.


if __name__ == "__main__":
    print()
    time_start = time.time()

    # Create pool of workers
    num_cpu = multiprocessing.cpu_count() - 1
    pool = multiprocessing.Pool(processes=num_cpu)

    # Map pool of workers to process
    pool.starmap(func=task_sleep, iterable=[(2, 1)] * 10)

    # Wait until workers complete execution
    pool.close()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s\n")