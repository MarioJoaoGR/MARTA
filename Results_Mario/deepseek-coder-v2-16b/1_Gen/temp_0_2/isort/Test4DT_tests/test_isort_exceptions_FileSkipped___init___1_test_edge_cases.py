
import pytest
from isort.exceptions import FileSkipped

def test_file_skipped_exception():
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("File is corrupted", "documents/report.xlsx")
    
    assert str(excinfo.value) == "File is corrupted"
    assert excinfo.value.file_path == "documents/report.xlsx"
