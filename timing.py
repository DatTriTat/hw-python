import time
def calculate_time(func):
    """
    Calculate the time in seconds to run the function

    Examples
    --------
    def func():
        time.sleep(2)
    >>> calculate_time(func)
    2.0009217262268066
    """
    def wrapper():
        current = time.time()
        func()
        end = time.time()
        print("Total time ",end - current)
    return wrapper
