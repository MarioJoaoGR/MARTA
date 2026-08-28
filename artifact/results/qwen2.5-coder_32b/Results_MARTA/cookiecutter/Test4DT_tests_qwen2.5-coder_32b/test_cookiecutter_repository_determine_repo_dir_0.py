
import os
import tempfile
import shutil
import pytest
from unittest.mock import patch
from cookiecutter.repository import determine_repo_dir, RepositoryNotFound

def create_temp_directory():
    """Create a temporary directory and return its path."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def local_template(tmp_path):
    template_dir = tmp_path / "local_template"
    template_dir.mkdir()
    (template_dir / "cookiecutter.json").write_text("{}")
    return str(template_dir)

@pytest.fixture
def zip_file(tmp_path, local_template):
    import zipfile

    zip_path = tmp_path / "template.zip"
    with zipfile.ZipFile(zip_path, 'w') as zf:
        for root, _, files in os.walk(local_template):
            for file in files:
                zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), local_template))
    return str(zip_path)


def test_determine_repo_dir_with_abbreviation(tmp_path):
    template = 'proj:api'
    abbreviations = {'proj': str(tmp_path / 'project-{}')}
    clone_to_dir = tmp_path / "clones"
    checkout = None
    no_input = False

    project_api_dir = tmp_path / "project-api"
    project_api_dir.mkdir()
    (project_api_dir / "cookiecutter.json").write_text("{}")

    with patch('cookiecutter.repository.expand_abbreviations', return_value=str(project_api_dir)):
        repo_dir, cleanup = determine_repo_dir(
            template=template,
            abbreviations=abbreviations,
            clone_to_dir=clone_to_dir,
            checkout=checkout,
            no_input=no_input
        )

    assert repo_dir == str(project_api_dir)
    assert not cleanup

def test_determine_repo_dir_with_remote_url(tmp_path):
    template = 'https://github.com/user/repo.git'
    abbreviations = {}
    clone_to_dir = tmp_path / "clones"
    checkout = 'feature-branch'
    no_input = True

    cloned_repo = tmp_path / "repo"
    cloned_repo.mkdir()
    (cloned_repo / "cookiecutter.json").write_text("{}")

    with patch('cookiecutter.repository.clone', return_value=str(cloned_repo)):
        repo_dir, cleanup = determine_repo_dir(
            template=template,
            abbreviations=abbreviations,
            clone_to_dir=clone_to_dir,
            checkout=checkout,
            no_input=no_input
        )

    assert repo_dir == str(cloned_repo)
    assert not cleanup

def test_determine_repo_dir_with_subdirectory(tmp_path):
    template = 'https://github.com/user/repo.git'
    abbreviations = {}
    clone_to_dir = tmp_path / "clones"
    checkout = None
    no_input = False
    directory = 'subdir'

    cloned_repo = tmp_path / "repo"
    cloned_repo.mkdir()
    subdir = cloned_repo / "subdir"
    subdir.mkdir()
    (subdir / "cookiecutter.json").write_text("{}")

    with patch('cookiecutter.repository.clone', return_value=str(cloned_repo)):
        repo_dir, cleanup = determine_repo_dir(
            template=template,
            abbreviations=abbreviations,
            clone_to_dir=clone_to_dir,
            checkout=checkout,
            no_input=no_input,
            directory=directory
        )

    assert repo_dir == str(subdir)
    assert not cleanup

def test_determine_repo_dir_with_zip_file(zip_file, tmp_path):
    template = zip_file
    abbreviations = {}
    clone_to_dir = tmp_path / "clones"
    checkout = None
    no_input = True
    password = 'secret_password'

    unzipped_dir = tmp_path / "unzipped"
    unzipped_dir.mkdir()
    (unzipped_dir / "cookiecutter.json").write_text("{}")

    with patch('cookiecutter.repository.unzip', return_value=str(unzipped_dir)):
        repo_dir, cleanup = determine_repo_dir(
            template=template,
            abbreviations=abbreviations,
            clone_to_dir=clone_to_dir,
            checkout=checkout,
            no_input=no_input,
            password=password
        )

    assert repo_dir == str(unzipped_dir)
    assert cleanup
