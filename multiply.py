def multiply_list(list):
    """
    Multiply all elements in a list

    Parameters
    ----------
    nums : list of int
       numbers in the list.

    Returns
    -------
    int
        The product of all numbers in the list.
    False
        If any item in the list is invalid.
    Examples
    --------
    >>> multiply_list([1, 2, 3, 7])
    42
    >>> multiply_list([3, 2, 4, 89])
    25
    >>> multiply_list([1, 2, 3, 'c'])
    False
    """
    total = 1
    for i in list:
        if type(i) == int:
            total = total * i
        else:
            return False
    return total
  
 
