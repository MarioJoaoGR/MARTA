
from fnmatch import fnmatch

import pytest

from isort.place import _forced_separate


class Config:
    def __init__(self, forced_separate=[]):
        self.forced_separate = forced_separate

def test_basic_call():
    config_instance = Config(["*.log", "data.*"])
    result = _forced_separate("data.txt", config_instance)
    assert result == ('data.*', "Matched forced_separate (data.*) config value.")

def test_no_match_case():
    config_instance = Config(["*.utils", "math.*"])
    result = _forced_separate("os.path", config_instance)
    assert result is None

def test_edge_case_with_single_pattern():
    config_instance = Config(["log.*"])
    result = _forced_separate("log.error", config_instance)
    assert result == ('log.*', "Matched forced_separate (log.*) config value.")

def test_pattern_with_wildcard():
    config_instance = Config(["*.log"])
    result = _forced_separate("test.log", config_instance)
    assert result == ('*.log', "Matched forced_separate (*.log) config value.")
