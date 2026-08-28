
import pytest
from tornado import httpclient, gen
from unittest.mock import patch

class TestHTTPClientClose:
    @pytest.mark.asyncio
    async def test_httpclient_close(self):
        with patch('tornado.httpclient.AsyncHTTPClient') as mock_async_client:
            http_client = httpclient.HTTPClient()
            await gen.sleep(0)  # Allow time for the client to be initialized
            
            assert not http_client._closed, "HTTPClient should not be closed initially"
            
            http_client.close()
            assert http_client._closed, "HTTPClient should be closed after calling close()"
            
            mock_async_client.assert_called_once(), "AsyncHTTPClient should be instantiated once"
