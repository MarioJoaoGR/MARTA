
import os
import logging
from pytutils.log import configure, DEFAULT_CONFIG
import pytest

@pytest.mark.skip(reason="This test is not yet implemented")
def test_invalid_env_var():
    # Set up the environment variable with an invalid value
    os.environ['LOGGING'] = 'invalid'
    
    # Call the configure function to trigger the logging configuration
    with pytest.raises(Exception):
        configure()
    
    # Check that no logging configuration was applied (e.g., by checking log messages)
    log = logging.getLogger(__name__)
    assert not hasattr(log, 'handlers')  # Assuming there are no handlers configured
