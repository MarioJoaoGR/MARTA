
import os
from unittest.mock import patch, MagicMock
import pytest
from flutils.setuputils.cfg import _prep_setup_dir, _validate_setup_dir



def test_invalid_input():
    with patch('os.path.exists', return_value=False):
        with pytest.raises(FileNotFoundError):
            _prep_setup_dir('/non/existent/path')