
import pytest
from flutes.iterator import scanl


def test_invalid_input_too_many_args():
    with pytest.raises(ValueError):
        list(scanl(lambda s, x: s + x, ['a', 'b', 'c', 'd'], 1, 2))