
import pytest
from unittest.mock import patch
from ansible.cli.adhoc import context, AdHocCLI



def test_invalid_inputs_error_handling():
    with patch('ansible.cli.adhoc.context', {'CLIARGS': {'module_name': 'unknown_module', 'module_args': '', 'task_timeout': 30}}):
        with pytest.raises(TypeError):
            AdHocCLI()