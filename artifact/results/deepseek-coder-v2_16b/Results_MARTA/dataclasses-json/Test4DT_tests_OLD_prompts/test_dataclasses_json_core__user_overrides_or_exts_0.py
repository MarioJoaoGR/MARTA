
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from collections import defaultdict
from unittest.mock import patch

# Assuming the function _user_overrides_or_exts is defined in a module named 'dataclasses_json.core'
from dataclasses_json.core import _user_overrides_or_exts

@pytest.fixture(scope="module")
def config():
    class Config:
        encoders = {str: lambda x: f"encoded_{x}"}
        decoders = {str: lambda x: x.replace("encoded_", "")}
        mm_fields = {str: lambda x: {"type": "custom"}}
    
    cfg.global_config = Config()
    return cfg.global_config


def test_invalid_input():
    with pytest.raises(TypeError):
        @dataclass
        class YourDataclass:
            field1: str = fields(metadata={"dataclasses_json": {"encoder": lambda x: f"encoded_{x}", "decoder": lambda x: x.replace("encoded_", "")}})

if __name__ == "__main__":
    pytest.main()