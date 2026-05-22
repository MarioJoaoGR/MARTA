
import pytest
from unittest.mock import patch, MagicMock
from httpie.legacy.v3_2_0_session_header_format import pre_process
from requests import Session
from typing import List, Dict, Any

@pytest.fixture
def setup():
    session = Session()
    headers = [{'name': 'Content-Type', 'value': 'application/json'}, {'name': 'Accept', 'value': '*/*'}]
    return pre_process(session, headers)

def test_valid_headers_list(setup):
    expected_result = [('Content-Type', 'application/json'), ('Accept', '*/*')]
    assert setup == expected_result
