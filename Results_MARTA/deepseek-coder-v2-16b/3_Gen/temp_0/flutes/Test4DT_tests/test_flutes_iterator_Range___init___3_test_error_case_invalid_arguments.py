
import pytest
from flutes.iterator import Range

def test_error_case_invalid_arguments():
    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4)
