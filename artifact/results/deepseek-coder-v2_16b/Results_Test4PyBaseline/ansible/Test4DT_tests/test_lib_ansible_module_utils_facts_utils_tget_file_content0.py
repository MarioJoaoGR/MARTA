
import os
import fcntl
from ansible.module_utils.facts.utils import get_file_content

def test_get_file_content_basic():
    assert get_file_content('example.txt') == 'This is the content of example.txt.'

def test_get_file_content_nonexistent():
    assert get_file_content('nonexistent.txt', 'File not found') == 'File not found'

def test_get_file_content_strip_whitespace():
    assert get_file_content('whitespace.txt', strip=True) == 'No leading or trailing whitespace here.'

def test_get_file_content_empty_with_default():
    assert get_file_content('empty.txt', 'Empty file') == 'Empty file'

def test_get_file_content_all_parameters():
    assert get_file_content('example.txt', 'Default content', False) == 'Default content'
