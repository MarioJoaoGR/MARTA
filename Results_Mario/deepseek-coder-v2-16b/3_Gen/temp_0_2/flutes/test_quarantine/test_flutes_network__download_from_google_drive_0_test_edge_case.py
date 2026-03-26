
import pytest
from flutes.network import _download_from_google_drive, _extract_google_drive_file_id
from unittest.mock import patch

@pytest.mark.parametrize("url, filename, path", [
    (None, "file.txt", "./downloads"),
    ("https://example.com/valid-url", None, "./downloads"),
    ("https://example.com/valid-url", "file.txt", None)
])
def test_edge_case(url, filename, path):
    with pytest.raises(ValueError):
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

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_edge_case.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________ test_edge_case[None-file.txt-./downloads] ___________________

url = None, filename = 'file.txt', path = './downloads'

    @pytest.mark.parametrize("url, filename, path", [
        (None, "file.txt", "./downloads"),
        ("https://example.com/valid-url", None, "./downloads"),
        ("https://example.com/valid-url", "file.txt", None)
    ])
    def test_edge_case(url, filename, path):
        with pytest.raises(ValueError):
>           _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_edge_case.py:13: 
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
________ test_edge_case[https://example.com/valid-url-None-./downloads] ________

url = 'https://example.com/valid-url', filename = None, path = './downloads'

    @pytest.mark.parametrize("url, filename, path", [
        (None, "file.txt", "./downloads"),
        ("https://example.com/valid-url", None, "./downloads"),
        ("https://example.com/valid-url", "file.txt", None)
    ])
    def test_edge_case(url, filename, path):
        with pytest.raises(ValueError):
>           _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_edge_case.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/network.py:139: in _download_from_google_drive
    filepath = os.path.join(path, filename)
<frozen posixpath>:90: in join
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

funcname = 'join', args = ('./downloads', None), hasstr = True, hasbytes = False
s = None

>   ???
E   TypeError: join() argument must be str, bytes, or os.PathLike object, not 'NoneType'

<frozen genericpath>:152: TypeError
_________ test_edge_case[https://example.com/valid-url-file.txt-None] __________

url = 'https://example.com/valid-url', filename = 'file.txt', path = None

    @pytest.mark.parametrize("url, filename, path", [
        (None, "file.txt", "./downloads"),
        ("https://example.com/valid-url", None, "./downloads"),
        ("https://example.com/valid-url", "file.txt", None)
    ])
    def test_edge_case(url, filename, path):
        with pytest.raises(ValueError):
>           _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_edge_case.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/network.py:139: in _download_from_google_drive
    filepath = os.path.join(path, filename)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

a = None, p = ('file.txt',)

>   ???
E   TypeError: expected str, bytes or os.PathLike object, not NoneType

<frozen posixpath>:76: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_edge_case.py::test_edge_case[None-file.txt-./downloads]
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_edge_case.py::test_edge_case[https:/example.com/valid-url-None-./downloads]
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0_test_edge_case.py::test_edge_case[https:/example.com/valid-url-file.txt-None]
============================== 3 failed in 0.71s ===============================
"""