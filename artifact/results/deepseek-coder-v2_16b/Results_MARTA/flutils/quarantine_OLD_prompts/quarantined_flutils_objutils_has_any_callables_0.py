
import pytest
from flutils.objutils import has_any_callables, has_any_attrs
from unittest.mock import patch



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_has_any_callables_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        class MyClass:
            def method1(self):
                pass
    
            @staticmethod
            def method2():
                pass
    
        obj = MyClass()
        assert has_any_callables(obj, 'method1', 'method2') is True
>       assert has_any_callables(obj, 'method1', 'non_existent_attr') is False
E       AssertionError: assert True is False
E        +  where True = has_any_callables(<test_flutils_objutils_has_any_callables_0.test_valid_case.<locals>.MyClass object at 0x7f1eeb6a2c50>, 'method1', 'non_existent_attr')

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_has_any_callables_0.py:17: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with patch('flutils.objutils.has_any_attrs', return_value=False):
            obj = None
            attrs = ('method1', 'getattr')
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_has_any_callables_0.py:23: Failed
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        obj = 123
        attrs = ('method1', 'getattr')
        with patch('flutils.objutils.has_any_attrs', return_value=False):
>           with pytest.raises(AttributeError):
E           Failed: DID NOT RAISE <class 'AttributeError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_has_any_callables_0.py:30: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_has_any_callables_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_has_any_callables_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_has_any_callables_0.py::test_invalid_input
============================== 3 failed in 0.05s ===============================
"""