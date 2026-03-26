
import pytest
from typing import Callable, Collection, TypeVar
from collections import namedtuple

T = TypeVar('T')
R = TypeVar('R')

# Import the function from its module
from flutes.structure import map_structure

def test_map_structure_direct_return():
    def identity(x):
        return x
    
    # Test when obj is not a list, tuple, dict, or set
    obj = 123
    result = map_structure(identity, obj)
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

flutes/Test4DT_tests/test_flutes_structure_map_structure_2.py .F         [100%]

=================================== FAILURES ===================================
________________________ test_map_structure_namedtuple _________________________

    def test_map_structure_namedtuple():
        Point = namedtuple('Point', ['x', 'y'])
    
        def add_one(p):
            return Point(p.x + 1, p.y + 1)
    
        point = Point(1, 2)
        expected = Point(2, 3)
>       result = map_structure(add_one, point)

flutes/Test4DT_tests/test_flutes_structure_map_structure_2.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/structure.py:88: in map_structure
    return type(obj)(*[map_structure(fn, x) for x in obj])
flutes/flutes/structure.py:88: in <listcomp>
    return type(obj)(*[map_structure(fn, x) for x in obj])
flutes/flutes/structure.py:96: in map_structure
    return fn(obj)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

p = 1

    def add_one(p):
>       return Point(p.x + 1, p.y + 1)
E       AttributeError: 'int' object has no attribute 'x'

flutes/Test4DT_tests/test_flutes_structure_map_structure_2.py:25: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_2.py::test_map_structure_namedtuple
========================= 1 failed, 1 passed in 0.10s ==========================
"""