
import pytest
from pathlib import Path
from httpie.sessions import Environment, Session
from unittest.mock import patch

def test_get_httpie_session():
    env = Environment()
    config_dir = Path('~/.httpie').expanduser()
    
    with patch('httpie.sessions.Session', autospec=True) as mock_session:
        session = get_httpie_session(env, config_dir, 'my_session', host='api.example.com', url='http://api.example.com/endpoint')
        
        assert isinstance(session, Session)
        mock_session.assert_called_once_with(
            Path('~/.httpie/api.example.com/my_session').expanduser(),
            env=env,
            session_id='my_session',
            bound_host='api.example.com',
            suppress_legacy_warnings=False
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_sessions_get_httpie_session_0_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_get_httpie_session_0_test_edge_cases.py:12:18: E0602: Undefined variable 'get_httpie_session' (undefined-variable)


"""