
from pymonet.maybe import Maybe

def test_invalid_input():
    # Test invalid input where value is provided but is_nothing is True
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing is True
    assert maybe_none.value is None

    # Test invalid input where value is not provided but is_nothing is False
    try:
        maybe_empty = Maybe(value=42, is_nothing=False)
        assert False, "Expected a ValueError for invalid input"
    except ValueError as e:
        assert str(e) == "Value must be provided when is_nothing is False"

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_just_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test invalid input where value is provided but is_nothing is True
        maybe_none = Maybe(value=None, is_nothing=True)
        assert maybe_none.is_nothing is True
>       assert maybe_none.value is None
E       AttributeError: 'Maybe' object has no attribute 'value'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_just_2_test_invalid_input.py:8: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_just_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""