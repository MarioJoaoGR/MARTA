
import pytest
from flutes.network import _download_from_google_drive
import requests
import os
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("url", ["invalid_url"])
def test_invalid_url(url):
    with pytest.raises(Exception) as e:
        _download_from_google_drive(url, "myfile.txt", "/home/user")
    assert str(e.value) == "Invalid URL provided"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_invalid_url.py F [100%]

=================================== FAILURES ===================================
________________________ test_invalid_url[invalid_url] _________________________

url = 'invalid_url'

    @pytest.mark.parametrize("url", ["invalid_url"])
    def test_invalid_url(url):
        with pytest.raises(Exception) as e:
            _download_from_google_drive(url, "myfile.txt", "/home/user")
>       assert str(e.value) == "Invalid URL provided"
E       assert "[Errno 2] No...r/myfile.txt'" == 'Invalid URL provided'
E         
E         - Invalid URL provided
E         + [Errno 2] No such file or directory: '/home/user/myfile.txt'

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_invalid_url.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_invalid_url.py::test_invalid_url[invalid_url]
============================== 1 failed in 0.45s ===============================

"""