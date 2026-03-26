
import pytest
from dataclasses_json import utils as dtu
from typing import List, Tuple

@pytest.mark.parametrize("type_, args, expected", [
    (List[int], ('a', 'b'), True),  # True, since both 'a' and 'b' are in List[int].
    (Tuple[int, int], (1, 2), True),  # True, since both 1 and 2 are in Tuple[int, int].
    (List[str], ('a',), False),       # False, because 'a' is not in List[str].
    (Tuple[int, str], (1, 'a'), False)# False, because 'a' is not an int.
])
def test_valid_input(type_, args, expected):
    assert dtu._hasargs(type_, *args) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_valid_input.py F [ 25%]
F..                                                                      [100%]

=================================== FAILURES ===================================
______________________ test_valid_input[List-args0-True] _______________________

type_ = typing.List[int], args = ('a', 'b'), expected = True

    @pytest.mark.parametrize("type_, args, expected", [
        (List[int], ('a', 'b'), True),  # True, since both 'a' and 'b' are in List[int].
        (Tuple[int, int], (1, 2), True),  # True, since both 1 and 2 are in Tuple[int, int].
        (List[str], ('a',), False),       # False, because 'a' is not in List[str].
        (Tuple[int, str], (1, 'a'), False)# False, because 'a' is not an int.
    ])
    def test_valid_input(type_, args, expected):
>       assert dtu._hasargs(type_, *args) == expected
E       AssertionError: assert False == True
E        +  where False = <function _hasargs at 0x101f585e0>(typing.List[int], *('a', 'b'))
E        +    where <function _hasargs at 0x101f585e0> = dtu._hasargs

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_valid_input.py:13: AssertionError
______________________ test_valid_input[Tuple-args1-True] ______________________

type_ = typing.Tuple[int, int], args = (1, 2), expected = True

    @pytest.mark.parametrize("type_, args, expected", [
        (List[int], ('a', 'b'), True),  # True, since both 'a' and 'b' are in List[int].
        (Tuple[int, int], (1, 2), True),  # True, since both 1 and 2 are in Tuple[int, int].
        (List[str], ('a',), False),       # False, because 'a' is not in List[str].
        (Tuple[int, str], (1, 'a'), False)# False, because 'a' is not an int.
    ])
    def test_valid_input(type_, args, expected):
>       assert dtu._hasargs(type_, *args) == expected
E       assert False == True
E        +  where False = <function _hasargs at 0x101f585e0>(typing.Tuple[int, int], *(1, 2))
E        +    where <function _hasargs at 0x101f585e0> = dtu._hasargs

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_valid_input.py::test_valid_input[List-args0-True]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_valid_input.py::test_valid_input[Tuple-args1-True]
========================= 2 failed, 2 passed in 0.03s ==========================
"""