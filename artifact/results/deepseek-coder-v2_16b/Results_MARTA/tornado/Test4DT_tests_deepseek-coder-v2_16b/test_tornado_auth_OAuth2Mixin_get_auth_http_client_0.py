
import pytest
from tornado import httpclient
from tornado.auth import OAuth2Mixin

class TestOAuth2Mixin:
    def test_get_auth_http_client(self):
        class MyOAuth2Subclass(httpclient.AsyncHTTPClient, OAuth2Mixin):
            pass
        
        my_mixin = MyOAuth2Subclass()
        http_client_instance = my_mixin.get_auth_http_client()
        assert isinstance(http_client_instance, httpclient.AsyncHTTPClient)
    
    def test_invalid_input_get_auth_http_client(self):
        class MyOAuth2Subclass(httpclient.AsyncHTTPClient, OAuth2Mixin):
            pass
        
        my_mixin = MyOAuth2Subclass()
        with pytest.raises(AttributeError):
            assert my_mixin._OAUTH_AUTHORIZE_URL is None
