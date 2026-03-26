
from typing import Iterator

class Range:
    """A replacement for built-in :py:class:`range` with support for indexing operators. For example:
    
        .. code:: python
    
            >>> r = Range(10)         # (end)
            >>> r = Range(1, 10 + 1)  # (start, end)
            >>> r = Range(1, 11, 2)   # (start, end, step)
            >>> print(r[0], r[2], r[4])
            1 5 9
    
    A class that mimics the behavior of Python's built-in `range` with support for indexing operators. This allows instances of this class to be sliced and indexed like a list or tuple.

    Parameters:
        - *args (int): Accepts one, two, or three arguments which correspond to the parameters used in the built-in `range` function: start, stop, and step respectively. If only one argument is provided, it is treated as the 'stop' value. If two arguments are given, they are treated as 'start' and 'stop'. If three arguments are provided, they are treated as 'start', 'stop', and 'step'.
    
    Raises:
        - ValueError: Raised if zero or more than three arguments are passed to the constructor.
    
    Examples:
        Creating a Range instance with different numbers of arguments:
            >>> r = Range(10)         # Equivalent to range(10)
            >>> print(r[0], r[2], r[4])  # Outputs: 0, 2, 4 (since step is defaulted to 1)
        
        Creating a Range instance with start and stop values:
            >>> r = Range(1, 10 + 1)  # Equivalent to range(1, 11)
            >>> print(r[0], r[2], r[4])  # Outputs: 1, 3, 5
        
        Creating a Range instance with start, stop, and step values:
            >>> r = Range(1, 11, 2)   # Equivalent to range(1, 11, 2)
            >>> print(r[0], r[2], r[4])  # Outputs: 1, 3, 5
    
    Returns:
        - An instance of the Range class that supports indexing and can be iterated over.
    
    Usage:
        This class is useful when you need a sequence object that behaves like Python's built-in `range` but with additional features or compatibility with list/tuple indexing. It can be used in loops, indexed access, and other operations where standard range behavior is required.
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

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index >= self.length:
                raise IndexError("Index out of range")
            return self.val + index * self.step
        else:
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else self.length
            step = index.step if index.step is not None else 1
            if step == 0 or (start - self.val) * step < 0:
                raise ValueError("Step must be non-zero")
            result = []
            current = start + self.val
            while (current - self.val) * step < (stop - self.val) * step:
                result.append(current)
                current += step
            return result

    def __iter__(self):
        return RangeIterator(self)

class RangeIterator:
    def __init__(self, range_obj):
        self.range_obj = range_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.range_obj.length:
            raise StopIteration
        value = self.range_obj.val + self.index * self.range_obj.step
        self.index += 1
        return value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.04s =============================
"""