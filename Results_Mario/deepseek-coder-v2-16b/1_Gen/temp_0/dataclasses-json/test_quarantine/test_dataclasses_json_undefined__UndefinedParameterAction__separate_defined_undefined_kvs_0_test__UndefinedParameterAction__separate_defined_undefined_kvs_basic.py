
from dataclasses import fields
from typing import Dict, Tuple
from dataclasses_json.undefined import _UndefinedParameterAction as UPA

class ExampleClass:
    param1: int
    param2: str

def test__UndefinedParameterAction__separate_defined_undefined_kvs_basic():
    kvs = {'param1': 1, 'extra_param': 'test'}
    expected_known = {'param1': 1}
    expected_unknown = {'extra_param': 'test'}

    result = UPA._separate_defined_undefined_kvs(ExampleClass, kvs)
    
    assert result[0] == expected_known
    assert result[1] == expected_unknown

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0_test__UndefinedParameterAction__separate_defined_undefined_kvs_basic.py F [100%]

=================================== FAILURES ===================================
_____ test__UndefinedParameterAction__separate_defined_undefined_kvs_basic _____

    def test__UndefinedParameterAction__separate_defined_undefined_kvs_basic():
        kvs = {'param1': 1, 'extra_param': 'test'}
        expected_known = {'param1': 1}
        expected_unknown = {'extra_param': 'test'}
    
>       result = UPA._separate_defined_undefined_kvs(ExampleClass, kvs)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0_test__UndefinedParameterAction__separate_defined_undefined_kvs_basic.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/undefined.py:51: in _separate_defined_undefined_kvs
    class_fields = fields(cls)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

class_or_instance = <class 'Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0_test__UndefinedParameterAction__separate_defined_undefined_kvs_basic.ExampleClass'>

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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0_test__UndefinedParameterAction__separate_defined_undefined_kvs_basic.py::test__UndefinedParameterAction__separate_defined_undefined_kvs_basic
============================== 1 failed in 0.04s ===============================

"""