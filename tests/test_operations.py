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
                          (-1,-1,-2) # adding two negative ints
                          (1.5,2.5,4.0) # adding two positive floats
                          (-1.5,2.5,-1.0)], #adding a positive and a negative float
                          ids=[
                              "add_two_positive_ints",
                              "add_ two_zeros",
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
                          (-1,-1,0) # subtracting a negative int from negative int
                          (2.5,1.5,1.0) # subtracting two positive floats
                          (-1.5,2.5,-4.0)], #subtracting negative and positive float
                          ids=[
                              "subtract_two_positive_ints",
                              "subtract_ two_zeros",
                              "subtracting_negative_and_positive_int",
                              "subtract_two_negative_ints",
                              "subtract_two_positive_floats",
                              "subtract_negative_and_positive_floats"
                          ]
                          )
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = operations.subtraction(a,b)
    assert result == expected, f"expected subtraction({a},{b} to be {expected} but got {result})"

