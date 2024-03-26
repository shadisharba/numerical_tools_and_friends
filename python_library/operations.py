# Documenting a function in sphinx style using VSCode docstring generator plugin
def add( a, b ):
    """
    This function computes the sum of the two arguments.

    :param num1: first argument
    :type num1: float
    :param num2: second argument
    :type num2: float
    :return: sum of the two arguments 
    :rtype: int or float

    .. note:: This function can accept :class:`int` parameters too.

    Example::
    
        result = add(a,b)
    """
    assert type(a) == type(b)
    return a + b

# Division function
def divide(divident, divisor):
    """
    This function computes the division of divident by the divisor.
    `Reference. <https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-i-5/>`_

    :param divident: divident number
    :type divident: float
    :param divisor: divisor number
    :type divisor: float
    :return: division result
    :rtype: float
    :raises ZeroDivisionError: when divisor = 0

    .. note:: This function can accept :class:`int` parameters too.

    .. warning:: ``divisor=0`` will cause :exc:`ZeroDivisionError` exception!

    Example::

        result = divide(a, b)
    """
    return divident / divisor

