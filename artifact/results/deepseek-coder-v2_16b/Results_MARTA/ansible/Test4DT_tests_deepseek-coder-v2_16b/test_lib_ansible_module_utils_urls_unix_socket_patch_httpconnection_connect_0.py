
import pytest
from ansible.module_utils.urls import unix_socket_patch_httpconnection_connect

def test_unix_socket_patch_httpconnection_connect():
    """Test that the `httplib.HTTPConnection.connect` method is patched to `UnixHTTPConnection.connect`."""
    from ansible.module_utils.urls import httplib, UnixHTTPConnection
    
    # Save the original connect method
    original_connect = httplib.HTTPConnection.connect
    
    try:
        # Patch the connect method
        with unix_socket_patch_httpconnection_connect():
            assert isinstance(httplib.HTTPConnection.connect, type(UnixHTTPConnection.connect))
        
        # Assert that the original connect method is restored
        assert httplib.HTTPConnection.connect == original_connect
    
    except AssertionError as e:
        pytest.fail(f"Assertion failed: {e}")
