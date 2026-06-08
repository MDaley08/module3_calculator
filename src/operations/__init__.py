
from typing import Union
Number = Union[int,float]

def _validate_num(a: Number) -> float:
    """
    Check if input is a valid Number

    Args:
        a: The input value of any type to check.
    Returns:
        float if inputted value is of a valid type
    """
    if not (isinstance(a,Number)) or isinstance(a,bool):
        raise TypeError(f"{a} is an invalid input")
    return float(a)


def _verify_inputs(a: Number, b:Number) -> tuple[float,float]:
    """
    Check if inputs are valid

    Args:
        a: first number to check if it has a valid value
        b: second number to check it has a valid value
    Returns:
        returns numbers if they are valid inputs
    """
    
    return _validate_num(a), _validate_num(b)
    


class operations:
    
    @staticmethod
    def additon(a: Number,b: Number) -> float:
        """
        adds two numbers

        Args:
            a: first number to add
            b: second number to add
        Returns:
            the sum of a and b
        """
        val_a, val_b = _verify_inputs(a,b)
        
        return val_a + val_b

    @staticmethod
    def subtraction(a: Number,b: Number) -> float:
        """
        subtracts b from a

        Args:
            a: the minuend(number being subtracted from)
            b: subtrahend(number being subtracted)
        Returns:
            the difference of b from a
        """
        val_a, val_b = cls._verify_inputs(a,b)
        
        return val_a - val_b

    @staticmethod
    def multiplication(a: Number,b: Number) -> float:
        """
        multiplies a and b

        Args:
            a: first factor to be multiplied
            b: second factor to be multiplied
        Returns:
            the product of a and b
        """
        val_a, val_b = _verify_inputs(a,b)

        return val_a * val_b

    @staticmethod
    def division(a: Number,b: Number) -> float:

        val_a, val_b = _verify_inputs(a,b)

        if b == 0:
            raise ValueError("cannot divide by 0")
        
        return val_a / val_b
