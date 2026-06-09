import pytest
from src.operations import operations
from typing import Union

Number = Union[int,float]


#---------------------------------------
# Unit tests for addition method
#---------------------------------------

@pytest.mark.parametrize("a,b,expected",
                         [(1,2,3), # adding two positive ints
                          (0,0,0), # adding two zeros
                          (1,-1,0), # adding a positive and a negative int
                          (-1,-1,-2), # adding two negative ints
                          (1.5,2.5,4.0), # adding two positive floats
                          (-1.5,2.5,1.0)], #adding a positive and a negative float
                          ids=[
                              "add_two_positive_ints",
                              "add_two_zeros",
                              "add_positive_and_negative_int",
                              "add_two_negative_ints",
                              "add_two_positive_floats",
                              "add_negative_and_positive_floats"
                          ]
                          )
def test_addition(a: Number, b: Number, expected: Number) -> None:

    result = operations.additon(a,b)
    assert result == expected, f"Expected addition({a},{b}) to be {expected} but got {result}"

#---------------------------------------
# Unit tests for subtraction method
#---------------------------------------

@pytest.mark.parametrize("a, b, expected",
                         [(2,1,1), # subtracting two positive ints
                          (0,0,0), # subtracting two zeros
                          (1,-1,2), # subtracting a a negrative from a positive int
                          (-1,-1,0), # subtracting a negative int from negative int
                          (2.5,1.5,1.0), # subtracting two positive floats
                          (-1.5,2.5,-4.0)], #subtracting negative and positive float
                          ids=[
                              "subtract_two_positive_ints",
                              "subtract_two_zeros",
                              "subtracting_negative_and_positive_int",
                              "subtract_two_negative_ints",
                              "subtract_two_positive_floats",
                              "subtract_negative_and_positive_floats"
                          ]
                          )
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = operations.subtraction(a,b)
    assert result == expected, f"expected subtraction({a},{b}) to be {expected} but got {result})"

#---------------------------------------
# Unit tests for multiplication method
#---------------------------------------

@pytest.mark.parametrize("a, b, expected",
                         [(2,1,2), # multiply two positive ints
                          (-2,1,-2), # multiply one negative int and one positive int
                          (-2,-2,4), # multiply two negative ints
                          (0,1,0), # multiply an 0 by an int
                          (1.5,1.5,2.25)], # multiply two floats
                        ids=[
                              "multiply_two_positive_ints",
                              "multiply_negative_and_positive_int",
                              "multiply_two_negative_ints",
                              "multiply_0_by_an_int",
                              "multiply_two_floats"
                          ]
                          )
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    result = operations.multiplication(a,b)
    assert result == expected, f"expected multiplication({a},{b}) to be {expected} but got {result}"

#---------------------------------------
# Unit tests for division method
#---------------------------------------
@pytest.mark.parametrize("a, b, expected",
                         [(2,1,2), # divide two positive ints
                          (-2,1,-2), # divide one negative int and one positive int
                          (-2,-2,1), # dividey two negative ints
                          (1.5,1.5,1)], # divide two floats
                        ids=[
                              "divide_two_positive_ints",
                              "divide_negative_by_positive_int",
                              "divide_two_negative_ints",
                              "divide_two_floats"
                          ]
                          )
def test_division(a: Number, b:Number, expected: Number) -> None:

    result = operations.division(a,b)
    assert result == expected, f"expected division({a},{b}) to be {expected} but got {result}"