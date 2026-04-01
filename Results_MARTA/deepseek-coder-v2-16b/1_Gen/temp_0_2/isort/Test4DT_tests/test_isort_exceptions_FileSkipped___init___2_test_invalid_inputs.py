
from isort.exceptions import FileSkipped
import pytest

def test_invalid_inputs():
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("File is corrupted", "documents/report.xlsx")
    
    assert str(excinfo.value) == "File is corrupted"
    assert excinfo.value.file_path == "documents/report.xlsx"
