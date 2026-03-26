
import pytest
from pytutils.log import get_config

def test_edge_cases():
    # Test with None values
    with pytest.raises(ValueError, match="Invalid logging config: None"):
        assert get_config(given=None, env_var=None, default=None) is None
