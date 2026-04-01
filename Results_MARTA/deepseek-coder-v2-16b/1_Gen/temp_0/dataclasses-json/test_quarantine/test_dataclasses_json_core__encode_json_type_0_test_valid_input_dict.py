
from dataclasses_json.core import _encode_json_type, _ExtendedEncoder
from unittest.mock import patch, Mock
import pytest

class MockEncoder(Mock):
    def default(self, obj):
        return str(obj)

@pytest.mark.parametrize("value", [
    ({'key': 'value'}),  # Test dictionary input
    ([1, 2, {'nested_key': 'nested_value'}])  # Test list with nested structure
])
def test_valid_input_dict(value):
    with patch('dataclasses_json.core._ExtendedEncoder', MockEncoder):
        encoded = _encode_json_type(value)
        if isinstance(encoded, dict):
            assert all(isinstance(k, str) and isinstance(v, str) for k, v in encoded.items())  # Check keys and values are strings
        elif isinstance(encoded, list):
            assert all(isinstance(item, str) for item in encoded)  # Check items are strings

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_dict.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_dict[value1] _________________________

value = [1, 2, {'nested_key': 'nested_value'}]

    @pytest.mark.parametrize("value", [
        ({'key': 'value'}),  # Test dictionary input
        ([1, 2, {'nested_key': 'nested_value'}])  # Test list with nested structure
    ])
    def test_valid_input_dict(value):
        with patch('dataclasses_json.core._ExtendedEncoder', MockEncoder):
            encoded = _encode_json_type(value)
            if isinstance(encoded, dict):
                assert all(isinstance(k, str) and isinstance(v, str) for k, v in encoded.items())  # Check keys and values are strings
            elif isinstance(encoded, list):
>               assert all(isinstance(item, str) for item in encoded)  # Check items are strings
E               assert False
E                +  where False = all(<generator object test_valid_input_dict.<locals>.<genexpr> at 0x1043f8190>)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_dict.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_dict.py::test_valid_input_dict[value1]
========================= 1 failed, 1 passed in 0.03s ==========================

"""