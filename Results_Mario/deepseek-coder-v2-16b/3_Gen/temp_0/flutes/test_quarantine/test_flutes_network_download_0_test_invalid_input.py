
import pytest
from flutes.network import download
import os
import tempfile
import tarfile
import zipfile
import functools
from tqdm import tqdm

@pytest.mark.parametrize("url", ["http://invalid-scheme//example.com", "https://drive.google.com/invalid_path"])
def test_invalid_input(url):
    with pytest.raises(Exception):
        download(url)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_network_download_0_test_invalid_input.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________ test_invalid_input[https://drive.google.com/invalid_path] ___________

url = 'https://drive.google.com/invalid_path'

    @pytest.mark.parametrize("url", ["http://invalid-scheme//example.com", "https://drive.google.com/invalid_path"])
    def test_invalid_input(url):
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

flutes/Test4DT_tests/test_flutes_network_download_0_test_invalid_input.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network_download_0_test_invalid_input.py::test_invalid_input[https:/drive.google.com/invalid_path]
========================= 1 failed, 1 passed in 0.14s ==========================
"""