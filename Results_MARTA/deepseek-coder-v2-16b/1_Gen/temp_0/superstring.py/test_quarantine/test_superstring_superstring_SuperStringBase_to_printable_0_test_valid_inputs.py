
from superstring.superstring import SuperStringBase

def test_valid_inputs():
    obj = SuperStringBase()
    assert obj.to_printable() == "The quick brown fox jumps over the lazy dog"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        obj = SuperStringBase()
>       assert obj.to_printable() == "The quick brown fox jumps over the lazy dog"
E       AssertionError: assert None == 'The quick brown fox jumps over the lazy dog'
E        +  where None = to_printable()
E        +    where to_printable = <superstring.superstring.SuperStringBase object at 0x7f74839b9b10>.to_printable

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_valid_inputs.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.04s ===============================
"""