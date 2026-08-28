
import os
import tempfile
import shutil
import pytest
from cookiecutter.find import find_template
from cookiecutter.exceptions import NonTemplatedInputDirException

def setup_repo_with_template(tmpdir, template_name):
    repo_path = os.path.join(tmpdir, 'repo')
    os.mkdir(repo_path)
    template_dir = os.path.join(repo_path, template_name)
    os.mkdir(template_dir)
    with open(os.path.join(template_dir, 'dummy_file.txt'), 'w') as f:
        f.write('This is a dummy file.')
    return repo_path


def test_no_cookiecutter_in_name():
    with tempfile.TemporaryDirectory() as tmpdir:
        valid_repo_dir = setup_repo_with_template(tmpdir, 'my-template')
        with pytest.raises(NonTemplatedInputDirException):
            find_template(valid_repo_dir)

def test_no_jinja_placeholders():
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = os.path.join(tmpdir, 'repo')
        os.mkdir(repo_path)
        template_dir = os.path.join(repo_path, 'cookiecutter-my-template')
        os.mkdir(template_dir)
        with open(os.path.join(template_dir, 'dummy_file.txt'), 'w') as f:
            f.write('This is a dummy file without placeholders.')
        with pytest.raises(NonTemplatedInputDirException):
            find_template(repo_path)
