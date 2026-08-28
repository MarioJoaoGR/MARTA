
import os
from unittest.mock import patch, MagicMock
import pytest
from cookiecutter.exceptions import NonTemplatedInputDirException
from cookiecutter.find import find_template

# Test for valid case where the directory and 'cookiecutter' with '{{' and '}}' exist

# Test for case where no template is found
def test_no_template():
    with patch('os.listdir', return_value=['not_cookiecutter']):
        repo_path = "test/repo"
        with pytest.raises(NonTemplatedInputDirException):
            find_template(repo_path)