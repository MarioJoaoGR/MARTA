
import pytest
from flutes import Range

def test_error_case_no_args():
    with pytest.raises(ValueError):
        r = Range()
