
import pytest
from dataclasses import fields, Field
from typing import Dict, Tuple, List
from dataclasses_json.undefined import _UndefinedParameterAction

class MockClass:
    def __init__(self, param1=None, param2=None):
        self.param1 = param1
        self.param2 = param2

def test_separate_defined_undefined_kvs():
    mock_cls = MockClass(param1=1, param2="test")
    
    # Test with None input
    result = _UndefinedParameterAction._separate_defined_undefined_kvs(mock_cls, None)
    
    assert isinstance(result[0], dict), "Known parameters should be a dictionary"
    assert isinstance(result[1], dict), "Unknown parameters should be a dictionary"
    assert len(result[0]) == 2, "Expected 2 known parameters"
    assert len(result[1]) == 0, "Expected no unknown parameters"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_____________________ test_separate_defined_undefined_kvs ______________________

    def test_separate_defined_undefined_kvs():
        mock_cls = MockClass(param1=1, param2="test")
    
        # Test with None input
>       result = _UndefinedParameterAction._separate_defined_undefined_kvs(mock_cls, None)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_1_test_edge_case.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/undefined.py:51: in _separate_defined_undefined_kvs
    class_fields = fields(cls)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

class_or_instance = <Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_1_test_edge_case.MockClass object at 0x106006680>

    def fields(class_or_instance):
        """Return a tuple describing the fields of this dataclass.
    
        Accepts a dataclass or an instance of one. Tuple elements are of
        type Field.
        """
    
        # Might it be worth caching this, per class?
        try:
            fields = getattr(class_or_instance, _FIELDS)
        except AttributeError:
>           raise TypeError('must be called with a dataclass type or instance') from None
E           TypeError: must be called with a dataclass type or instance

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/dataclasses.py:1198: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_1_test_edge_case.py::test_separate_defined_undefined_kvs
============================== 1 failed in 0.04s ===============================
"""