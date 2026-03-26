
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_none_input():
    file_path = None
    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path)
    
    assert str(exc_info.value) == "isort was told to sort imports within code that contains syntax errors: None."
    assert exc_info.value.file_path is None
