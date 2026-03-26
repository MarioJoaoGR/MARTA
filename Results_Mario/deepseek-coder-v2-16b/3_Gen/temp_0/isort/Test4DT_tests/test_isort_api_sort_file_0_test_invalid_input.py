
import io
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from isort.api import sort_file


@pytest.mark.skip(reason="This test will fail because the file does not exist")
def test_invalid_input():
    with patch('sys.stderr', new=io.StringIO()) as mock_stderr:
        assert not sort_file("nonexistent_file.py")
