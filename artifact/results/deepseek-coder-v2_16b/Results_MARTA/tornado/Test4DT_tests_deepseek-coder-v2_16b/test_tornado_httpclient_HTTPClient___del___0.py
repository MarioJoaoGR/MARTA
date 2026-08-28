
import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPError

class TestHTTPClient:
    @pytest.mark.asyncio
    async def test_fetch_google(self):
        http_client = HTTPClient()
        try:
            response = await http_client.fetch("http://www.google.com/")
            assert response is not None
            assert isinstance(response, dict)  # Assuming the response is a dictionary-like object
            print(response.body)  # This will print the body of the response for debugging purposes
        except HTTPError as e:
            pytest.fail(f"HTTP request failed with error {str(e)}")
        finally:
            http_client.close()

    @pytest.mark.asyncio
    async def test_fetch_nonexistent(self):
        http_client = HTTPClient()
        try:
            with pytest.raises(HTTPError) as excinfo:
                await http_client.fetch("http://www.nonexistentdomain.com/")
            assert "Not Found" in str(excinfo.value)  # Assuming the error message contains "Not Found"
        except HTTPError as e:
            pytest.fail(f"HTTP request failed with unexpected error {str(e)}")
        finally:
            http_client.close()

    @pytest.mark.asyncio
    async def test_custom_async_http_client(self):
        from tornado.httpclient import AsyncHTTPClient

        class CustomAsyncHTTPClient(AsyncHTTPClient):
            pass  # Define your custom logic here if necessary

        http_client = HTTPClient(async_client_class=CustomAsyncHTTPClient)
        try:
            response = await http_client.fetch("http://www.google.com/")
            assert response is not None
            assert isinstance(response, dict)  # Assuming the response is a dictionary-like object
            print(response.body)  # This will print the body of the response for debugging purposes
        except HTTPError as e:
            pytest.fail(f"HTTP request failed with error {str(e)}")
        finally:
            http_client.close()
