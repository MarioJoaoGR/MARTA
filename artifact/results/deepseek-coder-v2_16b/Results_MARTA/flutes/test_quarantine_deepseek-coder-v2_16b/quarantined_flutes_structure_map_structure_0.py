
import pytest
from typing import Callable, Collection
from collections import namedtuple

# Define the transformation function
def square(x):
    return x ** 2

# Define a nested collection (list)
nested_list = [1, 2, 3, 4, 5]

# Apply map_structure to transform elements in the list
transformed_list = map_structure(square, nested_list)
print(transformed_list)  # Output: [1, 4, 9, 16, 25]

# Define a nested collection (tuple)
nested_tuple = (1, 2, 3, 4, 5)

# Apply map_structure to transform elements in the tuple
transformed_tuple = map_structure(square, nested_tuple)
print(transformed_tuple)  # Output: (1, 4, 9, 16, 25)

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])
nested_namedtuple = Point(1, 2)

# Apply map_structure to transform elements in the namedtuple
transformed_namedtuple = map_structure(square, nested_namedtuple)
print(transformed_namedtuple)  # Output: Point(x=1, y=4)

# Define a nested collection (dictionary)
nested_dict = {1: 2, 3: 4}

# Apply map_structure to transform elements in the dictionary
transformed_dict = map_structure(square, nested_dict)
print(transformed_dict)  # Output: {1: 4, 3: 16}

def test_map_structure_list():
    def square(x):
        return x ** 2

    nested_list = [1, 2, 3, 4, 5]
    transformed_list = map_structure(square, nested_list)
    assert transformed_list == [1, 4, 9, 16, 25]

def test_map_structure_tuple():
    def square(x):
        return x ** 2

    nested_tuple = (1, 2, 3, 4, 5)
    transformed_tuple = map_structure(square, nested_tuple)
    assert transformed_tuple == (1, 4, 9, 16, 25)

def test_map_structure_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    nested_namedtuple = Point(1, 2)

    def square(point):
        return Point(square(point.x), square(point.y))

    transformed_namedtuple = map_structure(square, nested_namedtuple)
    assert transformed_namedtuple == Point(1, 4)

def test_map_structure_dict():
    def square(x):
        return x ** 2

    nested_dict = {1: 2, 3: 4}
    transformed_dict = map_structure(square, nested_dict)
    assert transformed_dict == {1: 4, 3: 16}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__________ ERROR collecting test_flutes_structure_map_structure_0.py ___________
/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_structure_map_structure_0.py:14: in <module>
    transformed_list = map_structure(square, nested_list)
E   NameError: name 'map_structure' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_structure_map_structure_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""