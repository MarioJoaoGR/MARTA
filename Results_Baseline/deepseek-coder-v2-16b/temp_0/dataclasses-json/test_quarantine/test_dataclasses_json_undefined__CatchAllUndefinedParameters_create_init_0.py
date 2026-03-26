
# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass
import inspect
import functools

# Import the function to be tested
from dataclasses_json.undefined import create_init

@dataclass
class ExampleDataclass:
    param1: int
    param2: str = None

def test_create_init_with_dataclass():
    modified_init = create_init(ExampleDataclass)
    example_instance = modified_init(param1=1, param3="test")  # Corrected to match the dataclass definition
    assert hasattr(example_instance, 'param1') and example_instance.param1 == 1
    assert hasattr(example_instance, 'param2') and example_instance.param2 is None
    assert not hasattr(example_instance, 'param3')  # Corrected to match the assertion logic

def test_create_init_with_custom_class():
    class MyClass:
        def __init__(self, a, b=None, c=0):
            self.a = a
            self.b = b
            self.c = c
    
    modified_init = create_init(MyClass)
    instance = modified_init(a=1, b=2, d="extra")  # Corrected to match the custom class definition
    assert hasattr(instance, 'a') and instance.a == 1
    assert hasattr(instance, 'b') and instance.b == 2
    assert not hasattr(instance, 'c')
    assert not hasattr(instance, 'd')  # Corrected to match the assertion logic

def test_create_init_with_existing_instance():
    @dataclass
    class ExampleDataclass:
        param1: int
        param2: str = None
    
    dataclass_instance = ExampleDataclass(param1=1)
    modified_init = create_init(ExampleDataclass)
    instance = modified_init(dataclass_instance, param2="test", extra_param="extra")  # Corrected to match the existing instance usage
    assert hasattr(instance, 'param1') and instance.param1 == 1
    assert hasattr(instance, 'param2') and instance.param2 == "test"
    assert not hasattr(instance, 'extra_param')  # Corrected to match the assertion logic

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0.py:9:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)

"""