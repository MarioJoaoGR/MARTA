
import pytest
from flutes.structure import map_structure_zip
from collections import namedtuple, OrderedDict

def test_valid_input():
    def add(a, b): return a + b
    
    # Test with lists of numbers
    assert map_structure_zip(add, [[1, 2], [3, 4]]) == [4, 6]
    
    # Test with namedtuples
    Point = namedtuple('Point', ['x', 'y'])
    points = [Point(1, 2), Point(3, 4)]
    assert map_structure_zip(add, points) == Point(x=4, y=6)
    
    # Test with tuples of numbers
    assert map_structure_zip(lambda a, b: a * b, [(1, 2), (3, 4)]) == [3, 8]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def add(a, b): return a + b
    
        # Test with lists of numbers
        assert map_structure_zip(add, [[1, 2], [3, 4]]) == [4, 6]
    
        # Test with namedtuples
        Point = namedtuple('Point', ['x', 'y'])
        points = [Point(1, 2), Point(3, 4)]
        assert map_structure_zip(add, points) == Point(x=4, y=6)
    
        # Test with tuples of numbers
>       assert map_structure_zip(lambda a, b: a * b, [(1, 2), (3, 4)]) == [3, 8]
E       assert (3, 8) == [3, 8]
E         
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_valid_input.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.12s ===============================
"""