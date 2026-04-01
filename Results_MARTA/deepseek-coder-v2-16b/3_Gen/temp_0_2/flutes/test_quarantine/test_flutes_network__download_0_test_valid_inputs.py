
import os
import urllib.request
from typing import Optional
from flutes.network import _download, BarFn
from unittest.mock import MagicMock
import pytest

@pytest.mark.parametrize("url, filename, path", [
    ("http://example.com/file.zip", "file.zip", "/path/to/save"),
    ("https://example.com/file.zip", "file.zip", "/path/to/save")
])
def test_valid_inputs(url, filename, path):
    # Mock the bar_fn if provided
    bar_fn = MagicMock()
    
    # Call the function with valid inputs
    result = _download(url, filename, path, bar_fn)
    
    # Check that the file was downloaded to the correct path
    expected_filepath = os.path.join(path, filename)
    assert result == expected_filepath

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

flutes/Test4DT_tests/test_flutes_network__download_0_test_valid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____ test_valid_inputs[http://example.com/file.zip-file.zip-/path/to/save] _____

url = 'http://example.com/file.zip', filename = 'file.zip'
path = '/path/to/save'

    @pytest.mark.parametrize("url, filename, path", [
        ("http://example.com/file.zip", "file.zip", "/path/to/save"),
        ("https://example.com/file.zip", "file.zip", "/path/to/save")
    ])
    def test_valid_inputs(url, filename, path):
        # Mock the bar_fn if provided
        bar_fn = MagicMock()
    
        # Call the function with valid inputs
>       result = _download(url, filename, path, bar_fn)

flutes/Test4DT_tests/test_flutes_network__download_0_test_valid_inputs.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
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

self = <urllib.request.HTTPDefaultErrorHandler object at 0x7fde1d705c90>
req = <urllib.request.Request object at 0x7fde1d7064d0>
fp = <http.client.HTTPResponse object at 0x7fde1d741fc0>, code = 404
msg = 'Not Found', hdrs = <http.client.HTTPMessage object at 0x7fde1d707710>

    def http_error_default(self, req, fp, code, msg, hdrs):
>       raise HTTPError(req.full_url, code, msg, hdrs, fp)
E       urllib.error.HTTPError: HTTP Error 404: Not Found

/usr/local/lib/python3.11/urllib/request.py:643: HTTPError
____ test_valid_inputs[https://example.com/file.zip-file.zip-/path/to/save] ____

url = 'https://example.com/file.zip', filename = 'file.zip'
path = '/path/to/save'

    @pytest.mark.parametrize("url, filename, path", [
        ("http://example.com/file.zip", "file.zip", "/path/to/save"),
        ("https://example.com/file.zip", "file.zip", "/path/to/save")
    ])
    def test_valid_inputs(url, filename, path):
        # Mock the bar_fn if provided
        bar_fn = MagicMock()
    
        # Call the function with valid inputs
>       result = _download(url, filename, path, bar_fn)

flutes/Test4DT_tests/test_flutes_network__download_0_test_valid_inputs.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
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

self = <urllib.request.HTTPDefaultErrorHandler object at 0x7fde1d705c90>
req = <urllib.request.Request object at 0x7fde1da06f10>
fp = <http.client.HTTPResponse object at 0x7fde1d741960>, code = 404
msg = 'Not Found', hdrs = <http.client.HTTPMessage object at 0x7fde1d6d7090>

    def http_error_default(self, req, fp, code, msg, hdrs):
>       raise HTTPError(req.full_url, code, msg, hdrs, fp)
E       urllib.error.HTTPError: HTTP Error 404: Not Found

/usr/local/lib/python3.11/urllib/request.py:643: HTTPError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__download_0_test_valid_inputs.py::test_valid_inputs[http:/example.com/file.zip-file.zip-/path/to/save]
FAILED flutes/Test4DT_tests/test_flutes_network__download_0_test_valid_inputs.py::test_valid_inputs[https:/example.com/file.zip-file.zip-/path/to/save]
============================== 2 failed in 0.42s ===============================
"""