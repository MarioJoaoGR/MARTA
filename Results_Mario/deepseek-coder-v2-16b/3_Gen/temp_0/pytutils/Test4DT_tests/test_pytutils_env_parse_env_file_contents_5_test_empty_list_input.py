
import re
import pytest
from unittest.mock import patch
from pytutils.env import parse_env_file_contents

@pytest.mark.parametrize("lines", [[]])
def test_empty_list_input(lines):
    with patch('pytutils.env.re') as mock_re:
        mock_re.match.side_effect = lambda pattern, string: None if not string else {'A': 1}.get(pattern)
        gen = parse_env_file_contents(lines)
        assert list(gen) == []
