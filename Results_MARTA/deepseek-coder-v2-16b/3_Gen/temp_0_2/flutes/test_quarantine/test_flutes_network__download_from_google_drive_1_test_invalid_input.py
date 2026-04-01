
import pytest
from flutes.network import _download_from_google_drive

@pytest.mark.parametrize("url, filename, path", [
    ("invalid_url", "myfile.txt", "./downloads")
])
def test_invalid_input(url, filename, path):
    with pytest.raises(Exception):
        _download_from_google_drive(url, filename, path)

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

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
____________ test_invalid_input[invalid_url-myfile.txt-./downloads] ____________

url = 'invalid_url', filename = 'myfile.txt', path = './downloads'

    @pytest.mark.parametrize("url, filename, path", [
        ("invalid_url", "myfile.txt", "./downloads")
    ])
    def test_invalid_input(url, filename, path):
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_invalid_input.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_invalid_input.py::test_invalid_input[invalid_url-myfile.txt-./downloads]
============================== 1 failed in 0.42s ===============================
"""