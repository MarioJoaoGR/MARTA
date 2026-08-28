
import pytest
from ansible.galaxy.api import GalaxyAPI
from unittest.mock import patch

@pytest.fixture(scope="module")
def valid_api():
    return GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')

@pytest.fixture(scope="module")
def invalid_task_id_api():
    return GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com', task_id=-1)

def test_valid_input_with_task_id(valid_api):
    with patch('ansible.galaxy.api.requests.get') as mock_get:
        # Mock the response from requests.get
        mock_response = {
            "results": [{"status": "success"}]
        }
        mock_get.return_value.json.return_value = mock_response
        
        task_id = 12345
        result = valid_api.get_import_task(task_id=task_id)
        
        assert len(result) == 1
        assert result[0]['status'] == 'success'

def test_missing_parameters():
    with pytest.raises(ValueError):
        api = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
        api.get_import_task()

def test_invalid_task_id(invalid_task_id_api):
    with pytest.raises(ValueError) as excinfo:
        invalid_task_id_api.get_import_task()
    
    assert str(excinfo.value) == "Expected task_id or github_user and github_repo"
