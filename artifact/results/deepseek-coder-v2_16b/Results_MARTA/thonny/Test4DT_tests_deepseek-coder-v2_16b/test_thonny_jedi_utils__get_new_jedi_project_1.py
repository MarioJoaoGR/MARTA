
import pytest
from thonny.jedi_utils import _get_new_jedi_project
import jedi


def test_invalid_input():
    invalid_sys_path = []
    project = _get_new_jedi_project(invalid_sys_path)
    assert project is None, "Expected None since the input list is empty"