
# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass
import inspect
import functools

# Assuming the module name is 'dataclasses_json.undefined' and the function is imported correctly
from dataclasses_json.undefined import create_init

@dataclass
class MyClass:
    a: int
    b: str = None

def test_create_init_basic():
    modified_init = create_init(MyClass)
    MyClass.__init__ = modified_init
    
    # Test with additional unknown parameter
    instance = MyClass(a=1, c=2)
    assert hasattr(instance, 'c')
    assert getattr(instance, 'c') == 2

@dataclass
class UserData:
    name: str
    age: int

def test_create_init_with_dataclass():
    modified_init = create_init(UserData)
    UserData.__init__ = modified_init
    
    # Test with additional unknown parameter
    user = UserData(name="John Doe", unknown_param=42)
    assert hasattr(user, 'unknown_param')
    assert getattr(user, 'unknown_param') == 42

@dataclass
class ThirdPartyDataClass:
    field1: str
    field2: int

def test_create_init_with_third_party_dataclass():
    modified_init = create_init(ThirdPartyDataClass)
    ThirdPartyDataClass.__init__ = modified_init
    
    # Test with additional unknown parameter
    third_party_instance = ThirdPartyDataClass(field1="value", unknown_param=3.14)
    assert hasattr(third_party_instance, 'unknown_param')
    assert getattr(third_party_instance, 'unknown_param') == 3.14

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0.py:9:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)

"""