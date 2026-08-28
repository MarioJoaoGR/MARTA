
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.playbook.role_include import IncludeRole



def test_invalid_inputs():
    with pytest.raises(Exception) as excinfo:
        with patch('lib.ansible.playbook.role_include.IncludeRole.__init__', side_effect=Exception('Invalid options specified for the role action')):
            IncludeRole(block='invalid', role=123, task_include='not a list')
    assert str(excinfo.value) == 'Invalid options specified for the role action'