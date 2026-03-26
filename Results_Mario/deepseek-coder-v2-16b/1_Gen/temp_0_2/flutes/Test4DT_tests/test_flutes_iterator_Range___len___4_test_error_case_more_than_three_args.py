
import pytest
from flutes.iterator import Range

def test_error_case_more_than_three_args():
    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4)
