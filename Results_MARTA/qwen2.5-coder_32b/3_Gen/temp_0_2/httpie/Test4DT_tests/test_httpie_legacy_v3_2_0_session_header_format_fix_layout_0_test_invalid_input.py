
import pytest
from unittest.mock import patch
from httpie.sessions import materialize_headers

def fix_layout(session: 'Session', *args, **kwargs) -> None:
    if not isinstance(session['headers'], dict):
        return None

    session['headers'] = materialize_headers(session['headers'])

@pytest.mark.parametrize("invalid_input", [
    ({'headers': 'not a dictionary'}),
    ({'headers': 12345}),
    ({'headers': []})
])
def test_invalid_input(invalid_input):
    with patch('httpie.sessions.materialize_headers', return_value={'name': 'Value'}):
        fix_layout({'headers': invalid_input}, None)
