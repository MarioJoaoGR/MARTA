
import pytest
from unittest.mock import patch, MagicMock
import os
import sys
from ansible.modules.pip import setup_virtualenv


def test_invalid_inputs():
    module = MagicMock()
    module.params = {'virtualenv_command': '', 'virtualenv_site_packages': False, 'virtualenv_python': None}
    with pytest.raises(IndexError):
        setup_virtualenv(module, env="myenv", chdir="/path/to/project", out="", err="")