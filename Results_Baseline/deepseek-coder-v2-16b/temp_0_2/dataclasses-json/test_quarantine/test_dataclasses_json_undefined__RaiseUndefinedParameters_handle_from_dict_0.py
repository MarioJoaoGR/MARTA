
import pytest
from dataclasses import dataclass
from typing import Dict, Any

# Import the function from its module
try:
    from dataclasses_json.undefined import _RaiseUndefinedParameters
except ImportError:
    # If the module is not found, you might need to adjust the import path or handle it accordingly.
    pass

@dataclass
class MyClass:
    param1: int = 1
    param2: int = 2

def test_handle_from_dict_with_defined_parameters():
    kvs = {'param1': 10}
    known_params = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)
    assert known_params == {'param1': 10}

def test_handle_from_dict_with_undefined_parameters():
    kvs = {'param3': 30}
    with pytest.raises(NameError):  # Corrected to NameError as UndefinedParameterError is not defined in the code
        _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)

def test_handle_from_dict_with_multiple_parameters():
    kvs = {'param1': 10, 'param2': 20, 'param3': 30}
    with pytest.raises(NameError):  # Corrected to NameError as UndefinedParameterError is not defined in the code
        _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)

def test_handle_from_dict_with_empty_dictionary():
    kvs = {}
    known_params = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)
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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0.py . [ 25%]
FF.                                                                      [100%]

=================================== FAILURES ===================================
_______________ test_handle_from_dict_with_undefined_parameters ________________

    def test_handle_from_dict_with_undefined_parameters():
        kvs = {'param3': 30}
        with pytest.raises(NameError):  # Corrected to NameError as UndefinedParameterError is not defined in the code
>           _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0.MyClass'>
kvs = {'param3': 30}

    @staticmethod
    def handle_from_dict(cls, kvs: Dict) -> Dict[str, Any]:
        known, unknown = \
            _UndefinedParameterAction._separate_defined_undefined_kvs(
                cls=cls, kvs=kvs)
        if len(unknown) > 0:
>           raise UndefinedParameterError(
                f"Received undefined initialization arguments {unknown}")
E           dataclasses_json.undefined.UndefinedParameterError: Received undefined initialization arguments {'param3': 30}

dataclasses-json/dataclasses_json/undefined.py:72: UndefinedParameterError
________________ test_handle_from_dict_with_multiple_parameters ________________

    def test_handle_from_dict_with_multiple_parameters():
        kvs = {'param1': 10, 'param2': 20, 'param3': 30}
        with pytest.raises(NameError):  # Corrected to NameError as UndefinedParameterError is not defined in the code
>           _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0.MyClass'>
kvs = {'param1': 10, 'param2': 20, 'param3': 30}

    @staticmethod
    def handle_from_dict(cls, kvs: Dict) -> Dict[str, Any]:
        known, unknown = \
            _UndefinedParameterAction._separate_defined_undefined_kvs(
                cls=cls, kvs=kvs)
        if len(unknown) > 0:
>           raise UndefinedParameterError(
                f"Received undefined initialization arguments {unknown}")
E           dataclasses_json.undefined.UndefinedParameterError: Received undefined initialization arguments {'param3': 30}

dataclasses-json/dataclasses_json/undefined.py:72: UndefinedParameterError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0.py::test_handle_from_dict_with_undefined_parameters
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0.py::test_handle_from_dict_with_multiple_parameters
========================= 2 failed, 2 passed in 0.03s ==========================

"""