
import io
from flutes.io import _ProgressBufferedReader, BarFn
import pytest

@pytest.fixture
def setup_reader():
    raw = io.BytesIO(b'some data')
    bar_fn = BarFn(total=len(b'some data'))
    reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)
    return reader

def test_seek_initial_position(setup_reader):
    assert setup_reader.tell() == 0

def test_seek_to_new_position(setup_reader):
    initial_pos = setup_reader.tell()
    new_pos = setup_reader.seek(1024)
    assert new_pos == 1024
    assert setup_reader.tell() == 1024

def test_seek_to_new_position_with_offset(setup_reader):
    initial_pos = setup_reader.tell()
    new_pos = setup_reader.seek(1024, io.SEEK_CUR)
    assert new_pos == 1024 + initial_pos
    assert setup_reader.tell() == 1024 + initial_pos

def test_seek_to_new_position_with_end(setup_reader):
    file_size = len(b'some data')
    new_pos = setup_reader.seek(0, io.SEEK_END)
    assert new_pos == file_size
    assert setup_reader.tell() == file_size

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io__ProgressBufferedReader_seek_0_test_edge_seek
flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_edge_seek.py:9:13: E0110: Abstract class 'Callable' with abstract methods instantiated (abstract-class-instantiated)


"""