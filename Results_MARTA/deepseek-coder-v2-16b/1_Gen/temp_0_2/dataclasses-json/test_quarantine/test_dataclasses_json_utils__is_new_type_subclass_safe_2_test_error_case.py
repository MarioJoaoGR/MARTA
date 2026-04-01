
import pytest
from dataclasses_json.utils import _is_new_type_subclass_safe

def test_error_case():
    class A: pass
    class B(A): pass
    class C: pass
    class D(C): __supertype__ = C

    # Test valid subclass relationship
    assert _is_new_type_subclass_safe(B, A) == True

    # Test invalid subclass relationship
    with pytest.raises(TypeError):
        assert _is_new_type_subclass_safe(C, D)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        class A: pass
        class B(A): pass
        class C: pass
        class D(C): __supertype__ = C
    
        # Test valid subclass relationship
        assert _is_new_type_subclass_safe(B, A) == True
    
        # Test invalid subclass relationship
        with pytest.raises(TypeError):
>           assert _is_new_type_subclass_safe(C, D)
E           AssertionError: assert False
E            +  where False = _is_new_type_subclass_safe(<class 'Test4DT_tests.test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_error_case.test_error_case.<locals>.C'>, <class 'Test4DT_tests.test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_error_case.test_error_case.<locals>.D'>)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_error_case.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_error_case.py::test_error_case
============================== 1 failed in 0.03s ===============================
"""