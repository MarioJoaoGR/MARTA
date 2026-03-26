
from typing import Any, Callable, Iterable

import pytest

from isort.sorting import _natural_keys, naturally


# Test cases for the naturally function
def test_naturally_default():
    result = naturally(['item12', 'item2', 'item1'])
    assert result == ['item1', 'item2', 'item12']

def test_naturally_custom_key():
    result = naturally(to_sort=['file10.txt', 'file2.txt', 'file1.txt'], key=lambda x: x.split('.')[-1])