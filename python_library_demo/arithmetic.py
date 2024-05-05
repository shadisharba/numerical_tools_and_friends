class Arithmetic():
    """ Arithmetic class for operations on two numbers
    """
    def __init__(self, a, b):
        """ init function

        :param a: first number
        :type a: float
        :param b: second number
        :type b: float 

        .. note:: This function can accept :class:`int` parameters too.

        Example:: 

            object = Arithmetic(a=10,b=2)
        """
        self.a = a
        self.b = b

    def add(self):
        """ this method adds the two numbers of the class

        :return: sum of the two attributes of the class
        :rtype: float

        Example:: 

            result = Arithmetic.add() 
        """
        self.add = self.a + self.b
        return self.add

    def subtract(self):
        """this method subtracts the two numbers of the class

        :return: difference of the second number from first number
        :rtype: float
        
        Example:: 

            result = Arithmetic.subtract()
        """
        self.sub = self.a - self.b
        return self.sub
    
    def multiply(self):
        """ this method multiplies the two numbers of the class

        :return: product of the two attributes of the class
        :rtype: float
        
        Example:: 

            result = Arithmetic.multiply()
        """
        self.mul = self.a * self.b
        return self.mul

    def divide(self):
        """ this method divides the first number by second number
        
        :return: quotient of the division of the two attributes of the class
        :rtype: float

        .. warning:: ``b=0`` will cause :exc:`ZeroDivisionError` exception!
        
        Example:: 

            result = Arithmetic.divide()
        """
        try:
            self.div = self.a / self.b
            return self.div
        except ZeroDivisionError:
            pass