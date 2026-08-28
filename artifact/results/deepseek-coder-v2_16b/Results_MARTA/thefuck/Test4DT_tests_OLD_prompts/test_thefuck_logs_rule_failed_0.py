
import pytest
from unittest.mock import patch, MagicMock
from thefuck.logs import rule_failed


def test_rule_failed_with_none_rule():
    mock_rule = None
    exc_info = (Exception, Exception("An error occurred"), None)
    
    with patch('sys.stderr', new=MagicMock()) as mock_stderr:
        with pytest.raises(AttributeError):
            rule_failed(mock_rule, exc_info)
