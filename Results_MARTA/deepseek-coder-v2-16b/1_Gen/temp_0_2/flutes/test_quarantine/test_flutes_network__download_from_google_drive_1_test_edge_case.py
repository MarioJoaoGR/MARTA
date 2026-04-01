
import pytest
from unittest.mock import patch, MagicMock
import os
from flutes.network import _download_from_google_drive, _extract_google_drive_file_id

@pytest.mark.parametrize("url, filename, path, expected", [
    ("invalid_url", "file.txt", "./downloads", ValueError),
    (None, "file.txt", "./downloads", TypeError),
    ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", None, "./downloads", ValueError),
    ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", "file.txt", None, ValueError),
])
def test_edge_case(url, filename, path, expected):
    with pytest.raises(expected) if isinstance(expected, type) else pytest.fail("Expected exception not raised"):
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
collected 4 items

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_________ test_edge_case[invalid_url-file.txt-./downloads-ValueError] __________

url = 'invalid_url', filename = 'file.txt', path = './downloads'
expected = <class 'ValueError'>

    @pytest.mark.parametrize("url, filename, path, expected", [
        ("invalid_url", "file.txt", "./downloads", ValueError),
        (None, "file.txt", "./downloads", TypeError),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", None, "./downloads", ValueError),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", "file.txt", None, ValueError),
    ])
    def test_edge_case(url, filename, path, expected):
>       with pytest.raises(expected) if isinstance(expected, type) else pytest.fail("Expected exception not raised"):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py:14: Failed
_____________ test_edge_case[None-file.txt-./downloads-TypeError] ______________

url = None, filename = 'file.txt', path = './downloads'
expected = <class 'TypeError'>

    @pytest.mark.parametrize("url, filename, path, expected", [
        ("invalid_url", "file.txt", "./downloads", ValueError),
        (None, "file.txt", "./downloads", TypeError),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", None, "./downloads", ValueError),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", "file.txt", None, ValueError),
    ])
    def test_edge_case(url, filename, path, expected):
        with pytest.raises(expected) if isinstance(expected, type) else pytest.fail("Expected exception not raised"):
>           _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py:15: 
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
_ test_edge_case[https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view-None-./downloads-ValueError] _

url = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view'
filename = None, path = './downloads', expected = <class 'ValueError'>

    @pytest.mark.parametrize("url, filename, path, expected", [
        ("invalid_url", "file.txt", "./downloads", ValueError),
        (None, "file.txt", "./downloads", TypeError),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", None, "./downloads", ValueError),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", "file.txt", None, ValueError),
    ])
    def test_edge_case(url, filename, path, expected):
        with pytest.raises(expected) if isinstance(expected, type) else pytest.fail("Expected exception not raised"):
>           _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py:15: 
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
_ test_edge_case[https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view-file.txt-None-ValueError] _

url = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view'
filename = 'file.txt', path = None, expected = <class 'ValueError'>

    @pytest.mark.parametrize("url, filename, path, expected", [
        ("invalid_url", "file.txt", "./downloads", ValueError),
        (None, "file.txt", "./downloads", TypeError),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", None, "./downloads", ValueError),
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", "file.txt", None, ValueError),
    ])
    def test_edge_case(url, filename, path, expected):
        with pytest.raises(expected) if isinstance(expected, type) else pytest.fail("Expected exception not raised"):
>           _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py:15: 
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
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py::test_edge_case[invalid_url-file.txt-./downloads-ValueError]
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py::test_edge_case[None-file.txt-./downloads-TypeError]
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py::test_edge_case[https:/drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view-None-./downloads-ValueError]
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_edge_case.py::test_edge_case[https:/drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view-file.txt-None-ValueError]
============================== 4 failed in 1.64s ===============================
"""