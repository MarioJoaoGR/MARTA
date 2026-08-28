# Module: isort.exceptions
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_existing_syntax_errors_initialization():
    # Test with a simple file name
    error = ExistingSyntaxErrors('example.py')
    assert str(error) == "isort was told to sort imports within code that contains syntax errors: example.py."
    assert error.file_path == 'example.py'

    # Test with a different file name
    error = ExistingSyntaxErrors('script_with_errors.py')
    assert str(error) == "isort was told to sort imports within code that contains syntax errors: script_with_errors.py."
    assert error.file_path == 'script_with_errors.py'

    # Test with an absolute path
    error = ExistingSyntaxErrors('/home/user/projects/my_project/main.py')
    assert str(error) == "isort was told to sort imports within code that contains syntax errors: /home/user/projects/my_project/main.py."
    assert error.file_path == '/home/user/projects/my_project/main.py'

def test_existing_syntax_errors_with_empty_string():
    # Test with an empty string as file path
    error = ExistingSyntaxErrors('')
    assert str(error) == "isort was told to sort imports within code that contains syntax errors: ."
    assert error.file_path == ''

def test_existing_syntax_errors_with_whitespace():
    # Test with whitespace only as file path
    error = ExistingSyntaxErrors('   ')
    assert str(error) == "isort was told to sort imports within code that contains syntax errors:    ."
    assert error.file_path == '   '

def test_existing_syntax_errors_with_special_characters():
    # Test with special characters in the file path
    error = ExistingSyntaxErrors('file@name!.py')
    assert str(error) == "isort was told to sort imports within code that contains syntax errors: file@name!.py."
    assert error.file_path == 'file@name!.py'
