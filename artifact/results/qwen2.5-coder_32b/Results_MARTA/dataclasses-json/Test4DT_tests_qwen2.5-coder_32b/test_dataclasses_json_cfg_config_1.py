
import pytest
from dataclasses_json.cfg import config, Undefined

def test_config_basic():
    # Test basic functionality without any parameters
    metadata = config()
    assert metadata == {'dataclasses_json': {}}
