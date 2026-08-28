
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_ExistingSyntaxErrors___init___basic():
    file_path = "path/to/your_script.py"
    exception = ExistingSyntaxErrors(file_path)
    
    assert str(exception) == f"isort was told to sort imports within code that contains syntax errors: {file_path}."
    assert exception.file_path == file_path
