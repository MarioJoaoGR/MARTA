
import os
import tempfile
import shutil
import pytest
from zipfile import ZipFile, BadZipFile
from cookiecutter.zipfile import unzip, InvalidZipRepository

def create_zip_file(zip_path, files=None):
    """Helper function to create a zip file with optional files."""
    if files is None:
        files = {'test.txt': 'This is a test file.'}
    
    with ZipFile(zip_path, 'w') as zipf:
        for filename, content in files.items():
            zipf.writestr(filename, content)

def create_protected_zip_file(zip_path, password='testpassword', files=None):
    """Helper function to create a password-protected zip file."""
    if files is None:
        files = {'protected_test.txt': 'This is a protected test file.'}
    
    with ZipFile(zip_path, 'w') as zipf:
        for filename, content in files.items():
            zipf.writestr(filename, content)
    
    # Reopen the zip file to set the password
    with ZipFile(zip_path, 'a', compression=ZipFile.ZIP_DEFLATED) as zipf:
        for filename in files.keys():
            zipf.setpassword(password.encode('utf-8'))

@pytest.fixture(scope='function')
def valid_zip_path(temp_dir):
    """Fixture to create a valid zip file."""
    zip_path = os.path.join(temp_dir, 'repo.zip')
    create_zip_file(zip_path)
    return zip_path

@pytest.fixture(scope='function')
def password_protected_zip_path(temp_dir):
    """Fixture to create a password-protected zip file."""
    zip_path = os.path.join(temp_dir, 'protected_repo.zip')
    create_protected_zip_file(zip_path)
    return zip_path

@pytest.fixture(scope='function')
def temp_dir():
    """Fixture to create and clean up a temporary directory."""
    dir_path = tempfile.mkdtemp()
    yield dir_path
    shutil.rmtree(dir_path)






def test_empty_zip_file(temp_dir):
    """Test the scenario where the zip file is empty."""
    empty_zip_path = os.path.join(temp_dir, 'empty_repo.zip')
    create_zip_file(empty_zip_path, files={})
    
    with pytest.raises(InvalidZipRepository) as excinfo:
        unzip(empty_zip_path, is_url=False, clone_to_dir=temp_dir, no_input=True)
    assert "Zip repository {} is empty".format(empty_zip_path) in str(excinfo.value)

def test_no_top_level_directory(temp_dir):
    """Test the scenario where the zip file does not contain a top-level directory."""
    no_top_level_zip_path = os.path.join(temp_dir, 'no_top_level_repo.zip')
    create_zip_file(no_top_level_zip_path, files={'file1.txt': 'Content 1', 'file2.txt': 'Content 2'})
    
    with pytest.raises(InvalidZipRepository) as excinfo:
        unzip(no_top_level_zip_path, is_url=False, clone_to_dir=temp_dir, no_input=True)
    assert "does not include a top-level directory" in str(excinfo.value)