
import pytest
from flutes.structure import map_structure
from collections import namedtuple

def test_map_structure():
    # Test with a list
    def square(x: int) -> int:
        return x ** 2
    
    assert map_structure(square, [1, 2, 3]) == [1, 4, 9]
    
    # Test with a tuple
    assert map_structure(square, (1, 2, 3)) == (1, 4, 9)
    
    # Test with a dictionary
    assert map_structure(square, {'a': 1, 'b': 2}) == {'a': 1, 'b': 4}
    
    # Test with a set
    assert map_structure(square, {1, 2, 3}) == {1, 4, 9}
    
    # Test with nested structure (list of lists)
    nested_list = [[1, 2], [3, 4]]
    expected_nested_list = [[1, 4], [9, 16]]
    assert map_structure(lambda x: x ** 2, nested_list) == expected_nested_list
    
    # Test with namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    points = [Point(1, 2), Point(3, 4)]
    expected_points = [Point(1, 4), Point(9, 16)]
    assert map_structure(lambda p: Point(p.x ** 2, p.y ** 2), points) == expected_points

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________________ test_map_structure ______________________________

    def test_map_structure():
        # Test with a list
        def square(x: int) -> int:
            return x ** 2
    
        assert map_structure(square, [1, 2, 3]) == [1, 4, 9]
    
        # Test with a tuple
        assert map_structure(square, (1, 2, 3)) == (1, 4, 9)
    
        # Test with a dictionary
        assert map_structure(square, {'a': 1, 'b': 2}) == {'a': 1, 'b': 4}
    
        # Test with a set
        assert map_structure(square, {1, 2, 3}) == {1, 4, 9}
    
        # Test with nested structure (list of lists)
        nested_list = [[1, 2], [3, 4]]
        expected_nested_list = [[1, 4], [9, 16]]
        assert map_structure(lambda x: x ** 2, nested_list) == expected_nested_list
    
        # Test with namedtuple
        Point = namedtuple('Point', ['x', 'y'])
        points = [Point(1, 2), Point(3, 4)]
        expected_points = [Point(1, 4), Point(9, 16)]
>       assert map_structure(lambda p: Point(p.x ** 2, p.y ** 2), points) == expected_points

flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_edge_cases.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/structure.py:85: in map_structure
    return [map_structure(fn, x) for x in obj]
flutes/flutes/structure.py:85: in <listcomp>
    return [map_structure(fn, x) for x in obj]
flutes/flutes/structure.py:88: in map_structure
    return type(obj)(*[map_structure(fn, x) for x in obj])
flutes/flutes/structure.py:88: in <listcomp>
    return type(obj)(*[map_structure(fn, x) for x in obj])
flutes/flutes/structure.py:96: in map_structure
    return fn(obj)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

p = 1

>   assert map_structure(lambda p: Point(p.x ** 2, p.y ** 2), points) == expected_points
E   AttributeError: 'int' object has no attribute 'x'

flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_edge_cases.py:31: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_edge_cases.py::test_map_structure
============================== 1 failed in 0.11s ===============================
"""