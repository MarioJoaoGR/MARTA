
import pytest
from unittest.mock import patch
import argparse

def readable_file_arg(filename):
    """
    Check if the given file is readable and return its name, or raise an error if not.

    Parameters:
        filename (str): The path to the file you want to check.

    Returns:
        str: The name of the file if it is readable.

    Raises:
        argparse.ArgumentTypeError: If the file does not exist or is not readable, an error message indicating the issue will be raised.

    Examples:
        >>> readable_file_arg('example.txt')
        'example.txt'
        
        >>> try:
        ...     print(readable_file_arg('nonexistent.txt'))
        ... except argparse.ArgumentTypeError as e:
        ...     print(e)
        nonexistent.txt: No such file or directory
    """
    try:
        with open(filename, 'rb'):
            return filename
    except OSError as ex:
        raise argparse.ArgumentTypeError(f'{ex.filename}: {ex.strerror}')

@pytest.fixture
def valid_file():
    # Create a temporary file for testing
    import os
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write('test content')
        tmp.seek(0)
        yield tmp.name
        os.remove(tmp.name)

@pytest.mark.parametrize("file_path", ["valid_file"])
def test_valid_file(valid_file):
    with patch('builtins.open', create=True):  # Mock the built-in open function
        assert readable_file_arg(valid_file) == valid_file

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_readable_file_arg_0_test_valid_file.py _
In test_valid_file: function uses no argument 'file_path'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_readable_file_arg_0_test_valid_file.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""