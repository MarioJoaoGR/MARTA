
import pytest
from flutes.iterator import Range

def test_edge_case_zero_args():
    with pytest.raises(ValueError):
        r = Range()
