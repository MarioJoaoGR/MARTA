
import pytest
from pytutils.props import lazyperclassproperty

# Define a mock function to simulate expensive calculations
def expensive_calculation(cls):
    return cls()

@pytest.fixture
def define_classes():
    class MyClass1:
        pass

    class MyClass2(MyClass1):
        pass

    # Apply the lazyperclassproperty decorator to a method in the classes
    @lazyperclassproperty(expensive_calculation)
    def cached_instance(cls):
        return cls()

    MyClass1.cached_instance = cached_instance
    MyClass2.cached_instance = cached_instance

    return MyClass1, MyClass2

def test_invalid_inputs(define_classes):
    MyClass1, MyClass2 = define_classes

    # Test that the property is correctly initialized for each class
    assert isinstance(MyClass1.cached_instance, MyClass1)
    assert isinstance(MyClass2.cached_instance, MyClass2)
    assert MyClass1.cached_instance is not MyClass2.cached_instance

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_invalid_inputs.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_invalid_inputs _____________________

    @pytest.fixture
    def define_classes():
        class MyClass1:
            pass
    
        class MyClass2(MyClass1):
            pass
    
        # Apply the lazyperclassproperty decorator to a method in the classes
>       @lazyperclassproperty(expensive_calculation)
E       TypeError: 'roclassproperty' object is not callable

pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_invalid_inputs.py:18: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_invalid_inputs.py::test_invalid_inputs
=============================== 1 error in 0.07s ===============================
"""