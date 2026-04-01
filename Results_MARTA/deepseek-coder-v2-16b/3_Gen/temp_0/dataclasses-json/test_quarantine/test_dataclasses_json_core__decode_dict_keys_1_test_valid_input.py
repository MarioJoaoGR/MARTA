
import pytest
from dataclasses_json.core import _decode_dict_keys, _get_type_origin
from typing import Any, TypeVar, Tuple, List, Union
from unittest.mock import patch

@pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
    (None, {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
    ([int, tuple], {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
    (None, {'key1': 'value1', 'key2': 'value2'}, True, {'key1': 'value1', 'key2': 'value2'}),
    ([int], {'a': 'value1', 2: 'value2'}, False, {'a': 'value1', 2: 'value2'})
])
def test_valid_input(key_type, xs, infer_missing, expected):
    with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
        result = _decode_dict_keys(key_type, xs, infer_missing)
        assert result == expected

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________ test_valid_input[None-xs0-True-expected0] ___________________

key_type = None, xs = {1: 'value', (2, 3): 'another value'}
infer_missing = True, expected = {1: 'value', (2, 3): 'another value'}

    @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
        (None, {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
        ([int, tuple], {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
        (None, {'key1': 'value1', 'key2': 'value2'}, True, {'key1': 'value1', 'key2': 'value2'}),
        ([int], {'a': 'value1', 2: 'value2'}, False, {'a': 'value1', 2: 'value2'})
    ])
    def test_valid_input(key_type, xs, infer_missing, expected):
        with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
            result = _decode_dict_keys(key_type, xs, infer_missing)
>           assert result == expected
E           AssertionError: assert <map object at 0x1036f8ee0> == {1: 'value', ...nother value'}
E             
E             Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py:16: AssertionError
________________ test_valid_input[key_type1-xs1-True-expected1] ________________

key_type = [<class 'int'>, <class 'tuple'>]
xs = {1: 'value', (2, 3): 'another value'}, infer_missing = True
expected = {1: 'value', (2, 3): 'another value'}

    @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
        (None, {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
        ([int, tuple], {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
        (None, {'key1': 'value1', 'key2': 'value2'}, True, {'key1': 'value1', 'key2': 'value2'}),
        ([int], {'a': 'value1', 2: 'value2'}, False, {'a': 'value1', 2: 'value2'})
    ])
    def test_valid_input(key_type, xs, infer_missing, expected):
        with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
>           result = _decode_dict_keys(key_type, xs, infer_missing)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

key_type = [<class 'int'>, <class 'tuple'>]
xs = {1: 'value', (2, 3): 'another value'}, infer_missing = True

    def _decode_dict_keys(key_type, xs, infer_missing):
        """
        Because JSON object keys must be strs, we need the extra step of decoding
        them back into the user's chosen python type
        """
        decode_function = key_type
        # handle NoneType keys... it's weird to type a Dict as NoneType keys
        # but it's valid...
        # Issue #341 and PR #346:
        #   This is a special case for Python 3.7 and Python 3.8.
        #   By some reason, "unbound" dicts are counted
        #   as having key type parameter to be TypeVar('KT')
        if key_type is None or key_type == Any or isinstance(key_type, TypeVar):
            decode_function = key_type = (lambda x: x)
        # handle a nested python dict that has tuples for keys. E.g. for
        # Dict[Tuple[int], int], key_type will be typing.Tuple[int], but
        # decode_function should be tuple, so map() doesn't break.
        #
        # Note: _get_type_origin() will return typing.Tuple for python
        # 3.6 and tuple for 3.7 and higher.
>       elif _get_type_origin(key_type) in {tuple, Tuple}:
E       TypeError: unhashable type: 'list'

dataclasses-json/dataclasses_json/core.py:369: TypeError
__________________ test_valid_input[None-xs2-True-expected2] ___________________

key_type = None, xs = {'key1': 'value1', 'key2': 'value2'}, infer_missing = True
expected = {'key1': 'value1', 'key2': 'value2'}

    @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
        (None, {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
        ([int, tuple], {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
        (None, {'key1': 'value1', 'key2': 'value2'}, True, {'key1': 'value1', 'key2': 'value2'}),
        ([int], {'a': 'value1', 2: 'value2'}, False, {'a': 'value1', 2: 'value2'})
    ])
    def test_valid_input(key_type, xs, infer_missing, expected):
        with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
            result = _decode_dict_keys(key_type, xs, infer_missing)
>           assert result == expected
E           AssertionError: assert <map object at 0x103740190> == {'key1': 'val...y2': 'value2'}
E             
E             Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py:16: AssertionError
_______________ test_valid_input[key_type3-xs3-False-expected3] ________________

key_type = [<class 'int'>], xs = {'a': 'value1', 2: 'value2'}
infer_missing = False, expected = {'a': 'value1', 2: 'value2'}

    @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
        (None, {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
        ([int, tuple], {1: 'value', (2, 3): 'another value'}, True, {1: 'value', (2, 3): 'another value'}),
        (None, {'key1': 'value1', 'key2': 'value2'}, True, {'key1': 'value1', 'key2': 'value2'}),
        ([int], {'a': 'value1', 2: 'value2'}, False, {'a': 'value1', 2: 'value2'})
    ])
    def test_valid_input(key_type, xs, infer_missing, expected):
        with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
>           result = _decode_dict_keys(key_type, xs, infer_missing)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

key_type = [<class 'int'>], xs = {'a': 'value1', 2: 'value2'}
infer_missing = False

    def _decode_dict_keys(key_type, xs, infer_missing):
        """
        Because JSON object keys must be strs, we need the extra step of decoding
        them back into the user's chosen python type
        """
        decode_function = key_type
        # handle NoneType keys... it's weird to type a Dict as NoneType keys
        # but it's valid...
        # Issue #341 and PR #346:
        #   This is a special case for Python 3.7 and Python 3.8.
        #   By some reason, "unbound" dicts are counted
        #   as having key type parameter to be TypeVar('KT')
        if key_type is None or key_type == Any or isinstance(key_type, TypeVar):
            decode_function = key_type = (lambda x: x)
        # handle a nested python dict that has tuples for keys. E.g. for
        # Dict[Tuple[int], int], key_type will be typing.Tuple[int], but
        # decode_function should be tuple, so map() doesn't break.
        #
        # Note: _get_type_origin() will return typing.Tuple for python
        # 3.6 and tuple for 3.7 and higher.
>       elif _get_type_origin(key_type) in {tuple, Tuple}:
E       TypeError: unhashable type: 'list'

dataclasses-json/dataclasses_json/core.py:369: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py::test_valid_input[None-xs0-True-expected0]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py::test_valid_input[key_type1-xs1-True-expected1]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py::test_valid_input[None-xs2-True-expected2]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py::test_valid_input[key_type3-xs3-False-expected3]
============================== 4 failed in 0.05s ===============================
"""