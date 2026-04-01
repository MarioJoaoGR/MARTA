
from unittest.mock import patch

import pytest

from isort.settings import Config


def test_invalid_inputs():
    with patch('os.path.splitext', return_value=('.unsupported', '')):
        assert not Config().is_supported_filetype('example.unsupported')
