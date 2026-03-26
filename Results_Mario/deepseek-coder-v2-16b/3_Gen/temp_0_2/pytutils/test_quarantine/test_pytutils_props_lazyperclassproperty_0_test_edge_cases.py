
import pytest
from unittest.mock import patch, MagicMock
from pytutils.props import lazyperclassproperty

# Define the classes with the lazy property
class MyClass1:
    pass

class MyClass2(MyClass1):
    pass

@lazyperclassproperty
def cached_instance(cls):
    return cls()

MyClass1.cached_instance = cached_instance
MyClass2.cached_instance = cached_instance

# Test cases
def test_lazyperclassproperty():
    with patch('pytutils.props.lazyperclassproperty') as mock_lazyperclassproperty:
        # Mock the behavior of lazyperclassproperty to return a new instance each time
        mock_lazyperclassproperty.return_value = lambda cls: MagicMock()
        
        # First access should create a new instance
        assert isinstance(MyClass1.cached_instance, MagicMock)
        assert not hasattr(MyClass2, 'cached_instance')  # MyClass2 should not have its own cached instance yet
        
        # Accessing MyClass2's property should create a new instance
        assert isinstance(MyClass2.cached_instance, MagicMock)
        
        # Both classes should now have their own instances
        assert hasattr(MyClass1, 'cached_instance')
        assert hasattr(MyClass2, 'cached_instance')

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

pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
__________________________ test_lazyperclassproperty ___________________________

    def test_lazyperclassproperty():
        with patch('pytutils.props.lazyperclassproperty') as mock_lazyperclassproperty:
            # Mock the behavior of lazyperclassproperty to return a new instance each time
            mock_lazyperclassproperty.return_value = lambda cls: MagicMock()
    
            # First access should create a new instance
>           assert isinstance(MyClass1.cached_instance, MagicMock)
E           assert False
E            +  where False = isinstance(<Test4DT_tests.test_pytutils_props_lazyperclassproperty_0_test_edge_cases.MyClass1 object at 0x7f6708dcc550>, MagicMock)
E            +    where <Test4DT_tests.test_pytutils_props_lazyperclassproperty_0_test_edge_cases.MyClass1 object at 0x7f6708dcc550> = MyClass1.cached_instance

pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_edge_cases.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_edge_cases.py::test_lazyperclassproperty
============================== 1 failed in 0.07s ===============================
"""