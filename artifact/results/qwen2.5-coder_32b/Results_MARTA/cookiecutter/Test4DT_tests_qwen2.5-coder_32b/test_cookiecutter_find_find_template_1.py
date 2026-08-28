
import os
import tempfile
import shutil
import pytest
from cookiecutter.exceptions import NonTemplatedInputDirException
from cookiecutter.find import find_template

def setup_happy_path(tmpdir):
    repo_dir = tmpdir.mkdir('repo')
    template_dir = repo_dir.mkdir('cookiecutter-my-template')
    with open(os.path.join(template_dir, 'README.md'), 'w') as f:
        f.write("{{ project_name }}")
    return str(repo_dir)

def setup_edge_case_empty_directory(tmpdir):
    repo_dir = tmpdir.mkdir('repo')
    return str(repo_dir)



def test_edge_case_no_matching_directory():
    with tempfile.TemporaryDirectory() as tmpdir_for_tests:
        repo_dir = os.path.join(tmpdir_for_tests, 'repo')
        os.makedirs(repo_dir)
        template_dir = os.path.join(repo_dir, 'my-template')
        os.makedirs(template_dir)
        with open(os.path.join(template_dir, 'README.md'), 'w') as f:
            f.write("{{ project_name }}")
        with pytest.raises(NonTemplatedInputDirException):
            find_template(repo_dir)
