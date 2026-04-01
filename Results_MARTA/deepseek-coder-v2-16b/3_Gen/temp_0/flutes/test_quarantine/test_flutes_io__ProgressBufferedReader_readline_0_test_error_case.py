
import pytest
from unittest.mock import patch
from flutes.io import _ProgressBufferedReader
import io

@pytest.fixture
def mock_progress_bar():
    with patch('some_progress_bar_library.create_progress_bar') as mock_bar:
        yield mock_bar

@pytest.fixture
def raw_data():
    return io.BytesIO(b'line1\nline2\nline3\n')

@pytest.fixture
def reader(mock_progress_bar, raw_data):
    bar_fn = mock_progress_bar.return_value
    return _ProgressBufferedReader(raw=raw_data, buffer_size=4096, bar_fn=bar_fn)

def test_error_case(reader):
    assert reader._read_bytes == 0
    assert reader.readline() == b'line1\n'
    assert reader._read_bytes == 6
    assert reader.readline() == b'line2\n'
    assert reader._read_bytes == 13
    assert reader.readline() == b'line3\n'
    assert reader._read_bytes == 18

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_readline_0_test_error_case.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_error_case _______________________

    @pytest.fixture
    def mock_progress_bar():
>       with patch('some_progress_bar_library.create_progress_bar') as mock_bar:

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_readline_0_test_error_case.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1430: in __enter__
    self.target = self.getter()
/usr/local/lib/python3.11/pkgutil.py:700: in resolve_name
    mod = importlib.import_module(modname)
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1204: in _gcd_import
    ???
<frozen importlib._bootstrap>:1176: in _find_and_load
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = 'some_progress_bar_library'
import_ = <function _gcd_import at 0x7ffbcf303d80>

>   ???
E   ModuleNotFoundError: No module named 'some_progress_bar_library'

<frozen importlib._bootstrap>:1140: ModuleNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_readline_0_test_error_case.py::test_error_case
=============================== 1 error in 0.17s ===============================
"""