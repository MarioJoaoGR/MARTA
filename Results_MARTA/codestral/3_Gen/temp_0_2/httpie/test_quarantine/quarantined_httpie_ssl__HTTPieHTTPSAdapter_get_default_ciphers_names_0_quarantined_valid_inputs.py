
import unittest
from httpie.ssl_ import SSLContext
from unittest.mock import patch, MagicMock

class HTTPieHTTPSAdapter:
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

    @classmethod
    def get_default_ciphers_names(cls):
        """
        Returns the default ciphers names used by the SSL context.
        
        This function retrieves the default ciphers names from the SSL context, which is created with verification disabled. The ciphers are obtained from the SSL context's available ciphers list.
        
        Parameters:
            None
        
        Returns:
            List[str]: A list of cipher names supported by the SSL context.
        
        Usage:
            To get the default ciphers names for use in cryptographic operations, call this function without any parameters. It will return a list of cipher names that can be used to configure or verify the ciphers in use.
        """
        with patch('httpie.ssl_.SSLContext', new=MagicMock()) as mock_ssl_context:
            ssl_context = cls._create_ssl_context(verify=False)
            return [cipher['name'] for cipher in ssl_context.get_ciphers()]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_valid_inputs.py:3:0: E0611: No name 'SSLContext' in module 'httpie.ssl_' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_valid_inputs.py:36:28: E1101: Instance of 'HTTPieHTTPSAdapter' has no '_create_ssl_context' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_valid_inputs.py:56:26: E1101: Class 'HTTPieHTTPSAdapter' has no '_create_ssl_context' member (no-member)


"""