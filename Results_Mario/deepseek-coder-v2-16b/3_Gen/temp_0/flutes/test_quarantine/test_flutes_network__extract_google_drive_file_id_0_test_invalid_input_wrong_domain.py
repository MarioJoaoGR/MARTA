
import pytest
from flutes.network import _extract_google_drive_file_id

def test_invalid_input_wrong_domain():
    # Test with a URL that does not belong to Google Drive
    url = "https://example.com/wrong/url"
    assert _extract_google_drive_file_id(url) == ''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input_wrong_domain.py F [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_input_wrong_domain ________________________

    def test_invalid_input_wrong_domain():
        # Test with a URL that does not belong to Google Drive
        url = "https://example.com/wrong/url"
>       assert _extract_google_drive_file_id(url) == ''
E       AssertionError: assert 'tps:' == ''
E         
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input_wrong_domain.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input_wrong_domain.py::test_invalid_input_wrong_domain
============================== 1 failed in 0.10s ===============================
"""