
import pytest
from unittest.mock import patch
from httpie.output.formatters.json import JSONFormatter

def test_none_input():
    with patch('httpie.output.formatters.json.JSONFormatter.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            formatter = JSONFormatter()
