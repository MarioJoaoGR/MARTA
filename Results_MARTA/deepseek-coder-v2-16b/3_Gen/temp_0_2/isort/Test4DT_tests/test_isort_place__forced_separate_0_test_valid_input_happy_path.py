
import pytest
from unittest.mock import MagicMock
from isort.place import Config
from fnmatch import fnmatch

def _forced_separate(name: str, config: Config) -> tuple[str, str] | None:
    for forced_separate in config.forced_separate:
        # Ensure all forced_separate patterns will match to end of string
        path_glob = forced_separate
        if not forced_separate.endswith("*"):
            path_glob = f"{forced_separate}*"

        if fnmatch(name, path_glob) or fnmatch(name, "." + path_glob):
            return (forced_separate, f"Matched forced_separate ({forced_separate}) config value.")

    return None

@pytest.mark.parametrize("name, expected", [
    ('example.log', ('*.log', 'Matched forced_separate (*.log) config value.')),
    ('data.csv', ('data.*', 'Matched forced_separate (data.*) config value.')),
    ('structure/data.csv', None),
])
def test_valid_input_happy_path(name, expected):
    # Create a mock Config object with the required patterns
    config = MagicMock()
    config.forced_separate = ['*.log', 'data.*']
    
    # Call the function and check the result
    result = _forced_separate(name, config)
    assert result == expected
