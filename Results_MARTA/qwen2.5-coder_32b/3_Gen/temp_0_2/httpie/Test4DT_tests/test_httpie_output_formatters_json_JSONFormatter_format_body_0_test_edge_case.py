
import pytest
from unittest.mock import patch
from httpie.output.formatters.json import JSONFormatter
import json

@pytest.fixture(autouse=True)
def setup_formatter():
    formatter = JSONFormatter(format_options={'json': {'format': True, 'sort_keys': False, 'indent': 2}})
    return formatter

def test_edge_case(setup_formatter):
    with patch('httpie.output.formatters.json.JSONFormatter.__init__', return_value=None):
        assert setup_formatter.enabled is True
