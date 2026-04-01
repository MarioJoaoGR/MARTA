
import pytest
from flutes.iterator import Range

def test_error_case_no_args():
    with pytest.raises(ValueError):
        r = Range()  # This should raise ValueError as per the function's requirement
