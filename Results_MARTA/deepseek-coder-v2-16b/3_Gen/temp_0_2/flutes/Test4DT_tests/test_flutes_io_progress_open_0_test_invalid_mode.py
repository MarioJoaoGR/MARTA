
import pytest
from flutes.io import progress_open
import io

def test_invalid_mode():
    with pytest.raises(ValueError):
        with progress_open('sample.txt', mode='w') as f:
            pass
