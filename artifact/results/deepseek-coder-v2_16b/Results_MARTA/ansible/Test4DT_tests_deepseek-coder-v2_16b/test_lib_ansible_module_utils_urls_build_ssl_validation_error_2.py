
import pytest
from ansible.module_utils.urls import SSLValidationError

def build_ssl_validation_error(hostname, port, paths, exc=None):
    msg = [
        ('Failed to validate the SSL certificate for %s:%s.'
         ' Make sure your managed systems have a valid CA'
         ' certificate installed.')
    ]
    if not HAS_SSLCONTEXT:
        msg.append('If the website serving the url uses SNI you need'
                   ' python >= 2.7.9 on your managed machine')
        msg.append(' (the python executable used (%s) is version: %s)' %
                   (sys.executable, ''.join(sys.version.splitlines())))
        if not HAS_URLLIB3_PYOPENSSLCONTEXT and not HAS_URLLIB3_SSL_WRAP_SOCKET:
            msg.append('or you can install the `urllib3`, `pyOpenSSL`,'
                       ' `ndg-httpsclient`, and `pyasn1` python modules')

        msg.append('to perform SNI verification in python >= 2.6.')

    msg.append('You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.'
               ' Paths checked for this platform: %s.')

    if exc:
        msg.append('The exception msg was: %s.' % to_native(exc))

    raise SSLValidationError(' '.join(msg) % (hostname, port, ", ".join(paths)))

# Test scenarios
def test_valid_input():
    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error('example.com', 443, ['https://example.com'])
    assert str(excinfo.value) == (
        'Failed to validate the SSL certificate for example.com:443.'
        ' Make sure your managed systems have a valid CA certificate installed.'
        ' Paths checked for this platform: https://example.com.'
    )

def test_edge_case_none():
    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(None, None, None)
    assert str(excinfo.value) == (
        'Failed to validate the SSL certificate for None:None.'
        ' Make sure your managed systems have a valid CA certificate installed.'
        ' Paths checked for this platform: .'
    )

def test_invalid_input():
    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error('invalidhost', 12345, ['https://example.com'])
    assert str(excinfo.value) == (
        'Failed to validate the SSL certificate for invalidhost:12345.'
        ' Make sure your managed systems have a valid CA certificate installed.'
        ' Paths checked for this platform: https://example.com.'
    )
