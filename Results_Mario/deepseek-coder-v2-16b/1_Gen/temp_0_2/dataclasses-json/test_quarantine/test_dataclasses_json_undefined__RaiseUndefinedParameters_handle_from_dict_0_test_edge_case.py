
from dataclasses_json.undefined import UndefinedParameterError
import pytest
from unittest.mock import patch

# Assuming _RaiseUndefinedParameters is defined in a module named dataclasses_json.undefined
from dataclasses_json.undefined import _RaiseUndefinedParameters

def test_handle_from_dict_raises_error():
    class TestClass:
        pass  # Example class with no fields, just for testing purposes

    kvs = {'param1': 1, 'extra_param': 2}
    
    with pytest.raises(UndefinedParameterError) as excinfo:
        _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
        
    assert str(excinfo.value) == "Received undefined initialization arguments {'extra_param'}"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
______________________ test_handle_from_dict_raises_error ______________________

    def test_handle_from_dict_raises_error():
        class TestClass:
            pass  # Example class with no fields, just for testing purposes
    
        kvs = {'param1': 1, 'extra_param': 2}
    
        with pytest.raises(UndefinedParameterError) as excinfo:
>           _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_case.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/undefined.py:69: in handle_from_dict
    _UndefinedParameterAction._separate_defined_undefined_kvs(
dataclasses-json/dataclasses_json/undefined.py:51: in _separate_defined_undefined_kvs
    class_fields = fields(cls)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

class_or_instance = <class 'Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_case.test_handle_from_dict_raises_error.<locals>.TestClass'>

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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_case.py::test_handle_from_dict_raises_error
============================== 1 failed in 0.05s ===============================
"""