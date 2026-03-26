
import pytest
from itertools import count
import collections

# Import the function from its module
from pytutils.iters import consume

def test_consume_entire_iterator():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it)