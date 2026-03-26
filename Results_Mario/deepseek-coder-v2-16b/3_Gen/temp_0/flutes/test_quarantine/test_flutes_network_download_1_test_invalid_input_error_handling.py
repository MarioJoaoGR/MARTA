
import pytest
from flutes.network import download
from unittest.mock import patch, MagicMock
import os
import tempfile
import tarfile
import zipfile

@pytest.mark.parametrize("url", [None])
def test_invalid_input_error_handling(url):
    with pytest.raises(TypeError) as excinfo:
        download(url, save_dir="downloads")
    assert "missing 1 required positional argument" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_network_download_1_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
___________________ test_invalid_input_error_handling[None] ____________________

url = None

    @pytest.mark.parametrize("url", [None])
    def test_invalid_input_error_handling(url):
        with pytest.raises(TypeError) as excinfo:
            download(url, save_dir="downloads")
>       assert "missing 1 required positional argument" in str(excinfo.value)
E       assert 'missing 1 required positional argument' in "argument of type 'NoneType' is not iterable"
E        +  where "argument of type 'NoneType' is not iterable" = str(TypeError("argument of type 'NoneType' is not iterable"))
E        +    where TypeError("argument of type 'NoneType' is not iterable") = <ExceptionInfo TypeError("argument of type 'NoneType' is not iterable") tblen=2>.value

flutes/Test4DT_tests/test_flutes_network_download_1_test_invalid_input_error_handling.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network_download_1_test_invalid_input_error_handling.py::test_invalid_input_error_handling[None]
============================== 1 failed in 0.10s ===============================

"""