
import pytest
from flutes import Range

def test_error_case_no_arguments():
    with pytest.raises(ValueError):
        r = Range()
