# Some functions with google style python docstrings
# Using sphinx style annotations for note and example boxes.
def subtract( a, b ):
    """
    This function computes the difference between the two arguments.

    Args:
        a (float): first argument
        b (float): second argument

    Returns:
        float: difference between the two arguments

    .. note:: This function can accept :class:`int` parameters too.

    Example::
    
        result = subtract(a,b)
    """
    assert type(a) == type(b)
    return a - b

def multiply( a, b ):
    """
    This function computes the product of the two arguments.

    Args:
        a (float): first argument
        b (float): second argument

    Returns:
        float: product of the two arguments

    .. seealso:: If this note box is rendered, then it is possible to use both docstring conventions in the python files. Here, the function descriptions above were documented using the google convention and the special annotations below were written in sphinx convention. Pretty handy!
    
    .. note:: This function can accept :class:`int` parameters too.

    Example::
    
        result = multiply(a,b)
    """
    assert type(a) == type(b)
    return a * b