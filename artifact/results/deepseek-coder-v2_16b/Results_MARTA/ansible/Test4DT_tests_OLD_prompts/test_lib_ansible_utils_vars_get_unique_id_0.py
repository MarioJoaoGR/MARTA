
import pytest
from unittest.mock import patch
from ansible.utils.vars import get_unique_id

def test_valid_input():
    global cur_id, node_mac, random_int
    # Setup
    cur_id = 0
    node_mac = "001122334455"
    with patch('ansible.utils.vars.random', autospec=True) as mock_random:
        mock_random.randint.return_value = 12345678
        random_int = str(mock_random.randint(10000000, 99999999)).zfill(8)
    # Test
    unique_id = get_unique_id()
    assert isinstance(unique_id, str), "Expected a string"
    assert len(unique_id.split('-')) == 5, "Expected 5 parts separated by hyphens"

def test_edge_case():
    global cur_id, node_mac, random_int
    # Setup
    cur_id = 0
    node_mac = "001122334455"
    with patch('ansible.utils.vars.random', autospec=True) as mock_random:
        mock_random.randint.return_value = 12345678
        random_int = str(mock_random.randint(10000000, 99999999)).zfill(8)
    # Test
    unique_id = get_unique_id()
    assert isinstance(unique_id, str), "Expected a string"
    assert len(unique_id.split('-')) == 5, "Expected 5 parts separated by hyphens"
