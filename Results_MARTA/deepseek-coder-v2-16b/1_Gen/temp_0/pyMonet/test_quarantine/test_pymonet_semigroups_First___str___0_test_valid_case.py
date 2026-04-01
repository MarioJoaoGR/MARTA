
from pymonet.semigroups import First  # Assuming this module contains the First class definition

def test_valid_case():
    first1 = First(5)
    first2 = First(10)
    combined_first = first1 + first2  # This should return First(5), since it always returns the first value.
    
    assert isinstance(combined_first, First)
    assert combined_first.value == 5

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        first1 = First(5)
        first2 = First(10)
>       combined_first = first1 + first2  # This should return First(5), since it always returns the first value.
E       TypeError: unsupported operand type(s) for +: 'First' and 'First'

pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___0_test_valid_case.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.06s ===============================
"""