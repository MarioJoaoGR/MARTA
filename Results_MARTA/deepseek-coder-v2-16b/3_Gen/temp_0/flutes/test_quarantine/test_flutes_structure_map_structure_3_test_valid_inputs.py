
import pytest
from flutes.structure import map_structure
from typing import Callable, Collection, Dict, Set, Tuple, List, Any

# Assuming the function `square` is defined somewhere in your codebase
def square(x):
    return x ** 2

# Test data for parametrization
test_data = [
    ([1, 2, 3],),
    ((1, 2, 3),),
    ({1, 2, 3},)
]

@pytest.mark.parametrize("input_obj", test_data)
def test_valid_inputs(input_obj):
    expected = input_obj[0] if isinstance(input_obj[0], (list, tuple, set)) else {k: v ** 2 for k, v in input_obj[0].items()}
    result = map_structure(square, input_obj[0])
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_valid_inputs[input_obj0] _________________________

input_obj = ([1, 2, 3],)

    @pytest.mark.parametrize("input_obj", test_data)
    def test_valid_inputs(input_obj):
        expected = input_obj[0] if isinstance(input_obj[0], (list, tuple, set)) else {k: v ** 2 for k, v in input_obj[0].items()}
        result = map_structure(square, input_obj[0])
>       assert result == expected
E       assert [1, 4, 9] == [1, 2, 3]
E         
E         At index 1 diff: 4 != 2
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py:21: AssertionError
________________________ test_valid_inputs[input_obj1] _________________________

input_obj = ((1, 2, 3),)

    @pytest.mark.parametrize("input_obj", test_data)
    def test_valid_inputs(input_obj):
        expected = input_obj[0] if isinstance(input_obj[0], (list, tuple, set)) else {k: v ** 2 for k, v in input_obj[0].items()}
        result = map_structure(square, input_obj[0])
>       assert result == expected
E       assert (1, 4, 9) == (1, 2, 3)
E         
E         At index 1 diff: 4 != 2
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py:21: AssertionError
________________________ test_valid_inputs[input_obj2] _________________________

input_obj = ({1, 2, 3},)

    @pytest.mark.parametrize("input_obj", test_data)
    def test_valid_inputs(input_obj):
        expected = input_obj[0] if isinstance(input_obj[0], (list, tuple, set)) else {k: v ** 2 for k, v in input_obj[0].items()}
        result = map_structure(square, input_obj[0])
>       assert result == expected
E       assert {1, 4, 9} == {1, 2, 3}
E         
E         Extra items in the left set:
E         9
E         4
E         Extra items in the right set:
E         2
E         3
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py::test_valid_inputs[input_obj0]
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py::test_valid_inputs[input_obj1]
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py::test_valid_inputs[input_obj2]
============================== 3 failed in 0.11s ===============================
"""