
import pytest
from flutes.network import _download_from_google_drive

def test_invalid_input():
    with pytest.raises(Exception):
        # Invalid URL should raise an Exception
        _download_from_google_drive("invalid_url", "myfile.txt", "./downloads")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_invalid_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.46s ===============================
"""