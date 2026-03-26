
import pytest
from pathlib import Path
from flutes.network import download
import os
import tempfile
import tarfile
import zipfile
from tqdm import tqdm
import functools

# Helper function to remove suffix from a string
def remove_suffix(s, suffix):
    if s.endswith(suffix):
        return s[:-len(suffix)]
    return s

# Mock functions for testing
def _extract_google_drive_file_id(url):
    return url.split('/')[-1]

def _download_from_google_drive(url, filename, save_dir, bar_fn=None):
    # Mock download from Google Drive
    if bar_fn:
        bar_fn = functools.partial(bar_fn, total=100)
    else:
        bar_fn = tqdm
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as f:
        for _ in bar_fn(range(100)):
            pass
        f.write(b'mock content')
    return f.name

def _download(url, filename, save_dir, bar_fn=None):
    # Mock download from a regular URL
    if bar_fn:
        bar_fn = functools.partial(bar_fn, total=100)
    else:
        bar_fn = tqdm
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as f:
        for _ in bar_fn(range(100)):
            pass
        f.write(b'mock content')
    return f.name

# Test cases for uncovered lines
@pytest.mark.parametrize("url, save_dir, filename, extract, progress, bar_fn", [
    ("http://example.com/file", None, None, False, False, None),
    ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view", tempfile.gettempdir(), None, True, False, None),
])
def test_download_uncovered(url, save_dir, filename, extract, progress, bar_fn):
    with pytest.raises(ValueError):  # Assuming the function should raise an error if save_dir is None
        download(url, save_dir, filename, extract, progress, bar_fn)

@pytest.mark.parametrize("url, save_dir, filename, extract, progress, bar_fn", [
    ("http://example.com/file", tempfile.gettempdir(), "custom_filename.txt", False, True, tqdm),
    ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view", tempfile.gettempdir(), None, False, True, functools.partial(tqdm, total=100)),
])
def test_download_with_progress_bar(url, save_dir, filename, extract, progress, bar_fn):
    result = download(url, save_dir, filename, extract, progress, bar_fn)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_network_download_1.py FFF.              [100%]

=================================== FAILURES ===================================
_ test_download_uncovered[http://example.com/file-None-None-False-False-None] __

url = 'http://example.com/file', save_dir = None, filename = None
extract = False, progress = False, bar_fn = None

    @pytest.mark.parametrize("url, save_dir, filename, extract, progress, bar_fn", [
        ("http://example.com/file", None, None, False, False, None),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view", tempfile.gettempdir(), None, True, False, None),
    ])
    def test_download_uncovered(url, save_dir, filename, extract, progress, bar_fn):
        with pytest.raises(ValueError):  # Assuming the function should raise an error if save_dir is None
>           download(url, save_dir, filename, extract, progress, bar_fn)

flutes/Test4DT_tests/test_flutes_network_download_1.py:53: 
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

self = <urllib.request.HTTPDefaultErrorHandler object at 0x7eff47bf8250>
req = <urllib.request.Request object at 0x7eff4896e590>
fp = <http.client.HTTPResponse object at 0x7eff47c164d0>, code = 404
msg = 'Not Found', hdrs = <http.client.HTTPMessage object at 0x7eff47bfd910>

    def http_error_default(self, req, fp, code, msg, hdrs):
>       raise HTTPError(req.full_url, code, msg, hdrs, fp)
E       urllib.error.HTTPError: HTTP Error 404: Not Found

/usr/local/lib/python3.11/urllib/request.py:643: HTTPError
_ test_download_uncovered[https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view-/tmp-None-True-False-None] _

url = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view'
save_dir = '/tmp', filename = None, extract = True, progress = False
bar_fn = None

    @pytest.mark.parametrize("url, save_dir, filename, extract, progress, bar_fn", [
        ("http://example.com/file", None, None, False, False, None),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view", tempfile.gettempdir(), None, True, False, None),
    ])
    def test_download_uncovered(url, save_dir, filename, extract, progress, bar_fn):
>       with pytest.raises(ValueError):  # Assuming the function should raise an error if save_dir is None
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_network_download_1.py:52: Failed
_ test_download_with_progress_bar[http://example.com/file-/tmp-custom_filename.txt-False-True-tqdm] _

url = 'http://example.com/file', save_dir = '/tmp'
filename = 'custom_filename.txt', extract = False, progress = True
bar_fn = <class 'tqdm.std.tqdm'>

    @pytest.mark.parametrize("url, save_dir, filename, extract, progress, bar_fn", [
        ("http://example.com/file", tempfile.gettempdir(), "custom_filename.txt", False, True, tqdm),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view", tempfile.gettempdir(), None, False, True, functools.partial(tqdm, total=100)),
    ])
    def test_download_with_progress_bar(url, save_dir, filename, extract, progress, bar_fn):
>       result = download(url, save_dir, filename, extract, progress, bar_fn)

flutes/Test4DT_tests/test_flutes_network_download_1.py:60: 
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

self = <urllib.request.HTTPDefaultErrorHandler object at 0x7eff47bf8250>
req = <urllib.request.Request object at 0x7eff47c6f8d0>
fp = <http.client.HTTPResponse object at 0x7eff47c167d0>, code = 404
msg = 'Not Found', hdrs = <http.client.HTTPMessage object at 0x7eff47c757d0>

    def http_error_default(self, req, fp, code, msg, hdrs):
>       raise HTTPError(req.full_url, code, msg, hdrs, fp)
E       urllib.error.HTTPError: HTTP Error 404: Not Found

/usr/local/lib/python3.11/urllib/request.py:643: HTTPError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network_download_1.py::test_download_uncovered[http:/example.com/file-None-None-False-False-None]
FAILED flutes/Test4DT_tests/test_flutes_network_download_1.py::test_download_uncovered[https:/drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view-/tmp-None-True-False-None]
FAILED flutes/Test4DT_tests/test_flutes_network_download_1.py::test_download_with_progress_bar[http:/example.com/file-/tmp-custom_filename.txt-False-True-tqdm]
========================= 3 failed, 1 passed in 0.39s ==========================
"""