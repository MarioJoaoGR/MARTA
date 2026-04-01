
import pytest
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@pytest.fixture
def create_init():
    def wrapper(obj):
        return _IgnoreUndefinedParameters().create_init(obj)
    return wrapper

def test_edge_cases(create_init):
    class MyClass:
        def __init__(self, a, b=None, c=0):
            self.a = a
            self.b = b
            self.c = c

    modified_init = create_init(MyClass)
    
    # Test with all defined parameters
    instance = MyClass(10, c=20)
    assert hasattr(instance, 'a') and getattr(instance, 'a') == 10
    assert hasattr(instance, 'b') and getattr(instance, 'b') is None
    assert hasattr(instance, 'c') and getattr(instance, 'c') == 20
    
    # Test with undefined parameter (should be ignored)
    instance_undefined = modified_init(MyClass)(10)
    assert hasattr(instance_undefined, 'a') and getattr(instance_undefined, 'a') == 10
    assert not hasattr(instance_undefined, 'b')
    assert not hasattr(instance_undefined, 'c')

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

create_init = <function create_init.<locals>.wrapper at 0x105dd4dc0>

    def test_edge_cases(create_init):
        class MyClass:
            def __init__(self, a, b=None, c=0):
                self.a = a
                self.b = b
                self.c = c
    
        modified_init = create_init(MyClass)
    
        # Test with all defined parameters
        instance = MyClass(10, c=20)
        assert hasattr(instance, 'a') and getattr(instance, 'a') == 10
        assert hasattr(instance, 'b') and getattr(instance, 'b') is None
        assert hasattr(instance, 'c') and getattr(instance, 'c') == 20
    
        # Test with undefined parameter (should be ignored)
>       instance_undefined = modified_init(MyClass)(10)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_edge_cases.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/undefined.py:102: in _ignore_init
    _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
dataclasses-json/dataclasses_json/undefined.py:51: in _separate_defined_undefined_kvs
    class_fields = fields(cls)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

class_or_instance = <class 'Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_edge_cases.test_edge_cases.<locals>.MyClass'>

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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.04s ===============================
"""