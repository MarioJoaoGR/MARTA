
import pytest
from semantic_release.hvcs import Base

def test_missing_implementation():
    instance = Base()
    with pytest.raises(NotImplementedError):
        instance.domain()
