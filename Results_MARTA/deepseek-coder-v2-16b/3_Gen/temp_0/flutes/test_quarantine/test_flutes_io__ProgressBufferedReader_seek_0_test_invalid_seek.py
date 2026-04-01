
import io
from flutes.io import progress_bar as BarFn

class _ProgressBufferedReader(io.BufferedReader):
    """
    A class for reading from a raw IO base with progress feedback using a specified progress bar function.

    Parameters:
        raw (io.RawIOBase): The underlying raw I/O stream to read from.
        buffer_size (int, optional): The size of the buffer used for reading. Defaults to io.DEFAULT_BUFFER_SIZE.
        bar_fn (BarFn): A function that creates and updates a progress bar. It should take a 'total' parameter indicating the total number of bytes to be read.

    Attributes:
        _read_bytes (int): The number of bytes read so far from the raw IO base.
        progress_bar (BarFn): An instance of the progress bar function provided by `bar_fn`.

    Methods:
        __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn) -> None: Initializes the reader with the given parameters and sets up the progress bar.
    """
    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
        file_size = io.fstat(raw.fileno()).st_size
        self._read_bytes = 0
        self.progress_bar = bar_fn(total=file_size)

    def seek(self, offset: int, whence: int = io.SEEK_SET) -> int:
        """
        Moves the file pointer by the specified offset from the given position (specified by `whence`). The progress bar is updated based on the actual number of bytes moved. Returns the new position of the file pointer as an integer.

        Parameters:
            offset (int): The byte offset to move.
            whence (int, optional): The reference point from which `offset` is measured. Must be one of io.SEEK_SET, io.SEEK_CUR, or io.SEEK_END. Defaults to io.SEEK_SET.

        Returns:
            The new position of the file pointer after seeking, which includes the number of bytes actually read or moved.
        """
        ret = super().seek(offset, whence)
        self.progress_bar.update(ret - self._read_bytes)
        self._read_bytes = ret
        return ret

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_invalid_seek.py _
ImportError while importing test module '/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_invalid_seek.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_invalid_seek.py:3: in <module>
    from flutes.io import progress_bar as BarFn
E   ImportError: cannot import name 'progress_bar' from 'flutes.io' (/projects/F202407648IACDCF2/mario/flutes/flutes/io.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_invalid_seek.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""