
import pytest
import urllib.request
from flutes.network import _download
import os
from typing import Optional, Callable as BarFn

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid URL type
        _download(42, "file.zip", "/path/to/save")
    
    with pytest.raises(TypeError):
        # Test invalid filename type
        _download("http://example.com/file.zip", 42, "/path/to/save")
    
    with pytest.raises(TypeError):
        # Test invalid path type
        _download("http://example.com/file.zip", "file.zip", 42)
    
    with pytest.raises(TypeError):
        # Test invalid bar_fn type
        _download("http://example.com/file.zip", "file.zip", "/path/to/save", bar_fn=42)

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

flutes/Test4DT_tests/test_flutes_network__download_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            # Test invalid URL type
            _download(42, "file.zip", "/path/to/save")
    
        with pytest.raises(TypeError):
            # Test invalid filename type
            _download("http://example.com/file.zip", 42, "/path/to/save")
    
        with pytest.raises(TypeError):
            # Test invalid path type
            _download("http://example.com/file.zip", "file.zip", 42)
    
        with pytest.raises(TypeError):
            # Test invalid bar_fn type
>           _download("http://example.com/file.zip", "file.zip", "/path/to/save", bar_fn=42)

flutes/Test4DT_tests/test_flutes_network__download_1_test_invalid_inputs.py:23: 
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

self = <urllib.request.HTTPDefaultErrorHandler object at 0x7fa73b6a18d0>
req = <urllib.request.Request object at 0x7fa73b478350>
fp = <http.client.HTTPResponse object at 0x7fa73b4897b0>, code = 404
msg = 'Not Found', hdrs = <http.client.HTTPMessage object at 0x7fa73b21c4d0>

    def http_error_default(self, req, fp, code, msg, hdrs):
>       raise HTTPError(req.full_url, code, msg, hdrs, fp)
E       urllib.error.HTTPError: HTTP Error 404: Not Found

/usr/local/lib/python3.11/urllib/request.py:643: HTTPError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__download_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.23s ===============================
"""