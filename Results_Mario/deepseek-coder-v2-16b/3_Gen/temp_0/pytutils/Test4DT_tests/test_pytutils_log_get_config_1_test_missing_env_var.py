
import os
import pytest
from pytutils.log import get_config

def test_missing_env_var():
    # Test when env_var is provided but no corresponding environment variable exists
    with pytest.raises(ValueError):
        config = get_config(env_var='NONEXISTENT_ENV_VAR')
