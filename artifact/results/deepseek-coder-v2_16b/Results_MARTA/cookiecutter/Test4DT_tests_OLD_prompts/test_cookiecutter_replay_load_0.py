
import pytest
from unittest.mock import patch, MagicMock
import json

# Assuming the function 'load' and 'get_file_name' are defined in this module
def load(replay_dir, template_name):
    """Read json data from file."""
    if not isinstance(template_name, str):
        raise TypeError('Template name is required to be of type str')

    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, 'r') as infile:
        context = json.load(infile)

    if 'cookiecutter' not in context:
        raise ValueError('Context is required to contain a cookiecutter key')

    return context

def get_file_name(replay_dir, template_name):
    """Construct the full file path."""
    if not template_name.endswith('.json'):
        template_name += '.json'
    return replay_dir + template_name

# Test scenarios
@pytest.fixture(autouse=True)
def mock_get_file_name():
    with patch('cookiecutter.replay.get_file_name', side_effect=lambda dir, name: f"{dir}/{name}.json"):
        yield

@pytest.mark.parametrize("replay_dir, template_name", [
    ('data', 'example'),
    ('logs/', 'logfile'),
    ('backups/', 'backup123')
])
def test_valid_input(replay_dir, template_name):
    with patch('builtins.open', new_callable=MagicMock) as mock_file:
        mock_file.return_value.__enter__.return_value.read.return_value = json.dumps({'cookiecutter': {}})
        assert load(replay_dir, template_name) == {'cookiecutter': {}}

def test_none_input():
    with pytest.raises(TypeError):
        load(None, None)

def test_invalid_template_name():
    with pytest.raises(TypeError):
        load('data', 12345)
