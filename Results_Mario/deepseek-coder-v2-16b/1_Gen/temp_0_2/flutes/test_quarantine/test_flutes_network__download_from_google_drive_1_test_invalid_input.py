
import pytest
from flutes.network import _download_from_google_drive, _extract_google_drive_file_id
import requests
import os
from unittest.mock import patch

@pytest.mark.parametrize("url, filename, path", [
    (None, "file.txt", "./downloads"),  # Missing URL
    ("https://example.com/valid-link", None, "./downloads"),  # Missing filename
    ("https://example.com/valid-link", "file.txt", None)  # Missing path
])
def test_invalid_input(url, filename, path):
    with pytest.raises(TypeError):
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
collected 3 items

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_invalid_input.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
________________ test_invalid_input[None-file.txt-./downloads] _________________

url = None, filename = 'file.txt', path = './downloads'

    @pytest.mark.parametrize("url, filename, path", [
        (None, "file.txt", "./downloads"),  # Missing URL
        ("https://example.com/valid-link", None, "./downloads"),  # Missing filename
        ("https://example.com/valid-link", "file.txt", None)  # Missing path
    ])
    def test_invalid_input(url, filename, path):
        with pytest.raises(TypeError):
>           _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_invalid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/network.py:128: in _download_from_google_drive
    file_id = _extract_google_drive_file_id(url)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

url = None

    def _extract_google_drive_file_id(url: str) -> str:
        # The ID is the first segment after `/d/`.
>       url_suffix = url[url.find('/d/') + 3:]
E       AttributeError: 'NoneType' object has no attribute 'find'

flutes/flutes/network.py:114: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_invalid_input.py::test_invalid_input[None-file.txt-./downloads]
========================= 1 failed, 2 passed in 0.70s ==========================
"""