
from pathlib import Path
import pytest
from flutes.io import progress_open

def test_invalid_mode():
    with pytest.raises(ValueError):
        progress_open(Path('example.txt'), mode='x')  # 'x' is an invalid mode for reading
