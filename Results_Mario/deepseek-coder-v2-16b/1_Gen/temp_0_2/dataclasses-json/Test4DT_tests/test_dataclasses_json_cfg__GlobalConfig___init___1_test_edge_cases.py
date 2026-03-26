
import pytest
from dataclasses_json.cfg import _GlobalConfig

def test_edge_cases():
    # Test initialization with None
    config_none = _GlobalConfig()
    assert config_none.encoders == {}
    assert config_none.decoders == {}
    assert config_none.mm_fields == {}

    # Test initialization with empty lists
    config_empty = _GlobalConfig()
    assert config_empty.encoders == {}
    assert config_empty.decoders == {}
    assert config_empty.mm_fields == {}

    # Test boundary values (e.g., min/max int, float) if applicable
    # Since the class does not accept parameters and initializes empty dictionaries, no further boundary tests are needed for initialization
