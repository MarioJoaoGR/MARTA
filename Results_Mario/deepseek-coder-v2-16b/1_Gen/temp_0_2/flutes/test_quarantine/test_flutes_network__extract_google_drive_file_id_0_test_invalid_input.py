
import re
import pytest
from flutes.network import _extract_google_drive_file_id

@pytest.mark.parametrize("invalid_url", [
    "https://example.com/randomstring",
    "https://drive.google.com/file/d/",
    "https://drive.google.com/open?id=invalid_id"
])
def test_invalid_input(invalid_url):
    assert _extract_google_drive_file_id(invalid_url) == ''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input.py F [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
_____________ test_invalid_input[https://example.com/randomstring] _____________

invalid_url = 'https://example.com/randomstring'

    @pytest.mark.parametrize("invalid_url", [
        "https://example.com/randomstring",
        "https://drive.google.com/file/d/",
        "https://drive.google.com/open?id=invalid_id"
    ])
    def test_invalid_input(invalid_url):
>       assert _extract_google_drive_file_id(invalid_url) == ''
E       AssertionError: assert 'tps:' == ''
E         
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input.py:12: AssertionError
_______ test_invalid_input[https://drive.google.com/open?id=invalid_id] ________

invalid_url = 'https://drive.google.com/open?id=invalid_id'

    @pytest.mark.parametrize("invalid_url", [
        "https://example.com/randomstring",
        "https://drive.google.com/file/d/",
        "https://drive.google.com/open?id=invalid_id"
    ])
    def test_invalid_input(invalid_url):
>       assert _extract_google_drive_file_id(invalid_url) == ''
E       AssertionError: assert 'tps:' == ''
E         
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input.py::test_invalid_input[https:/example.com/randomstring]
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input.py::test_invalid_input[https:/drive.google.com/open?id=invalid_id]
========================= 2 failed, 1 passed in 0.10s ==========================
"""