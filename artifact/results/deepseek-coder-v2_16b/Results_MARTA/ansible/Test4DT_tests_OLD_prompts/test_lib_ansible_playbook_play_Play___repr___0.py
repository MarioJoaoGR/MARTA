
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError, AnsibleError



def test_invalid_role():
    with patch('ansible.playbook.play.context', autospec=True) as mock_context:
        mock_context.CLIARGS = {'tags': [], 'skip_tags': []}

        # Invalid role configuration
        play_config = {
            'hosts': ['localhost'],
            'roles': ['non_existent_role']
        }
        with pytest.raises(AnsibleError):
            Play.load(play_config)