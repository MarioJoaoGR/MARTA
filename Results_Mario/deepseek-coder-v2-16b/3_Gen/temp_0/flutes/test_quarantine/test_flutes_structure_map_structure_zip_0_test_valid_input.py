
import pytest
from flutes.structure import map_structure_zip
from collections import namedtuple, OrderedDict

def test_valid_input():
    # Define a simple function to use for mapping
    def add(a: int, b: int) -> int:
        return a + b
    
    # Test with lists of integers
    assert map_structure_zip(add, [[1, 2], [3, 4]]) == [4, 6]
    
    # Define a namedtuple for testing
    Point = namedtuple('Point', ['x', 'y'])
    
    # Test with a list of namedtuples
    points = [Point(1, 2), Point(3, 4)]
    assert map_structure_zip(add, points) == Point(x=4, y=6)
    
    # Test with tuples and multiplication function
    assert map_structure_zip(lambda a, b: a * b, [(1, 2), (3, 4)]) == [2, 8]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Define a simple function to use for mapping
        def add(a: int, b: int) -> int:
            return a + b
    
        # Test with lists of integers
        assert map_structure_zip(add, [[1, 2], [3, 4]]) == [4, 6]
    
        # Define a namedtuple for testing
        Point = namedtuple('Point', ['x', 'y'])
    
        # Test with a list of namedtuples
        points = [Point(1, 2), Point(3, 4)]
        assert map_structure_zip(add, points) == Point(x=4, y=6)
    
        # Test with tuples and multiplication function
>       assert map_structure_zip(lambda a, b: a * b, [(1, 2), (3, 4)]) == [2, 8]
E       assert (3, 8) == [2, 8]
E         
E         At index 0 diff: 3 != 2
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""