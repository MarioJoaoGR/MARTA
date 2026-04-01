
import os
import logging
from pytutils.log import configure
import pytest

@pytest.mark.skip(reason="This test is not yet implemented")
def test_none_config():
    log = logging.getLogger(__name__)
    with pytest.raises(TypeError):
        configure()
    assert log.hasHandlers() == False, "Expected no handlers to be configured"
