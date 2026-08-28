
import os
import tempfile
import shutil
import zipfile
from unittest.mock import patch

import pytest
from cookiecutter.zipfile import unzip, InvalidZipRepository


def create_temp_zip(password=None):
    """Create a temporary zip file for testing."""
    temp_dir = tempfile.mkdtemp()
    inner_dir = os.path.join(temp_dir, 'test_project')
    os.makedirs(inner_dir)
    with open(os.path.join(inner_dir, 'file.txt'), 'w') as f:
        f.write('Hello, World!')

    zip_path = os.path.join(temp_dir, 'test.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(inner_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                if password:
                    zf.setpassword(password.encode('utf-8'))
                zf.write(file_path, arcname)

    return zip_path






def test_unzip_local_zip_existing_directory_no_input():
    zip_path = create_temp_zip()
    clone_to_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(clone_to_dir, 'test_project'))
    with pytest.raises(InvalidZipRepository):
        unzip(zip_path, is_url=False, clone_to_dir=clone_to_dir, no_input=True)


def test_unzip_local_zip_existing_file_no_input():
    zip_path = create_temp_zip()
    clone_to_dir = tempfile.mkdtemp()
    with open(os.path.join(clone_to_dir, 'test_project'), 'w') as f:
        f.write('This is a test file.')
    with pytest.raises(InvalidZipRepository):
        unzip(zip_path, is_url=False, clone_to_dir=clone_to_dir, no_input=True)



