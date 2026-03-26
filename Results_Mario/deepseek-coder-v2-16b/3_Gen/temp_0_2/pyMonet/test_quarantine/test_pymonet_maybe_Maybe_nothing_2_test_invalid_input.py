
from pymonet.maybe import Maybe

def test_invalid_input():
    # Test when is_nothing is True but value is provided
    try:
        maybe_invalid = Maybe(value=42, is_nothing=True)
    except TypeError as e:
        assert str(e) == "is_nothing must be a boolean"
    else:
        raise AssertionError("Expected a TypeError")

    # Test when is_nothing is False but value is not provided
    try:
        maybe_invalid = Maybe(value=None, is_nothing=False)
    except ValueError as e:
        assert str(e) == "Value must be provided if is_nothing is False"
    else:
        raise AssertionError("Expected a ValueError")

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_nothing_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test when is_nothing is True but value is provided
        try:
            maybe_invalid = Maybe(value=42, is_nothing=True)
        except TypeError as e:
            assert str(e) == "is_nothing must be a boolean"
        else:
>           raise AssertionError("Expected a TypeError")
E           AssertionError: Expected a TypeError

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_nothing_2_test_invalid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_nothing_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""