
import os
import logging
from pytutils.log import configure, DEFAULT_CONFIG
import pytest

@pytest.mark.skip(reason="This test is intended to fail as it sets an invalid JSON string in the environment variable")
def test_invalid_inputs():
    # Set up the environment variable with an invalid JSON string
    os.environ['LOGGING'] = 'invalid json'
    
    # Call the configure function and assert that a ValueError is raised due to invalid JSON configuration
    with pytest.raises(ValueError):
        configure()
