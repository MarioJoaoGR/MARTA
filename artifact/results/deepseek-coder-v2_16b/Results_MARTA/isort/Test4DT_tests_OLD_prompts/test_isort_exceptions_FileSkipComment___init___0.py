
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
from isort.exceptions import FileSkipComment

def test_valid_input():
    with patch('sys.stdout', new=StringIO()) as fake_output:
        try:
            raise FileSkipComment("path/to/your/file")
        except FileSkipComment as e:
            print(e)  # Output will be: path/to/your/file contains an file skip comment and was skipped.
    assert str(fake_output.getvalue().strip()) == "path/to/your/file contains an file skip comment and was skipped."

def test_edge_case_none():
    with patch('sys.stdout', new=StringIO()) as fake_output:
        try:
            raise FileSkipComment("another/path/to/the/file")
        except FileSkipComment as e:
            print(e)  # Output will be: another/path/to/the/file contains an file skip comment and was skipped.
    assert str(fake_output.getvalue().strip()) == "another/path/to/the/file contains an file skip comment and was skipped."

def test_invalid_input():
    with patch('sys.stdout', new=StringIO()) as fake_output:
        try:
            raise FileSkipComment("invalid/file/path")
        except FileSkipComment as e:
            print(e)  # Output will be: invalid/file/path contains an file skip comment and was skipped.
    assert str(fake_output.getvalue().strip()) == "invalid/file/path contains an file skip comment and was skipped."
