
import pytest
from ansible.parsing.splitter import _get_quote_state



def test_get_quote_state_escaped_character():
    assert _get_quote_state('escaped\"single', None) == '"'