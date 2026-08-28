
import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class TestSimpleAsyncHTTPClient:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        self.client = SimpleAsyncHTTPClient()
    
    def test_release_fetch_with_valid_key(self):
        key = "test_key"
        self.client.active[key] = True
        assert key in self.client.active
        
        self.client._release_fetch(key)
        
        assert key not in self.client.active
    
    def test_release_fetch_with_none_key(self):
        with pytest.raises(KeyError):
            self.client._release_fetch(None)
