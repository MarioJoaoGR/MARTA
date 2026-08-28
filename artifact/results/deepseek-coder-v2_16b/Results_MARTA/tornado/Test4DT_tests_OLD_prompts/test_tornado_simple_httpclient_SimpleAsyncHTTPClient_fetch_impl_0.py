
import pytest
from tornado import httpclient, gen
from unittest.mock import patch
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class TestSimpleAsyncHTTPClient:
    
    @pytest.mark.asyncio
    async def test_none_input(self):
        client = SimpleAsyncHTTPClient()
        
        with pytest.raises(TypeError) as excinfo:
            await client.fetch_impl(None, None)
        assert "takes 0 positional arguments but 1 was given" in str(excinfo.value)
    
    @pytest.mark.asyncio
    async def test_invalid_request(self):
        client = SimpleAsyncHTTPClient()
        
        with pytest.raises(TypeError) as excinfo:
            await client.fetch_impl("invalid_url", None)
        assert "takes 0 positional arguments but 1 was given" in str(excinfo.value)
    
    @pytest.mark.asyncio
    async def test_valid_request(self):
        client = SimpleAsyncHTTPClient()
        
        with patch('tornado.simple_httpclient.gen_log') as mock_gen_log:
            request = httpclient.HTTPRequest("http://example.com")
            await client.fetch_impl(request, lambda response: None)
            
            assert len(client.active) == 1
            assert len(client.queue) == 0
            mock_gen_log.debug.assert_called_with("max_clients limit reached, request queued. 1 active, 0 queued requests.")
