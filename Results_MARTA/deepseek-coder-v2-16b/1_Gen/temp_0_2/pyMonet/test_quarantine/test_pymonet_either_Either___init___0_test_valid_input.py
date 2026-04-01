
from pymonet.either import Either, Left, Right  # Importing from module 'pymonet.either'

def test_valid_input():
    mock_either = Either(Right('success'))
    assert isinstance(mock_either, Either)
    assert mock_either.value == 'success'

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

pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        mock_either = Either(Right('success'))
        assert isinstance(mock_either, Either)
>       assert mock_either.value == 'success'
E       AssertionError: assert <pymonet.either.Right object at 0x7fce2b91d0d0> == 'success'
E        +  where <pymonet.either.Right object at 0x7fce2b91d0d0> = <pymonet.either.Either object at 0x7fce2b91fc10>.value

pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0_test_valid_input.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""