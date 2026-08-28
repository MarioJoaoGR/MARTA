
import pytest
from isort.exceptions import IntroducedSyntaxErrors

def test_invalid_input():
    with pytest.raises(IntroducedSyntaxErrors) as exc_info:
        raise IntroducedSyntaxErrors("example.py")
    
    assert str(exc_info.value) == "isort introduced syntax errors when attempting to sort the imports contained within example.py."
