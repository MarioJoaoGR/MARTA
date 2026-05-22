
import pytest
from unittest.mock import patch, MagicMock
from httpie.sessions import Session
from httpie.sessions import Environment
from pathlib import Path
from typing import Dict, Any, Union

@pytest.fixture
def mock_session():
    return Session(path=Path('test_session'), env=Environment(), bound_host='example.com', session_id='12345')

def test_invalid_input(mock_session):
    with patch('httpie.sessions.legacy_cookies.pre_process', side_effect=Exception("Invalid cookies")):
        with pytest.raises(Exception) as excinfo:
            mock_session.pre_process_data({'cookies': ['cookie1=value1; cookie2=value2']})
        assert str(excinfo.value) == "Invalid cookies"

    with patch('httpie.sessions.legacy_headers.pre_process', side_effect=Exception("Invalid headers")):
        with pytest.raises(Exception) as excinfo:
            mock_session.pre_process_data({'headers': ['Header1: Value1', 'Header2: Value2']})
        assert str(excinfo.value) == "Invalid headers"
