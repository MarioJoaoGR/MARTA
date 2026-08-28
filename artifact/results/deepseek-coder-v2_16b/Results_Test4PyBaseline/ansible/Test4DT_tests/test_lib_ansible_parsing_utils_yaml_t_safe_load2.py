
import pytest
from ansible.parsing.utils.yaml import _safe_load
import yaml

def test_load_with_ansibleloader():
    stream = "key: value"
    loader = _safe_load(stream)
    assert isinstance(loader, dict), "Expected a dictionary but got something else."