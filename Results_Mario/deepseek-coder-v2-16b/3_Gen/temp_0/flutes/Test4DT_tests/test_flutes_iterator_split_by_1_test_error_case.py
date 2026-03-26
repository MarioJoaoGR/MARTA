
import pytest
from flutes.iterator import split_by

def test_error_case():
    with pytest.raises(ValueError):
        list(split_by([1, 2, 3]))
