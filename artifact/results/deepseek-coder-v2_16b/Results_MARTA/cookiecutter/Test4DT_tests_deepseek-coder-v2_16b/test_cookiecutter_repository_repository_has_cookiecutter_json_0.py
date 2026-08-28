
import os
import pytest
from cookiecutter.repository import repository_has_cookiecutter_json


def test_invalid_directory():
    repo_directory = '/nonexistent/directory'
    assert repository_has_cookiecutter_json(repo_directory) is False

def test_directory_without_cookiecutter_json():
    repo_directory = '/existing/directory'
    assert not os.path.isfile(os.path.join(repo_directory, 'cookiecutter.json'))
    assert repository_has_cookiecutter_json(repo_directory) is False