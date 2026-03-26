
import pytest
from dataclasses_json.core import _decode_type, is_dataclass, _has_decoder_in_global_config, _get_decoder_in_global_config, _is_supported_generic, _decode_generic, _support_extended_types, _decode_dict_keys
from dataclasses import dataclass
from typing import Any, List, Dict, Union
import json

@pytest.mark.parametrize("type_, value, infer_missing, expected", [
    (int, "42", True, 42),
    (str, b"hello", True, "hello"),
    (list, "[1, 2, 3]", True, [1, 2, 3]),
    (dict, '{"key": "value"}', True, {"key": "value"}),
    (None, None, False, None),
])
def test_edge_case_none(type_, value, infer_missing, expected):
    result = _decode_type(type_, value, infer_missing)
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
collected 5 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py . [ 20%]
FFF.                                                                     [100%]

=================================== FAILURES ===================================
__________________ test_edge_case_none[str-hello-True-hello] ___________________

type_ = <class 'str'>, value = b'hello', infer_missing = True
expected = 'hello'

    @pytest.mark.parametrize("type_, value, infer_missing, expected", [
        (int, "42", True, 42),
        (str, b"hello", True, "hello"),
        (list, "[1, 2, 3]", True, [1, 2, 3]),
        (dict, '{"key": "value"}', True, {"key": "value"}),
        (None, None, False, None),
    ])
    def test_edge_case_none(type_, value, infer_missing, expected):
        result = _decode_type(type_, value, infer_missing)
>       assert result == expected
E       assert "b'hello'" == 'hello'
E         
E         - hello
E         + b'hello'
E         ? ++     +

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py:17: AssertionError
______________ test_edge_case_none[list-[1, 2, 3]-True-expected2] ______________

type_ = <class 'list'>, value = '[1, 2, 3]', infer_missing = True
expected = [1, 2, 3]

    @pytest.mark.parametrize("type_, value, infer_missing, expected", [
        (int, "42", True, 42),
        (str, b"hello", True, "hello"),
        (list, "[1, 2, 3]", True, [1, 2, 3]),
        (dict, '{"key": "value"}', True, {"key": "value"}),
        (None, None, False, None),
    ])
    def test_edge_case_none(type_, value, infer_missing, expected):
        result = _decode_type(type_, value, infer_missing)
>       assert result == expected
E       AssertionError: assert ['[', '1', ',...'2', ',', ...] == [1, 2, 3]
E         
E         At index 0 diff: '[' != 1
E         Left contains 6 more items, first extra item: ' '
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py:17: AssertionError
__________ test_edge_case_none[dict-{"key": "value"}-True-expected3] ___________

type_ = <class 'dict'>, value = '{"key": "value"}', infer_missing = True
expected = {'key': 'value'}

    @pytest.mark.parametrize("type_, value, infer_missing, expected", [
        (int, "42", True, 42),
        (str, b"hello", True, "hello"),
        (list, "[1, 2, 3]", True, [1, 2, 3]),
        (dict, '{"key": "value"}', True, {"key": "value"}),
        (None, None, False, None),
    ])
    def test_edge_case_none(type_, value, infer_missing, expected):
>       result = _decode_type(type_, value, infer_missing)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:247: in _decode_type
    return _decode_generic(type_, value, infer_missing)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = <class 'dict'>, value = '{"key": "value"}', infer_missing = True

    def _decode_generic(type_, value, infer_missing):
        if value is None:
            res = value
        elif _issubclass_safe(type_, Enum):
            # Convert to an Enum using the type as a constructor.
            # Assumes a direct match is found.
            res = type_(value)
        # FIXME this is a hack to fix a deeper underlying issue. A refactor is due.
        elif _is_collection(type_):
            if _is_mapping(type_) and not _is_counter(type_):
                k_type, v_type = _get_type_args(type_, (Any, Any))
                # a mapping type has `.keys()` and `.values()`
                # (see collections.abc)
>               ks = _decode_dict_keys(k_type, value.keys(), infer_missing)
E               AttributeError: 'str' object has no attribute 'keys'

dataclasses-json/dataclasses_json/core.py:303: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py::test_edge_case_none[str-hello-True-hello]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py::test_edge_case_none[list-[1, 2, 3]-True-expected2]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py::test_edge_case_none[dict-{"key": "value"}-True-expected3]
========================= 3 failed, 2 passed in 0.05s ==========================

"""