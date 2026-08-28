
import pytest
from dataclasses import fields, is_dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters

class MyClass:
    def __init__(self, param1: int, param2: str):
        self.param1 = param1
        self.param2 = param2


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        kvs = {'param1': 10, 'param2': 'value'}
>       known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:89: in handle_from_dict
    _UndefinedParameterAction._separate_defined_undefined_kvs(
/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:50: in _separate_defined_undefined_kvs
    class_fields = fields(cls)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

class_or_instance = <class 'test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.MyClass'>

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

/opt/conda/envs/test4py_env/lib/python3.10/dataclasses.py:1198: TypeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        kvs = {'invalid_key': 'value'}
        with pytest.raises(KeyError):
>           _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:89: in handle_from_dict
    _UndefinedParameterAction._separate_defined_undefined_kvs(
/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:50: in _separate_defined_undefined_kvs
    class_fields = fields(cls)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

class_or_instance = <class 'test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.MyClass'>

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

/opt/conda/envs/test4py_env/lib/python3.10/dataclasses.py:1198: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.py::test_invalid_input
============================== 2 failed in 0.11s ===============================
"""