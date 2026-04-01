
import pytest
from flutes.iterator import scanl

def test_error_case_too_many_args():
    with pytest.raises(ValueError):
        list(scanl(lambda x, y: x + y, [1, 2, 3], 'initial', 'extra'))
