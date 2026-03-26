
import pytest

from isort.exceptions import IntroducedSyntaxErrors


def test_invalid_input():
    """Test invalid input by providing a non-string value."""
    with pytest.raises(IntroducedSyntaxErrors) as excinfo:
        raise IntroducedSyntaxErrors("not a string")
    
    assert str(excinfo.value) == "isort introduced syntax errors when attempting to sort the imports contained within not a string."
