
import pytest
from isort.exceptions import MissingSection



def test_invalid_input():
    with pytest.raises(MissingSection):
        raise MissingSection(123, True)