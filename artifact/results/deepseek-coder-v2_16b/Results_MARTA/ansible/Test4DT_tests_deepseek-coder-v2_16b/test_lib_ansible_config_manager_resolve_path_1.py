
import pytest
from ansible.config.manager import resolve_path
import os

def test_resolve_path_with_cwd():
    path = '{{CWD}}/data/file.txt'
    resolved_path = resolve_path(path)
    assert resolved_path == f"{os.getcwd()}/data/file.txt"

def test_resolve_path_without_cwd():
    path = '/home/user/project'
    resolved_path = resolve_path(path)
    assert resolved_path == '/home/user/project'

def test_resolve_path_with_basedir():
    path = 'data/file.txt'
    basedir = '/home/user'
    resolved_path = resolve_path(path, basedir=basedir)
    assert resolved_path == '/home/user/data/file.txt'
