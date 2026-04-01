
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_empty_string_input():
    file_path = ''
    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path)
    
    assert str(exc_info.value) == "isort was told to sort imports within code that contains syntax errors: ."
    assert exc_info.value.file_path == ''
