
from dataclasses import dataclass, fields
from collections import defaultdict
import pytest
from dataclasses_json.core import _user_overrides_or_exts

@dataclass
class YourDataclass:
    # Define your dataclass here with appropriate fields and metadata if necessary
    pass

def test_valid_input():
    overrides = _user_overrides_or_exts(YourDataclass)
    assert isinstance(overrides, dict), "The result should be a dictionary"
    for field in fields(YourDataclass):
        assert field.name in overrides, f"Field {field.name} should have an override or extension"
