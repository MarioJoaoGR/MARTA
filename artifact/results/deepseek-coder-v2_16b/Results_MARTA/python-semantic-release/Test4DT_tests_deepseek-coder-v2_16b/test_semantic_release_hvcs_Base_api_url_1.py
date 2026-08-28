
import pytest
from semantic_release.hvcs import Base

def test_missing_lines_to_cover():
    base = Base()
    with pytest.raises(NotImplementedError):
        base.api_url()

def test_invalid_input():
    base = Base()
    with pytest.raises(NotImplementedError):
        base.api_url()
