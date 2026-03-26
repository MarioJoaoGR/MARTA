
from pymonet.semigroups import First

def test_valid_case():
    first1 = First(value=1)
    first2 = First(value=2)
    combined = first1 + first2  # This should return an instance of First with the value from first1, which is 1.
    assert combined.value == 1

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
        first1 = First(value=1)
        first2 = First(value=2)
>       combined = first1 + first2  # This should return an instance of First with the value from first1, which is 1.
E       TypeError: unsupported operand type(s) for +: 'First' and 'First'

pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___0_test_valid_case.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.06s ===============================
"""