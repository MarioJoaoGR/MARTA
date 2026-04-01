
import pytest
from flutes.structure import map_structure_zip
from collections import namedtuple

def test_map_structure_zip():
    def add(a, b): return a + b
    
    # Test with lists
    result = map_structure_zip(add, [[1, 2], [3, 4]])
    assert result == [4, 6]
    
    # Test with namedtuples
    Point = namedtuple('Point', ['x', 'y'])
    points = [Point(1, 2), Point(3, 4)]
    result = map_structure_zip(add, points)
    assert result == Point(x=4, y=6)
    
    # Test with tuples
    result = map_structure_zip(lambda a, b: a * b, [(1, 2), (3, 4)])
    assert result == [3, 8]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
____________________________ test_map_structure_zip ____________________________

    def test_map_structure_zip():
        def add(a, b): return a + b
    
        # Test with lists
        result = map_structure_zip(add, [[1, 2], [3, 4]])
        assert result == [4, 6]
    
        # Test with namedtuples
        Point = namedtuple('Point', ['x', 'y'])
        points = [Point(1, 2), Point(3, 4)]
        result = map_structure_zip(add, points)
        assert result == Point(x=4, y=6)
    
        # Test with tuples
        result = map_structure_zip(lambda a, b: a * b, [(1, 2), (3, 4)])
>       assert result == [3, 8]
E       assert (3, 8) == [3, 8]
E         
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_edge_cases.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_edge_cases.py::test_map_structure_zip
============================== 1 failed in 0.11s ===============================
"""