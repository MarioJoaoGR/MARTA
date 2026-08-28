
# Test case  
import pytest
from isort.exceptions import FileSkipped

def test_fileskipped_initialization():
    # Test with a basic message and file path
    message = "File does not exist"
    file_path = "non_existent_file.py"
    exception = FileSkipped(message, file_path)
    
    assert str(exception) == message
    assert exception.file_path == file_path

def test_fileskipped_with_empty_message():
    # Test with an empty message and a valid file path
    message = ""
    file_path = "empty_message_file.py"
    exception = FileSkipped(message, file_path)
    
    assert str(exception) == message
    assert exception.file_path == file_path

def test_fileskipped_with_empty_file_path():
    # Test with a valid message and an empty file path
    message = "File does not exist"
    file_path = ""
    exception = FileSkipped(message, file_path)
    
    assert str(exception) == message
    assert exception.file_path == file_path

def test_fileskipped_with_long_message():
    # Test with a long message and a valid file path
    message = "This is a very long message explaining why the file was skipped because of some specific conditions that need to be met before processing can continue."
    file_path = "long_message_file.py"
    exception = FileSkipped(message, file_path)
    
    assert str(exception) == message
    assert exception.file_path == file_path

def test_fileskipped_with_special_characters():
    # Test with special characters in both message and file path
    message = "File doesn't exist @ # $ % ^ & * ( )"
    file_path = "special_chars@#$%^&*().py"
    exception = FileSkipped(message, file_path)
    
    assert str(exception) == message
    assert exception.file_path == file_path

def test_fileskipped_with_unicode():
    # Test with unicode characters in both message and file path
    message = "Файл не существует"
    file_path = "файл_не_существует.py"
    exception = FileSkipped(message, file_path)
    
    assert str(exception) == message
    assert exception.file_path == file_path

def test_fileskipped_with_large_file_path():
    # Test with a very long file path
    message = "File does not exist"
    file_path = "/a" * 100 + ".py"
    exception = FileSkipped(message, file_path)
    
    assert str(exception) == message