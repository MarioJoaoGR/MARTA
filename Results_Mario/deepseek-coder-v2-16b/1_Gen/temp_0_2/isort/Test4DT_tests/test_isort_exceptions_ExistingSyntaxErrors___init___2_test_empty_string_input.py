
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_empty_string_input():
    with pytest.raises(ExistingSyntaxErrors) as excinfo:
        raise ExistingSyntaxErrors("")
    
    assert str(excinfo.value) == "isort was told to sort imports within code that contains syntax errors: ."
