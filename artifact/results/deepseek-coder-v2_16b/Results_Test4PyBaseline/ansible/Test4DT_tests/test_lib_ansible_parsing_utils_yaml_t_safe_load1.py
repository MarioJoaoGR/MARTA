
import pytest
from ansible.parsing.utils.yaml import _safe_load
import yaml

def test_safe_load_with_valid_stream():
    valid_yaml = "key: value"
    data = _safe_load(valid_yaml)
    assert isinstance(data, dict), "Expected a dictionary but got something else."