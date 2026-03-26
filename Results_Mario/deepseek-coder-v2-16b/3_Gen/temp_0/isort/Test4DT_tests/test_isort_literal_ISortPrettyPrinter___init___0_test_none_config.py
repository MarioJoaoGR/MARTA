
from unittest.mock import MagicMock

import pytest

from isort.literal import Config, ISortPrettyPrinter


@pytest.fixture
def mock_config():
    config = MagicMock()
    config.line_length = 88
    return config

def test_none_config(mock_config):
    pretty_printer = ISortPrettyPrinter(config=mock_config)
    assert isinstance(pretty_printer, ISortPrettyPrinter)
    assert pretty_printer._width == mock_config.line_length
    assert pretty_printer._compact is True
