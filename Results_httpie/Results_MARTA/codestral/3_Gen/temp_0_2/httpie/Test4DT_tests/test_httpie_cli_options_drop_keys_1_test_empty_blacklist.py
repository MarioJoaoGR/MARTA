
import pytest
from typing import Dict, Any, Tuple

def drop_keys(configuration: Dict[str, Any], key_blacklist: Tuple[str, ...]) -> Dict[str, Any]:
    return {key: value for key, value in configuration.items() if key not in key_blacklist}

@pytest.mark.parametrize("config, blacklist, expected", [({'a': 1, 'b': 2}, (), {'a': 1, 'b': 2})])
def test_empty_blacklist(config, blacklist, expected):
    assert drop_keys(config, blacklist) == expected
