
import requests
from httpie.client import HTTPieHTTPAdapter, HTTPieHTTPSAdapter
from httpie.plugin_manager import plugin_manager

def build_requests_session(
    verify: bool,
    ssl_version: str = None,
    ciphers: str = None,
) -> requests.Session:
    """
    Creates and configures a `requests.Session` object with custom HTTP and HTTPS adapters that handle SSL/TLS settings.
    
    The function initializes an `HTTPieHTTPSAdapter` for HTTPS connections, configuring it with the provided verification setting and cipher suite. It also mounts additional transport plugins' adapters based on registered plugins.
    
    Parameters:
        verify (bool): Whether to verify the server's TLS certificate. If True, the server's certificate must be verified; if False, it will not be verified.
        ssl_version (str, optional): The version of the SSL protocol to use. This should be one of the valid string arguments for `ssl.create_default_context()`. If None, a default version is used.
        ciphers (str, optional): A string specifying the enabled ciphers and protocols in standard cipher suite notation. If None, no specific ciphers are set.
        
    Returns:
        requests.Session: A configured `requests.Session` object with custom HTTP and HTTPS adapters.
    """
    requests_session = requests.Session()

    # Install our adapter.
    http_adapter = HTTPieHTTPAdapter()
    https_adapter = HTTPieHTTPSAdapter(
        ciphers=ciphers,
        verify=verify,
        ssl_version=(
            AVAILABLE_SSL_VERSION_ARG_MAPPING[ssl_version]
            if ssl_version else None
        ),
    )
    requests_session.mount('http://', http_adapter)
    requests_session.mount('https://', https_adapter)

    # Install adapters from plugins.
    for plugin_cls in plugin_manager.get_transport_plugins():
        transport_plugin = plugin_cls()
        requests_session.mount(
            prefix=transport_plugin.prefix,
            adapter=transport_plugin.get_adapter(),
        )

    return requests_session

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_client_build_requests_session_0_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_build_requests_session_0_test_edge_cases.py:4:0: E0401: Unable to import 'httpie.plugin_manager' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_build_requests_session_0_test_edge_cases.py:4:0: E0611: No name 'plugin_manager' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_build_requests_session_0_test_edge_cases.py:32:12: E0602: Undefined variable 'AVAILABLE_SSL_VERSION_ARG_MAPPING' (undefined-variable)


"""