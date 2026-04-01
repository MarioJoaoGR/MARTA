
import pytest
from unittest.mock import patch, MagicMock
from pytutils.pretty import pf

@pytest.mark.skip(reason="This test will be enabled once Pygments is properly configured.")
def test_none_input():
    # Test when input is None
    with patch('pytutils.pretty._pprint', MagicMock()):
        with patch('pygments.lexers.PythonLexer'):
            with patch('pygments.formatters.Terminal256Formatter'):
                assert pf(None) == 'None'
