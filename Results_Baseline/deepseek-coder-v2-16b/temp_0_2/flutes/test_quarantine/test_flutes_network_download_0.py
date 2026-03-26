
# Module: flutes.network
import pytest
from flutes.io import download
import os
import tempfile
import tarfile
import zipfile
from tqdm import tqdm
import functools

# Helper function to remove the file after the test
@pytest.fixture(autouse=True)
def cleanup():
    yield  # Run the tests
    if os.path.exists('test_downloaded_file'):
        os.remove('test_downloaded_file')
    if os.path.exists('test_extracted_dir'):
        for file in os.listdir('test_extracted_dir'):
            os.remove(os.path.join('test_extracted_dir', file))
        os.rmdir('test_extracted_dir')

def test_download_basic():
    url = 'http://example.com/file.txt'
    path = download(url)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting Test4DT_tests/test_flutes_network_download_0.py _______
ImportError while importing test module '/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_network_download_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
flutes/Test4DT_tests/test_flutes_network_download_0.py:4: in <module>
    from flutes.io import download
E   ImportError: cannot import name 'download' from 'flutes.io' (/projects/F202407648IACDCF2/mario/flutes/flutes/io.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_network_download_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""