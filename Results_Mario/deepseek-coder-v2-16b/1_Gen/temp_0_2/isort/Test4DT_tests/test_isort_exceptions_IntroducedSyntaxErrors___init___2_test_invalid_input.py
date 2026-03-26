
import pytest
from isort.exceptions import IntroducedSyntaxErrors

def test_invalid_input():
    with pytest.raises(IntroducedSyntaxErrors) as excinfo:
        raise IntroducedSyntaxErrors("non_existent_file.py")
    
    assert "isort introduced syntax errors when attempting to sort the imports contained within" in str(excinfo.value)
    assert "non_existent_file.py" in str(excinfo.value)
