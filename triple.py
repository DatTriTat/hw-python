def tripler(func):
    """
    Call the function that this function is used on three times.

    Parameters
    ----------
    func : fuction
       This function is called to use

    Examples
    --------
    def func():
        print('Hello, World!')
    >>> my_decorator(func)
    Hello, World!
    Hello, World!
    Hello, World!
    """
    def wrapper():
        func()
        func()
        func()
    return wrapper

