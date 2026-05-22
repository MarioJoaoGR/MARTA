
import unittest
from httpie.compat import cached_property

class TestCachedProperty(unittest.TestCase):
    def test_edge_case(self):
        class MyClass:
            def __init__(self):
                self._name = None
            
            @cached_property
            def name(self):
                return "example"
            
            @name.setter
            def name(self, value):
                self._name = value
        
        obj = MyClass()
        self.assertEqual(obj.name, "example")
        obj.name = "test_value"
        self.assertEqual(obj._name, "test_value")

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

httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___6_test_edge_case.py F [100%]

=================================== FAILURES ===================================
______________________ TestCachedProperty.test_edge_case _______________________

self = <Test4DT_tests_codestral.test_httpie_compat_cached_property___set_name___6_test_edge_case.TestCachedProperty testMethod=test_edge_case>

    def test_edge_case(self):
>       class MyClass:

httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___6_test_edge_case.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    class MyClass:
        def __init__(self):
            self._name = None
    
        @cached_property
        def name(self):
            return "example"
    
>       @name.setter
E       AttributeError: 'cached_property' object has no attribute 'setter'

httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___6_test_edge_case.py:15: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___6_test_edge_case.py::TestCachedProperty::test_edge_case
============================== 1 failed in 0.14s ===============================
"""