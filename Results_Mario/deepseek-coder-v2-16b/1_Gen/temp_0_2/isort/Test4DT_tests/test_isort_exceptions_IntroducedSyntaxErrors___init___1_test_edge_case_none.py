
import pytest
from isort.exceptions import IntroducedSyntaxErrors

def test_edge_case_none():
    with pytest.raises(IntroducedSyntaxErrors) as excinfo:
        raise IntroducedSyntaxErrors(None)
    assert str(excinfo.value) == "isort introduced syntax errors when attempting to sort the imports contained within None."
