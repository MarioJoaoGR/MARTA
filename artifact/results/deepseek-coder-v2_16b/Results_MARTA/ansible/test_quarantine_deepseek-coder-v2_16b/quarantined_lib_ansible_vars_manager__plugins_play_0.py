
import pytest
from ansible.vars.manager import _plugins_play

def test_basic_usage():
    entities = {
        "dir1": {"file1": {"play": 1}, "file2": {"play": 2}},
        "dir2": {"file3": {"play": 3}}
    }
    result = _plugins_play(entities)
    assert result == {
        "dir1": {"file1": {"play": 1}, "file2": {"play": 2}},
        "dir2": {"file3": {"play": 3}}
    }

def test_empty_dictionary():
    entities = {}
    result = _plugins_play(entities)
    assert result == {}

def test_nested_structures():
    entities = {
        "dir1": {"file1": {"play": {"nested_key": "value"}}, "file2": {"play": 2}},
        "dir2": {"file3": {"play": 3, "additional_file": {"play": {"nested_key": "new_value"}}}, "file4": {"play": 4}}
    }
    result = _plugins_play(entities)
    assert result == {
        "dir1": {"file1": {"play": {"nested_key": "value"}}, "file2": {"play": 2}},
        "dir2": {"file3": {"play": 3, "additional_file": {"play": {"nested_key": "new_value"}}}, "file4": {"play": 4}}
    }

def test_single_path_with_multiple_entities():
    entities = {
        "dir1": {"file1": {"play": 1}, "file2": {"play": 2}},
        "dir2": {"file3": {"play": 3}},
        "dir3": {"file4": {"play": 4}, "file5": {"play": 5}}
    }
    result = _plugins_play(entities)
    assert result == {
        "dir1": {"file1": {"play": 1}, "file2": {"play": 2}},
        "dir2": {"file3": {"play": 3}},
        "dir3": {"file4": {"play": 4}, "file5": {"play": 5}}
    }

def test_large_dictionary_with_overlapping_keys():
    entities = {
        "dir1": {"file1": {"play": {"key1": "value1"}}, "file2": {"play": {"key2": "value2"}}},
        "dir2": {"file3": {"play": {"key3": "value3"}, "additional_file": {"play": {"key4": "value4"}}}},
        "dir3": {"file4": {"play": {"key5": "value5"}, "file5": {"play": {"key6": "value6"}}}
    }
    result = _plugins_play(entities)
    assert result == {
        "dir1": {"file1": {"play": {"key1": "value1"}}, "file2": {"play": {"key2": "value2"}}},
        "dir2": {"file3": {"play": {"key3": "value3"}, "additional_file": {"play": {"key4": "value4"}}}},
        "dir3": {"file4": {"play": {"key5": "value5"}, "file5": {"play": {"key6": "value6"}}}
    }

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax. Perhaps you forgot a comma? (line 49, col 17)
        "dir3": {"file4": {"play": {"key5": "value5"}, "file5": {"play": {"key6": "value6"}}}
"""