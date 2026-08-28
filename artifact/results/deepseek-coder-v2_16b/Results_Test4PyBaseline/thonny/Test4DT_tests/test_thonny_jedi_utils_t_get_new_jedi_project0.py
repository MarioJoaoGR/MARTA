
import pytest
from thonny.jedi_utils import _get_new_jedi_project
import jedi

# Test cases for _get_new_jedi_project function

def test_non_empty_list():
    sys_path = ['/path/to/project']
    project = _get_new_jedi_project(sys_path)
    assert isinstance(project, jedi.Project), "Expected a Jedi Project instance"