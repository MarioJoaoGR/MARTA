
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(None)
