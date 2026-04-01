
import pytest
from pytutils.enum import LookupEnumMixin
import enum

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def test_valid_input():
    # Test the function with a valid enumeration class
    result = LookupEnumMixin.lookup_by_name(Color)
    expected_result = {
        'RED': Color.RED,
        'GREEN': Color.GREEN,
        'BLUE': Color.BLUE
    }
    assert result == expected_result

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

pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test the function with a valid enumeration class
>       result = LookupEnumMixin.lookup_by_name(Color)

pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_valid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/props.py:10: in __get__
    return self.f(owner)
pytutils/pytutils/props.py:49: in _lazyclassprop
    setattr(cls, attr_name, fn(cls))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'pytutils.enum.LookupEnumMixin'>

    @lazyclassproperty
    def lookup_by_name(cls):
>       return cls.__members__
E       AttributeError: type object 'LookupEnumMixin' has no attribute '__members__'

pytutils/pytutils/enum.py:7: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""