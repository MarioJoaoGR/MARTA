
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.base import TransportPlugin

class TestTransportPlugin:
    def test_invalid_inputs(self):
        # Create an instance of the base class without overriding get_adapter
        plugin = TransportPlugin()
        
        with pytest.raises(NotImplementedError):
            # Attempt to call get_adapter on the base class, which should raise NotImplementedError
            plugin.get_adapter()
