
import pytest
from unittest.mock import patch, MagicMock
import yaml
from io import StringIO
from ansible.parsing.utils.yaml import _safe_load

def test_safe_load_string():
    # Sample YAML content as a string
    yaml_data = """
    key: value
    list:
      - item1
      - item2
    """
    
    stream = StringIO(yaml_data)
    loaded_data = _safe_load(stream)
    assert loaded_data == {'key': 'value', 'list': ['item1', 'item2']}

