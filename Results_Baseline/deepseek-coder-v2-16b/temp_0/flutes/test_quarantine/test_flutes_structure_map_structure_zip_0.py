
import pytest
from typing import Callable, Collection, Sequence
from collections import namedtuple

# Import the function from its module
from flutes.structure import map_structure_zip

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

Point = namedtuple('Point', ['x', 'y'])

# Test cases for basic usage
def test_map_structure_zip_basic():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = map_structure_zip(add, [list1, list2])
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0.py .F     [100%]

=================================== FAILURES ===================================
_____________________ test_map_structure_zip_named_tuples ______________________

    def test_map_structure_zip_named_tuples():
        points1 = [Point(1, 2), Point(3, 4)]
        points2 = [Point(5, 6), Point(7, 8)]
>       result = map_structure_zip(lambda p1, p2: Point(p1.x + p2.x, p1.y + p2.y), [points1, points2])

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/structure.py:116: in map_structure_zip
    return [map_structure_zip(fn, xs) for xs in zip(*objs)]
flutes/flutes/structure.py:116: in <listcomp>
    return [map_structure_zip(fn, xs) for xs in zip(*objs)]
flutes/flutes/structure.py:119: in map_structure_zip
    return type(obj)(*[map_structure_zip(fn, xs) for xs in zip(*objs)])
flutes/flutes/structure.py:119: in <listcomp>
    return type(obj)(*[map_structure_zip(fn, xs) for xs in zip(*objs)])
flutes/flutes/structure.py:127: in map_structure_zip
    return fn(*objs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

p1 = 1, p2 = 5

>   result = map_structure_zip(lambda p1, p2: Point(p1.x + p2.x, p1.y + p2.y), [points1, points2])
E   AttributeError: 'int' object has no attribute 'x'

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0.py:28: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0.py::test_map_structure_zip_named_tuples
========================= 1 failed, 1 passed in 0.12s ==========================
"""