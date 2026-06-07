import pytest
from src.operations import operations
from typing import Union

Number = Union[int,float]

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
    
