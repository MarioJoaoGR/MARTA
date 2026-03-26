
import pytest
from typing import List, Union
from unittest.mock import patch
from dataclasses_json.utils import _get_type_origin, is_dataclass

def is_generic_dataclass(type_):
    """
    Determines whether a given type is a generic dataclass from the typing module, considering differences between Python versions 3.6 and 3.7.

    Parameters:
        type_ (Type): The type object to check for being a generic dataclass.

    Returns:
        bool: True if the type is a generic dataclass, False otherwise.

    Notes:
        - This function first uses `_get_type_origin` to determine the origin of the provided type.
        - It then checks if this origin is a dataclass from the typing module using `is_dataclass`.
        - For Python versions 3.6, it specifically looks for the presence of an attribute that indicates the origin in some cases where `__origin__` might not be available.
        - This function is particularly useful for applications that need to distinguish between dataclasses and other types based on their generic origins from the typing module.

    Examples:
        >>> from typing import List, Union
        >>> MyClass = type('MyClass', (object,), {'attr': int})
        >>> my_generic_class = List[MyClass]
        >>> print(is_generic_dataclass(my_generic_class))  # Output will be False for Python versions >= 3.7 and True if the origin is a dataclass.
    """
    return is_dataclass(_get_type_origin(type_))

@pytest.mark.parametrize("type_, expected", [
    (List[int], True),
    (Union[int, str], True),
    (int, False),
    (str, False),
])
def test_valid_case(type_, expected):
    with patch('dataclasses_json.utils._get_type_origin', return_value=None) as mock_get_type_origin:
        if is_generic_dataclass(type_):
            assert True
        else:
            assert False

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case[List-True] __________________________

type_ = typing.List[int], expected = True

    @pytest.mark.parametrize("type_, expected", [
        (List[int], True),
        (Union[int, str], True),
        (int, False),
        (str, False),
    ])
    def test_valid_case(type_, expected):
        with patch('dataclasses_json.utils._get_type_origin', return_value=None) as mock_get_type_origin:
            if is_generic_dataclass(type_):
                assert True
            else:
>               assert False
E               assert False

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py:42: AssertionError
_________________________ test_valid_case[Union-True] __________________________

type_ = typing.Union[int, str], expected = True

    @pytest.mark.parametrize("type_, expected", [
        (List[int], True),
        (Union[int, str], True),
        (int, False),
        (str, False),
    ])
    def test_valid_case(type_, expected):
        with patch('dataclasses_json.utils._get_type_origin', return_value=None) as mock_get_type_origin:
            if is_generic_dataclass(type_):
                assert True
            else:
>               assert False
E               assert False

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py:42: AssertionError
__________________________ test_valid_case[int-False] __________________________

type_ = <class 'int'>, expected = False

    @pytest.mark.parametrize("type_, expected", [
        (List[int], True),
        (Union[int, str], True),
        (int, False),
        (str, False),
    ])
    def test_valid_case(type_, expected):
        with patch('dataclasses_json.utils._get_type_origin', return_value=None) as mock_get_type_origin:
            if is_generic_dataclass(type_):
                assert True
            else:
>               assert False
E               assert False

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py:42: AssertionError
__________________________ test_valid_case[str-False] __________________________

type_ = <class 'str'>, expected = False

    @pytest.mark.parametrize("type_, expected", [
        (List[int], True),
        (Union[int, str], True),
        (int, False),
        (str, False),
    ])
    def test_valid_case(type_, expected):
        with patch('dataclasses_json.utils._get_type_origin', return_value=None) as mock_get_type_origin:
            if is_generic_dataclass(type_):
                assert True
            else:
>               assert False
E               assert False

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py:42: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py::test_valid_case[List-True]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py::test_valid_case[Union-True]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py::test_valid_case[int-False]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py::test_valid_case[str-False]
============================== 4 failed in 0.04s ===============================
"""