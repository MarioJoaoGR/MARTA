
from flutes.iterator import Iterator
import pytest

class Range:
    """A replacement for built-in :py:class:`range` with support for indexing operators. For example:
    
        .. code:: python
    
            >>> r = Range(10)         # (end)
            >>> r = Range(1, 10 + 1)  # (start, end)
            >>> r = Range(1, 11, 2)   # (start, end, step)
            >>> print(r[0], r[2], r[4])
            1 5 9
    
    A class that mimics the behavior of Python's built-in `range` class, supporting indexing operators. This allows for creating a sequence of numbers with optional start, stop, and step parameters. The range is inclusive at the end (i.e., it includes the value specified by 'end', but does not include the value immediately past the 'end').
    
    Parameters:
        *args: Accepts one to three arguments which determine the start, stop, and step of the sequence respectively. If only one argument is provided, it is treated as the end of the range with a default start of 0 and a step of 1. If two arguments are given, they are interpreted as the start and end values, with a default step of 1. If three arguments are provided, they represent the start, stop, and step values respectively.
    
    Raises:
        ValueError: Raised if the function is called without any arguments or more than three arguments.
    
    Returns:
        An object of type Range that can be indexed to retrieve specific elements in the sequence.
    
    Examples:
        Creating a range from 0 to 9 with a step size of 1:
            >>> r = Range(10)
            >>> print(r[0], r[2], r[4])  # Outputs: 0 2 4
        
        Creating a range from 1 to 10 with a default step size of 1:
            >>> r = Range(1, 10 + 1)
            >>> print(r[0], r[2], r[4])  # Outputs: 1 3 5
        
        Creating a range from 1 to 11 with a step size of 2:
            >>> r = Range(1, 11, 2)
            >>> print(r[0], r[2], r[4])  # Outputs: 1 5 9
        
        Using the range in a loop or other operations that support indexing.
    """
    def __init__(self, *args):
        if len(args) == 0 or len(args) > 3:
            raise ValueError("Range should be called the same way as the builtin `range`")
        if len(args) == 1:
            self.l = 0
            self.r = args[0]
            self.step = 1
        else:
            self.l = args[0]
            self.r = args[1]
            self.step = 1 if len(args) == 2 else args[2]
        self.val = self.l
        self.length = (self.r - self.l) // self.step

    def __iter__(self):
        """
        Returns an iterator over the range defined by the start, stop, and step parameters.
        
        Parameters:
            l (int): The starting value of the range.
            r (int): The ending value of the range (exclusive).
            step (int, optional): The difference between each number in the sequence. Defaults to 1.
            
        Returns:
            Iterator[int]: An iterator that yields integers from `l` to `r`, incrementing by `step`.
        
        Usage:
            To use this method, create an instance of the `Range` class with appropriate parameters and call `__iter__()` on it. For example:
            
            ```python
            r = Range(1, 10 + 1)
            for value in r.__iter__():
                print(value)
            ```
        """
        return Iterator(self.l, self.r, self.step)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___iter___3_test_error_case_invalid_arguments
flutes/Test4DT_tests/test_flutes_iterator_Range___iter___3_test_error_case_invalid_arguments.py:77:15: E0110: Abstract class 'Iterator' with abstract methods instantiated (abstract-class-instantiated)

"""