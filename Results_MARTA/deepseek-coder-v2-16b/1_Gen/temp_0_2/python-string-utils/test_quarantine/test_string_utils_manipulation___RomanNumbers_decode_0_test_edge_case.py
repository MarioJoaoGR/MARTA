
import pytest
from string_utils.manipulation import __RomanNumbers

def test_edge_case():
    with pytest.raises(ValueError):
        assert __RomanNumbers().decode('')
    
    with pytest.raises(TypeError):
        assert __RomanNumbers().decode(123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with pytest.raises(ValueError):
            assert __RomanNumbers().decode('')
    
        with pytest.raises(TypeError):
>           assert __RomanNumbers().decode(123)

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_edge_case.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'string_utils.manipulation.__RomanNumbers'>, input_string = 123

    @classmethod
    def decode(cls, input_string: str) -> int:
        if not is_full_string(input_string):
>           raise ValueError('Input must be a non empty string')
E           ValueError: Input must be a non empty string

python-string-utils/string_utils/manipulation.py:119: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.03s ===============================
"""