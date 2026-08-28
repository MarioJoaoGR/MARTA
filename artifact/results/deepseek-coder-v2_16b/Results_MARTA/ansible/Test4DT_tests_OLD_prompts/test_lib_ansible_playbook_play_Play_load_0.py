
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.play import Play

def test_load_invalid_data():
    invalid_data = 'not a dict'
    with patch('ansible.playbook.play.Play.load_data') as mock_load_data:
        mock_load_data.side_effect = Exception("Invalid data")
        with pytest.raises(Exception):
            Play.load(invalid_data)

def test_load_none_data():
    none_data = None
    with patch('ansible.playbook.play.Play.load_data') as mock_load_data:
        mock_load_data.side_effect = Exception("None data")
        with pytest.raises(Exception):
            Play.load(none_data)
