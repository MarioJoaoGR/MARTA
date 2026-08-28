
import os
import tempfile
import shutil
import pytest
from cookiecutter.find import find_template
from cookiecutter.exceptions import NonTemplatedInputDirException

def create_temp_repo_with_template(template_name):
    repo_dir = tempfile.mkdtemp()
    template_dir = os.path.join(repo_dir, template_name)
    os.makedirs(template_dir)
    with open(os.path.join(template_dir, 'cookiecutter.json'), 'w') as f:
        f.write('{}')
    return repo_dir, template_dir



def test_no_valid_template():
    """Test with a repository directory containing no valid template directories."""
    repo_dir = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(repo_dir, 'other-directory'))
        with pytest.raises(NonTemplatedInputDirException):
            find_template(repo_dir)
    finally:
        shutil.rmtree(repo_dir)

def test_invalid_template_name():
    """Test with a repository directory containing a template directory with an invalid name."""
    repo_dir = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(repo_dir, 'invalid-template-name'))
        with pytest.raises(NonTemplatedInputDirException):
            find_template(repo_dir)
    finally:
        shutil.rmtree(repo_dir)

def test_empty_repository():
    """Test with an empty repository directory."""
    repo_dir = tempfile.mkdtemp()
    try:
        with pytest.raises(NonTemplatedInputDirException):
            find_template(repo_dir)
    finally:
        shutil.rmtree(repo_dir)