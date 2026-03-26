
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_none_input():
    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path=None)
    
    assert str(exc_info.value) == "isort was told to sort imports within code that contains syntax errors: None."
