
import pytest
from flutes.network import _download_from_google_drive, _extract_google_drive_file_id
from unittest.mock import patch

@pytest.mark.parametrize("url, filename, path, bar_fn", [
    (None, "myfile.txt", "/home/user", None),
])
def test_none_inputs(url, filename, path, bar_fn):
    with pytest.raises(TypeError):
        _download_from_google_drive(url, filename, path, bar_fn)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_none_inputs.py F [100%]

=================================== FAILURES ===================================
______________ test_none_inputs[None-myfile.txt-/home/user-None] _______________

url = None, filename = 'myfile.txt', path = '/home/user', bar_fn = None

    @pytest.mark.parametrize("url, filename, path, bar_fn", [
        (None, "myfile.txt", "/home/user", None),
    ])
    def test_none_inputs(url, filename, path, bar_fn):
        with pytest.raises(TypeError):
>           _download_from_google_drive(url, filename, path, bar_fn)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_none_inputs.py:11: 
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
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_none_inputs.py::test_none_inputs[None-myfile.txt-/home/user-None]
============================== 1 failed in 0.12s ===============================

"""