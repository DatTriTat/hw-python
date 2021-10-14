def calculator(number1, number2, operator):
    """
    Calculate function, returns the the result of the operation.

    Parameters
    ----------
    number1 : float
       The first number.

    number2 : float
        The second number.

    operator : String
        The operator

    Returns
    -------
    float
        The result of the operation.

    False
        If the operation is invalid.

    Examples
    --------
    >>> calculator(2, 2, '+')
    4
    >>> calculator(8, 4, '/')
    2
    >>> calculator(10, 2, '**')
    100
    >>> calculator(5, 2, 'a')
    False
    """
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '**':
        return number1 ** number2
    elif operator == '/' and number2 != 0:
        return number1 / number2
    elif operator == '//' and number2 != 0:
        return number1 // number2
    else: 
        return False

def parse_input():
    """
    Take input from the user and call the calculator function.

    Examples
    --------
    >>> parse_input()
    Enter equation: 10 + 11
    21.0
    >>> parse_input()
    Enter equation: 12 * 4.2
    50.400000000000006
    >>> parse_input()
    Enter equation: 10 ** 2
    100.0
    """
    equation = input('Enter equation: ')
    list = equation.split()
    num1 = float(list[0])
    operator = list[1]
    num2 = float(list[2])
    result = calculator(num1, num2, operator)
    print(f'The result: {result}')
