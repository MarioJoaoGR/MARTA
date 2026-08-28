
import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path
import os
import toml


def test_get_collection_name_from_path_invalid():
    input_path = '/some/other/path/file.txt'
    expected = None
    assert _get_collection_name_from_path(input_path) == expected

def test_get_collection_name_from_path_empty():
    input_path = ''
    expected = None
    assert _get_collection_name_from_path(input_path) == expected

def test_get_collection_name_from_path_none():
    input_path = None
    expected = None
    assert _get_collection_name_from_path(input_path) == expected