
import pytest
from dataclasses_json import core as dcj_core

@pytest.fixture
def example_list():
    return [1, 'string', {'key': 'value'}]

@pytest.fixture
def example_dict():
    return {'key1': [1, 2], 'key2': {'nestedKey': 'nestedValue'}}

def test_valid_input_list(example_list):
    encoded_list = dcj_core._encode_json_type(example_list)
    assert isinstance(encoded_list, list), "Encoded result should be a list"
    for item in encoded_list:
        assert not isinstance(item, (list, dict)), "Items within the list should not be lists or dictionaries"

def test_valid_input_dict(example_dict):
    encoded_dict = dcj_core._encode_json_type(example_dict)
    assert isinstance(encoded_dict, dict), "Encoded result should be a dictionary"
    for key, value in encoded_dict.items():
        assert not isinstance(key, (list, dict)), "Keys within the dictionary should not be lists or dictionaries"
        assert not isinstance(value, (list, dict)), "Values within the dictionary should not be lists or dictionaries"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_list.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_list _____________________________

example_list = [1, 'string', {'key': 'value'}]

    def test_valid_input_list(example_list):
        encoded_list = dcj_core._encode_json_type(example_list)
        assert isinstance(encoded_list, list), "Encoded result should be a list"
        for item in encoded_list:
>           assert not isinstance(item, (list, dict)), "Items within the list should not be lists or dictionaries"
E           AssertionError: Items within the list should not be lists or dictionaries
E           assert not True
E            +  where True = isinstance({'key': 'value'}, (<class 'list'>, <class 'dict'>))

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_list.py:17: AssertionError
____________________________ test_valid_input_dict _____________________________

example_dict = {'key1': [1, 2], 'key2': {'nestedKey': 'nestedValue'}}

    def test_valid_input_dict(example_dict):
        encoded_dict = dcj_core._encode_json_type(example_dict)
        assert isinstance(encoded_dict, dict), "Encoded result should be a dictionary"
        for key, value in encoded_dict.items():
            assert not isinstance(key, (list, dict)), "Keys within the dictionary should not be lists or dictionaries"
>           assert not isinstance(value, (list, dict)), "Values within the dictionary should not be lists or dictionaries"
E           AssertionError: Values within the dictionary should not be lists or dictionaries
E           assert not True
E            +  where True = isinstance([1, 2], (<class 'list'>, <class 'dict'>))

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_list.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_list.py::test_valid_input_list
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_list.py::test_valid_input_dict
============================== 2 failed in 0.03s ===============================
"""