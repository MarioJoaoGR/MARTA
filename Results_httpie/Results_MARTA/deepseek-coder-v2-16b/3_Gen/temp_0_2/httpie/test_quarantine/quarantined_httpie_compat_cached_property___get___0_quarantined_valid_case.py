
import pytest
from httpie.compat import cached_property
from unittest.mock import patch

class MyClass:
    def __init__(self, value):
        self.value = value
    
    @cached_property
    def expensive_calculation(self):
        print("Performing expensive calculation")
        return self.value * 2

def test_valid_case():
    obj = MyClass(10)
    
    with patch.object(MyClass, 'expensive_calculation', lambda x: 20):
        assert obj.expensive_calculation == 20

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_cached_property___get___0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        obj = MyClass(10)
    
        with patch.object(MyClass, 'expensive_calculation', lambda x: 20):
>           assert obj.expensive_calculation == 20
E           assert <lambda> == 20
E            +  where <lambda> = <test_httpie_compat_cached_property___get___0_test_valid_case.MyClass object at 0x7f1d4ad03b90>.expensive_calculation

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_cached_property___get___0_test_valid_case.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_cached_property___get___0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.14s ===============================
"""