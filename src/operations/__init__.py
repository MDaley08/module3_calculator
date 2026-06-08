
class operations:
    
    @ staticmethod
    def _validate_num(a) -> float:
        """
        Check if input is a valid Number

        Args:
            a: The input value of any type to check.
        Returns:
            None if value is not a valid number, returns the number itself if it is
        """
        if not (isinstance(a,(float,int))) or isinstance(a,bool):
            raise TypeError(f"{a} is an invalid input")
        return float(a)
    
    @ staticmethod
    def _verify_inputs(a,b):
        """
        Check if inputs are valid

        Args:
            a: first number to check if it has a valid value
            b: second number to check it has a valid value
        Returns:
            None if either value is not a valid input, returns the numbers
        """
        val_a = operations._validate_num(a)
        val_b = operations._validate_num(b)

        if val_a == None and val_b == None:
            return None
        
        return val_a, val_b
        

    
    @staticmethod
    def additon(a,b):
        """
        adds two numbers

        Args:
            a: first number to add
            b: second number to add
        Returns:
            the sum of a and b
        """
        val_a, val_b = operations._verify_inputs(a,b)
        
        return val_a + val_b

    @staticmethod
    def subtraction(a,b):
        """
        subtracts b from a

        Args:
            a: the minuend(number being subtracted from)
            b: subtrahend(number being subtracted)
        Returns:
            the difference of b from a
        """
        val_a, val_b = operations._verify_inputs(a,b)
        
        return val_a - val_b

    @staticmethod
    def multiplication(a,b):
        """
        multiplies a and b

        Args:
            a: first factor to be multiplied
            b: second factor to be multiplied
        Returns:
            the product of a and b
        """
        val_a, val_b = operations._verify_inputs(a,b)

        return val_a * val_b

    @staticmethod
    def division(a,b):

        val_a, val_b = operations._verify_inputs(a,b)

        if b == 0:
            raise ValueError("cannot divide by 0")
        
        return val_a / val_b
