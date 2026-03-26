
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_edge_case_none():
    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(None)
    
    assert str(exc_info.value) == "isort was told to sort imports within code that contains syntax errors: None."
