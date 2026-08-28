
# Module: isort.exceptions
import pytest
from isort.exceptions import FileSkipped

# Test Case 1: Raising the exception with a specific message and file path
def test_file_skipped_with_specific_message_and_path():
    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipped("File is corrupted", "documents/report.xlsx")
    
    assert str(exc_info.value) == "File is corrupted"
    assert exc_info.value.file_path == "documents/report.xlsx"

# Test Case 2: Handling the exception with a specific message and file path
def test_handle_file_skipped_with_specific_message_and_path():
    try:
        raise FileSkipped("File is corrupted", "documents/report.xlsx")
    except FileSkipped as e:
        assert str(e) == "File is corrupted"
        assert e.file_path == "documents/report.xlsx"

# Test Case 3: Raising the exception with a different message and file path
def test_file_skipped_with_different_message_and_path():
    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipped("File is not in the correct format", "data/transactions.csv")
    
    assert str(exc_info.value) == "File is not in the correct format"
    assert exc_info.value.file_path == "data/transactions.csv"

# Test Case 4: Handling the exception with a different message and file path
def test_handle_file_skipped_with_different_message_and_path():
    try:
        raise FileSkipped("File is not in the correct format", "data/transactions.csv")
    except FileSkipped as e:
        assert str(e) == "File is not in the correct format"
        assert e.file_path == "data/transactions.csv"

# Test Case 5: Raising and handling multiple exceptions with different scenarios
def test_multiple_exceptions():
    some_condition = True  # Assuming this variable should be defined here for testing purposes
    try:
        if some_condition:
            raise FileSkipped("File is missing", "documents/missing_report.xlsx")
        else:
            raise FileSkipped("File is too large", "data/large_file.txt")
    except FileSkipped as e:
        assert str(e) == "File is missing" or str(e) == "File is too large"
        assert e.file_path == "documents/missing_report.xlsx" or e.file_path == "data/large_file.txt"
