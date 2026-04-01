
import pytest
from string_utils.manipulation import __RomanNumbers

def test_edge_case():
    # Test with a valid Roman numeral sign
    assert __RomanNumbers.__index_for_sign('V') == 1
    
    # Test with an invalid Roman numeral sign
    with pytest.raises(ValueError) as excinfo:
        __RomanNumbers.__index_for_sign('Z')
    assert str(excinfo.value) == 'Invalid token found: "Z"'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Test with a valid Roman numeral sign
>       assert __RomanNumbers.__index_for_sign('V') == 1
E       AttributeError: type object '__RomanNumbers' has no attribute '__index_for_sign'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_edge_case.py:7: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.03s ===============================

"""