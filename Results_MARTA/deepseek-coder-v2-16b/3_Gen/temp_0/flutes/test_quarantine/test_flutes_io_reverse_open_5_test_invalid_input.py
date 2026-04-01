
import pytest
from flutes.io import reverse_open
from pathlib import Path

def test_invalid_input():
    with pytest.raises(ValueError):
        reverse_open('non_existent_file.txt')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io_reverse_open_5_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError):
>           reverse_open('non_existent_file.txt')

flutes/Test4DT_tests/test_flutes_io_reverse_open_5_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 'non_existent_file.txt'

    def reverse_open(path: PathType, *, encoding: str = 'utf-8', allow_empty_lines: bool = False,
                     buffer_size: int = io.DEFAULT_BUFFER_SIZE):
        # Credits: https://stackoverflow.com/questions/2301789/read-a-file-in-reverse-order-using-python
        r"""A generator that returns the lines of a file in reverse order. Usage and syntax is the same as built-in
        method :py:func:`open`.
    
        :param path: Path to file.
        :param encoding: Encoding of file. Defaults to ``"utf-8"``.
        :param allow_empty_lines: If ``False``, empty lines are skipped. Defaults to ``False``.
        :param buffer_size: Buffer size. You probably won't need to change this for most cases. Defaults to
            :py:data:`io.DEFAULT_BUFFER_SIZE`.
        """
        if buffer_size < _ReverseReadlineFile.MAX_CHAR_BYTES:
            raise ValueError(f"`buf_size` must be at least {_ReverseReadlineFile.MAX_CHAR_BYTES}")
>       fp = open(path, "rb")
E       FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'

flutes/flutes/io.py:252: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_5_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""