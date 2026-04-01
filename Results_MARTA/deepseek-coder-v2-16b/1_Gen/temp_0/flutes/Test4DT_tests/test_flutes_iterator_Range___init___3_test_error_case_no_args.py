
import pytest
from flutes.iterator import Range

def test_error_case_no_args():
    with pytest.raises(ValueError):
        r = Range()
