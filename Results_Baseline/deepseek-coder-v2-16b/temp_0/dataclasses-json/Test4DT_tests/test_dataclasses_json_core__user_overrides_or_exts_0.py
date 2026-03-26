
import pytest
from dataclasses import dataclass, fields
from collections import defaultdict
from dataclasses_json.core import _user_overrides_or_exts

# Example configuration settings
cfg = {
    'global_config': {
        'encoders': {'int': lambda x: str(x)},
        'decoders': {},
        'mm_fields': {}
    }
}

@dataclass
class ExampleConfig:
    pass

def test_example():
    with pytest.raises(TypeError):
        assert _user_overrides_or_exts(cfg) is None
