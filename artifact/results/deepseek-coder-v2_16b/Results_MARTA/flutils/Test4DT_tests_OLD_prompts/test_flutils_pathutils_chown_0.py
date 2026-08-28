
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import os
from flutils.pathutils import chown

def test_valid_case_single_file():
    with patch('flutils.pathutils.os.chown', return_value=None):
        path = Path('test_file')
        with patch('flutils.pathutils.Path.exists', return_value=True):
            chown(str(path))
            assert os.chown.called
