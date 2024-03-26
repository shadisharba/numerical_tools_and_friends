import time
import logging
from functools import wraps
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def sample_decorator(func):
    @wraps(func)  # This is used to preserve the metadata of the original function
    def wrapper(*args, **kwargs):
        print('do something before function execution')
        result = func(*args, **kwargs)
        print('do something after function execution')
        return result

    return wrapper


def debug_decorator(debug_mode):
    """Example: Passing arguments to a decorator"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if debug_mode:
                print(f"Function called: {func.__name__}")
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def timer(func):
    """Example: Measure execution time of function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {round(end_time - start_time, 4)}")
        return result

    return wrapper


def logging(func):
    """Example: Logging with decorator"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        log_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"{log_time}: {func.__name__} called")
        result = func(*args, **kwargs)
        return result

    return wrapper


@sample_decorator
def func_add(a, b):
    return a + b


print(func_add.__name__)
func_add(1, 2)


@debug_decorator(debug_mode=True)
def func_add(a, b):
    return a + b


func_add(1, 2)


@timer
def func_add(a, b):
    time.sleep(1)
    return a + b


func_add(1, 2)


@logging
def func_add(a, b):
    return a + b


func_add(1, 2)


def singleton(cls):
    """Example: Create singleton class with decorator.
    singleton is a type of creational design pattern that restricts a class to have only one instance. This is useful in cases where there is a limit on concurrent access to a shared resource, or a global point of access for a resource, such as imposing a limit on concurrent access to a database or a single point of access for a database.
    """
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class SampleClass:
    def __init__(self):
        pass


singleton_class = SampleClass()
singleton_class2 = SampleClass()
print(singleton_class == singleton_class2)
