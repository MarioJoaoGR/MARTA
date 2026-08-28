
import pytest
from unittest.mock import patch
from thonny.jedi_utils import _get_new_jedi_project


def test_get_new_jedi_project_with_empty_sys_path():
    with patch('thonny.jedi_utils._get_new_jedi_project') as mock_get_new_jedi_project:
        sys_path = []
        result = _get_new_jedi_project(sys_path)
        assert result is None, "Expected None but got a new Jedi project"
        mock_get_new_jedi_project.assert_not_called()