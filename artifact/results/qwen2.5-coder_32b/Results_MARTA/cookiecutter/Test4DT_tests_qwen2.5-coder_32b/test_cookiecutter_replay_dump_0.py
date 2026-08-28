
import os
import json
from cookiecutter.replay import dump

def make_sure_path_exists(path):
    """Ensure that a path exists."""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except OSError as exc:
        return False

def get_file_name(replay_dir, template_name):
    """Construct the full file name for the replay file."""
    if not template_name.endswith('.json'):
        template_name += '.json'
    return os.path.join(replay_dir, template_name)

# Test function for basic functionality
def test_dump_basic(tmp_path):
    # Setup: Create a temporary directory and context data
    replay_dir = tmp_path / 'replays'
    template_name = 'game_data'
    context_data = {
        'cookiecutter': {'project_name': 'MyProject', 'author': 'John Doe'}
    }

    # Call the function under test
    dump(str(replay_dir), template_name, context_data)

    # Assert that the file was created and contains the correct data
    expected_file_path = replay_dir / f'{template_name}.json'
    assert expected_file_path.exists()

    with open(expected_file_path, 'r') as infile:
        written_data = json.load(infile)
    
    assert written_data == context_data
