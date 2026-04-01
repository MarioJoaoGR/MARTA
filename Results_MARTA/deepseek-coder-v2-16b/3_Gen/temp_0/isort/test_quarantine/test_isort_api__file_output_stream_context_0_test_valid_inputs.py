
import pytest
from pathlib import Path
from typing import Iterator, TextIO
from isort.api import create_temp_file  # Assuming this is the correct import statement for the function

def _file_output_stream_context(filename: str | Path, source_file: File) -> Iterator[TextIO]:
    """
    Creates and yields a temporary file stream for writing, copying the mode from an existing file.

    Parameters:
        filename (str | Path): The path to the original file as either a string or a Path object. This is used to copy the mode when creating the temporary file.
        source_file (File): An instance of a File object representing the original file from which the encoding and newline settings are taken for the temporary file.

    Returns:
        Iterator[TextIO]: A generator that yields a writable text stream to the temporary file, allowing you to write data to it while the function is executing.

    Examples:
        Given a filename string `'/path/to/original/file.txt'` and a File object `source_file`, calling `_file_output_stream_context('/path/to/original/file.txt', source_file)` will create a temporary file with the same path but with an added suffix `.isorted` (e.g., `/path/to/original/file.txt.isorted`) and yield a writable stream to this temporary file.

        If you provide a Path object `Path('/path/to/original/file.txt')` as the filename and the same File object, the function will behave identically, creating a temporary file at `/path/to/original/file.txt.isorted`.

    Notes:
        This function creates a temporary file with read-write access (`"w+"` mode) using the encoding and newline settings from the provided `source_file`. It then copies the mode (permissions, etc.) from the original file specified by `filename` to the temporary file. The temporary file is automatically cleaned up when the generator yields its last value or when the context is exited.
    """
    tmp_file = create_temp_file(suffix=".isorted", dir=str(Path(filename).parent))
    with tmp_file.open("w+", encoding=source_file.encoding, newline="") as output_stream:
        shutil.copymode(filename, tmp_file)
        yield output_stream

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api__file_output_stream_context_0_test_valid_inputs
isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_valid_inputs.py:5:0: E0611: No name 'create_temp_file' in module 'isort.api' (no-name-in-module)
isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_valid_inputs.py:7:67: E0602: Undefined variable 'File' (undefined-variable)
isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_valid_inputs.py:28:8: E0602: Undefined variable 'shutil' (undefined-variable)


"""