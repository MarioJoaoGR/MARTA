
import pytest
from unittest.mock import patch
from io import StringIO
from thefuck.logs import rule_failed

def test_rule_failed_with_valid_rule():
    class RuleMock:
        name = "TestRule"
    
    exc_info = (Exception, Exception("An error occurred"), None)
    
    with patch('sys.stderr', new=StringIO()) as mock_stderr:
        rule_failed(RuleMock(), exc_info)
        assert 'Rule TestRule' in mock_stderr.getvalue()
        assert 'An error occurred' in mock_stderr.getvalue()

def test_rule_failed_with_invalid_rule():
    class RuleMock:
        name = None
    
    exc_info = (Exception, Exception("An error occurred"), None)
    
    with patch('sys.stderr', new=StringIO()) as mock_stderr:
        rule_failed(RuleMock(), exc_info)
        assert 'Rule None' in mock_stderr.getvalue()
        assert 'An error occurred' in mock_stderr.getvalue()
