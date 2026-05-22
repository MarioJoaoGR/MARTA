
import pytest
from unittest.mock import patch
from httpie.legacy.v3_2_0_session_header_format import OLD_HEADER_STORE_WARNING, OLD_HEADER_STORE_WARNING_FOR_NAMED_SESSIONS, OLD_HEADER_STORE_LINK, pre_process
from requests.sessions import Session
from typing import Any, List, Dict

@patch('httpie.legacy.v3_2_0_session_header_format.OLD_HEADER_STORE_WARNING', 'Warning message')
@patch('httpie.legacy.v3_2_0_session_header_format.OLD_HEADER_STORE_WARNING_FOR_NAMED_SESSIONS', '')
@patch('httpie.legacy.v3_2_0_session_header_format.OLD_HEADER_STORE_LINK', 'Link')
def test_invalid_headers():
    session = Session()
    headers = None
    
    with pytest.raises(TypeError):
        pre_process(session, headers)
