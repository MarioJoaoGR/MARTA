
import pytest
from unittest.mock import patch, MagicMock
import base64
import os
import errno
from ansible.modules.slurp import main
from ansible.module_utils.basic import AnsibleModule


def test_none_input():
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        mock_instance = mock_module.return_value
        mock_instance.params = {'src': None}

        with pytest.raises(SystemExit):
            main()
