
import os
from flutils.setuputils.cfg import _prep_setup_dir, _validate_setup_dir
from unittest.mock import patch
import pytest



def test_prep_setup_dir_invalid_path():
    setup_dir = "/nonexistent/path"
    with pytest.raises(FileNotFoundError):
        _prep_setup_dir(setup_dir)