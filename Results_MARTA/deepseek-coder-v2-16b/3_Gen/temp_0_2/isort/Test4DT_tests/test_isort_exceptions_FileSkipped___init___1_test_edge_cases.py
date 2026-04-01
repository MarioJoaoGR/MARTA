
import pytest
from isort.exceptions import FileSkipped

def test_file_skipped_edge_cases():
    # Test None values
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("Test message for None", None)
    assert str(excinfo.value) == "Test message for None"
    assert excinfo.value.file_path is None

    # Test empty string values
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("Test message for empty string", "")
    assert str(excinfo.value) == "Test message for empty string"
    assert excinfo.value.file_path == ""
