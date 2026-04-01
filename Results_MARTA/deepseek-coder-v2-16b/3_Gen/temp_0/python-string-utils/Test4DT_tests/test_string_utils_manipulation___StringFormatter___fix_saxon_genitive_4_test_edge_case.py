
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_edge_case():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(12345)  # This should raise an InvalidInputError
