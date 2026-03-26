
import pytest
from pathlib import Path
from flutes.log import set_log_file, LOGGER
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(TypeError):
        set_log_file(123)  # Invalid path type (int)
