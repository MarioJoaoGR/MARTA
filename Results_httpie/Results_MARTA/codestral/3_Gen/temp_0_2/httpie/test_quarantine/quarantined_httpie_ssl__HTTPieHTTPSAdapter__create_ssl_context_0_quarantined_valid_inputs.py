
import ssl
from httpie.ssl_ import resolve_ssl_version, ensure_default_certs_loaded
from urllib3.util.ssl_ import create_urllib3_context
from requests.adapters import HTTPAdapter

class HTTPieHTTPSAdapter(HTTPAdapter):
    """
    A custom HTTPS adapter for HTTPie that configures SSL/TLS settings.
    
    This class initializes an SSL context with specified verification and cipher settings, ensuring default certificates are loaded into the provided SSL context.
    
    Parameters:
        verify (bool): Whether to verify the server's TLS certificate. If True, the server's certificate must be verified; if False, it will not be verified.
        ssl_version (str, optional): The version of the SSL protocol to use. This should be one of the valid string arguments for `ssl.create_default_context()`. If None, a default version is used.
        ciphers (str, optional): A string specifying the enabled ciphers and protocols in standard cipher suite notation. If None, no specific ciphers are set.
        
    Returns:
        None
        
    Example:
        To use this class with HTTPie, you would create an instance of it like so:
        
        ```python
        from requests import Session
        from httpie_https_adapter import HTTPieHTTPSAdapter
        
        session = Session()
        session.mount('https://', HTTPieHTTPSAdapter(verify=True))
        ```
    
    Note:
        The `ssl_version` parameter should be one of the valid string arguments for `ssl.create_default_context()`. If not specified, a default SSL version is used. The `ciphers` parameter allows you to specify which ciphers and protocols are enabled in the SSL context. If not provided, no specific ciphers are set.
    """
    
    def __init__(self, verify: bool, ssl_version: str = None, ciphers: str = None, **kwargs):
        self._ssl_context = self._create_ssl_context(verify=verify, ssl_version=ssl_version, ciphers=ciphers)
        super().__init__(**kwargs)
    
    def _create_ssl_context(self, verify: bool, ssl_version: str = None, ciphers: str = None):
        ssl_context = create_urllib3_context(
            ciphers=ciphers,
            ssl_version=resolve_ssl_version(ssl_version),
            cert_reqs=ssl.CERT_REQUIRED if verify else ssl.CERT_NONE
        )
        ensure_default_certs_loaded(ssl_context)
        return ssl_context

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
============================ no tests ran in 0.10s =============================
"""