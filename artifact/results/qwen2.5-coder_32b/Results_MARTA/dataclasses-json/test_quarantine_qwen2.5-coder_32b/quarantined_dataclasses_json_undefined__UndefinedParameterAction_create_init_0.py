
import pytest
from dataclasses_json.undefined import _UndefinedParameterAction

def create_init(obj) -> callable:
    """
    Returns the `__init__` method of the given object.
    """
    return obj.__init__

class TestCreateInit:

    def test_create_init_with_class(self):
        """Test that create_init returns the __init__ method of a class."""
        class MyClass:
            def __init__(self, value):
                self.value = value

        init_method = create_init(MyClass)
        assert init_method is MyClass.__init__

    def test_create_init_with_instance(self):
        """Test that create_init returns the __init__ method of an instance's class."""
        class AnotherClass:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        another_instance = AnotherClass("Alice", 30)
        init_method = create_init(another_instance)
        assert init_method is AnotherClass.__init__

    def test_create_init_with_dataclass(self):
        """Test that create_init returns the __init__ method of a dataclass instance's class."""
        from dataclasses import dataclass

        @dataclass
        class Person:
            name: str
            age: int

        person_instance = Person("Charlie", 35)
        init_method = create_init(person_instance)
        assert init_method is Person.__init__

    def test_create_init_with_undefined_parameter_action(self):
        """Test that create_init returns the __init__ method of _UndefinedParameterAction."""
        init_method = create_init(_UndefinedParameterAction)
        assert init_method is _UndefinedParameterAction.__init__
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.py . [ 25%]
FF.                                                                      [100%]

=================================== FAILURES ===================================
________________ TestCreateInit.test_create_init_with_instance _________________

self = <test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.TestCreateInit object at 0x7fef7bccfee0>

    def test_create_init_with_instance(self):
        """Test that create_init returns the __init__ method of an instance's class."""
        class AnotherClass:
            def __init__(self, name, age):
                self.name = name
                self.age = age
    
        another_instance = AnotherClass("Alice", 30)
        init_method = create_init(another_instance)
>       assert init_method is AnotherClass.__init__
E       AssertionError: assert __init__ is <function TestCreateInit.test_create_init_with_instance.<locals>.AnotherClass.__init__ at 0x7fef7bce95a0>
E        +  where <function TestCreateInit.test_create_init_with_instance.<locals>.AnotherClass.__init__ at 0x7fef7bce95a0> = <class 'test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.TestCreateInit.test_create_init_with_instance.<locals>.AnotherClass'>.__init__

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.py:31: AssertionError
________________ TestCreateInit.test_create_init_with_dataclass ________________

self = <test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.TestCreateInit object at 0x7fef7bcfc0a0>

    def test_create_init_with_dataclass(self):
        """Test that create_init returns the __init__ method of a dataclass instance's class."""
        from dataclasses import dataclass
    
        @dataclass
        class Person:
            name: str
            age: int
    
        person_instance = Person("Charlie", 35)
        init_method = create_init(person_instance)
>       assert init_method is Person.__init__
E       AssertionError: assert __init__ is <function TestCreateInit.test_create_init_with_dataclass.<locals>.Person.__init__ at 0x7fef7bceab90>
E        +  where <function TestCreateInit.test_create_init_with_dataclass.<locals>.Person.__init__ at 0x7fef7bceab90> = <class 'test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.TestCreateInit.test_create_init_with_dataclass.<locals>.Person'>.__init__

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.py:44: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.py::TestCreateInit::test_create_init_with_instance
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0.py::TestCreateInit::test_create_init_with_dataclass
========================= 2 failed, 2 passed in 0.08s ==========================
"""