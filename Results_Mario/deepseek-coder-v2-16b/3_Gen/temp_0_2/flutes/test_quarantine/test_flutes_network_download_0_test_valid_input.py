
import pytest
from unittest.mock import patch
from flutes.network import download
from pathlib import Path
import tempfile
import os
import tarfile
import zipfile

@pytest.mark.parametrize("url, save_dir, filename", [
    ("http://example.com/file.zip", None, "file.zip"),
    ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view", Path(tempfile.gettempdir()), "file_from_drive.zip")
])
def test_valid_input(url, save_dir, filename):
    with patch('flutes.network._download') as mock_download:
        # Mock the behavior of _download and _download_from_google_drive to avoid actual network calls
        if 'drive.google.com' in url:
            mock_download.return_value = Path(save_dir) / filename if save_dir else Path(filename)
        else:
            mock_download.return_value = Path(tempfile.gettempdir()) / filename
    
    result = download(url, save_dir, filename)
    assert os.path.exists(result), f"File {result} does not exist."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_network_download_0_test_valid_input.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_________ test_valid_input[http://example.com/file.zip-None-file.zip] __________

url = 'http://example.com/file.zip', save_dir = None, filename = 'file.zip'

    @pytest.mark.parametrize("url, save_dir, filename", [
        ("http://example.com/file.zip", None, "file.zip"),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view", Path(tempfile.gettempdir()), "file_from_drive.zip")
    ])
    def test_valid_input(url, save_dir, filename):
        with patch('flutes.network._download') as mock_download:
            # Mock the behavior of _download and _download_from_google_drive to avoid actual network calls
            if 'drive.google.com' in url:
                mock_download.return_value = Path(save_dir) / filename if save_dir else Path(filename)
            else:
                mock_download.return_value = Path(tempfile.gettempdir()) / filename
    
>       result = download(url, save_dir, filename)

flutes/Test4DT_tests/test_flutes_network_download_0_test_valid_input.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/network.py:72: in download
    filepath = _download(url, filename, save_dir_str, bar_fn)
flutes/flutes/network.py:106: in _download
    filepath, _ = urllib.request.urlretrieve(url, filepath, _progress_hook)
/usr/local/lib/python3.11/urllib/request.py:241: in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
/usr/local/lib/python3.11/urllib/request.py:216: in urlopen
    return opener.open(url, data, timeout)
/usr/local/lib/python3.11/urllib/request.py:525: in open
    response = meth(req, response)
/usr/local/lib/python3.11/urllib/request.py:634: in http_response
    response = self.parent.error(
/usr/local/lib/python3.11/urllib/request.py:563: in error
    return self._call_chain(*args)
/usr/local/lib/python3.11/urllib/request.py:496: in _call_chain
    result = func(*args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <urllib.request.HTTPDefaultErrorHandler object at 0x7f55832bd8d0>
req = <urllib.request.Request object at 0x7f55832bf490>
fp = <http.client.HTTPResponse object at 0x7f5583273430>, code = 404
msg = 'Not Found', hdrs = <http.client.HTTPMessage object at 0x7f5583295ed0>

    def http_error_default(self, req, fp, code, msg, hdrs):
>       raise HTTPError(req.full_url, code, msg, hdrs, fp)
E       urllib.error.HTTPError: HTTP Error 404: Not Found

/usr/local/lib/python3.11/urllib/request.py:643: HTTPError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network_download_0_test_valid_input.py::test_valid_input[http:/example.com/file.zip-None-file.zip]
========================= 1 failed, 1 passed in 0.23s ==========================
"""