
import argparse
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

class TestHTTPieArgumentParser:
    @patch('httpie.ssl_._is_key_file_encrypted', return_value=True)
    def test_process_ssl_cert_with_encrypted_key(self, mock_is_key_file_encrypted):
        parser = HTTPieArgumentParser()
        parser.args = argparse.Namespace(cert_key='path/to/cert', cert_key_pass=None)
        
        with patch('httpie.cli.argparser.SSLCredentials') as mock_sslcredentials:
            mock_sslcredentials.return_value = MagicMock()
            mock_sslcredentials.return_value.value = None
            
            parser._process_ssl_cert()
            
            assert parser.args.cert_key_pass is not None
            mock_sslcredentials.return_value.prompt_password.assert_called_with('path/to/cert')
