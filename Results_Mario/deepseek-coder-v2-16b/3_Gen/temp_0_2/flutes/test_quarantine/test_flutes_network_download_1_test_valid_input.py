
import os
import tempfile
import tarfile
import zipfile
from unittest.mock import patch
import pytest
from flutes.network import download

@pytest.mark.parametrize("url, save_dir, filename", [
    ('http://example.com/file.zip', None, 'file.zip'),
    ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view', tempfile.gettempdir(), 'file_from_drive.zip')
])
@patch('flutes.network.tarfile.is_tarfile')
@patch('flutes.network.zipfile.is_zipfile')
@patch('flutes.network.os.path.exists', return_value=False)
@patch('flutes.network._download', return_value='/temp/path/to/file')
def test_valid_input(mock_download, mock_exists, mock_is_zipfile, mock_is_tarfile, url, save_dir, filename):
    # Mock the tarfile and zipfile checks to always return False since we want to simulate a new download
    mock_is_tarfile.return_value = False
    mock_is_zipfile.return_value = False

    result = download(url, save_dir, filename, extract=False, progress=False)
    assert os.path.exists(result), f"Expected file to exist at {result}, but it does not."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_network_download_1_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________ test_valid_input[http://example.com/file.zip-None-file.zip] __________

mock_download = <MagicMock name='_download' id='140378577668240'>
mock_exists = <MagicMock name='exists' id='140378589927184'>
mock_is_zipfile = <MagicMock name='is_zipfile' id='140378574492752'>
mock_is_tarfile = <MagicMock name='is_tarfile' id='140378574498064'>
url = 'http://example.com/file.zip', save_dir = None, filename = 'file.zip'

    @pytest.mark.parametrize("url, save_dir, filename", [
        ('http://example.com/file.zip', None, 'file.zip'),
        ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view', tempfile.gettempdir(), 'file_from_drive.zip')
    ])
    @patch('flutes.network.tarfile.is_tarfile')
    @patch('flutes.network.zipfile.is_zipfile')
    @patch('flutes.network.os.path.exists', return_value=False)
    @patch('flutes.network._download', return_value='/temp/path/to/file')
    def test_valid_input(mock_download, mock_exists, mock_is_zipfile, mock_is_tarfile, url, save_dir, filename):
        # Mock the tarfile and zipfile checks to always return False since we want to simulate a new download
        mock_is_tarfile.return_value = False
        mock_is_zipfile.return_value = False
    
        result = download(url, save_dir, filename, extract=False, progress=False)
>       assert os.path.exists(result), f"Expected file to exist at {result}, but it does not."
E       AssertionError: Expected file to exist at /temp/path/to/file, but it does not.
E       assert False
E        +  where False = <MagicMock name='exists' id='140378589927184'>('/temp/path/to/file')
E        +    where <MagicMock name='exists' id='140378589927184'> = <module 'posixpath' (frozen)>.exists
E        +      where <module 'posixpath' (frozen)> = os.path

flutes/Test4DT_tests/test_flutes_network_download_1_test_valid_input.py:24: AssertionError
_ test_valid_input[https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view-/tmp-file_from_drive.zip] _

mock_download = <MagicMock name='_download' id='140378574429584'>
mock_exists = <MagicMock name='exists' id='140378574324944'>
mock_is_zipfile = <MagicMock name='is_zipfile' id='140378577840848'>
mock_is_tarfile = <MagicMock name='is_tarfile' id='140378574499856'>
url = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view'
save_dir = '/tmp', filename = 'file_from_drive.zip'

    @pytest.mark.parametrize("url, save_dir, filename", [
        ('http://example.com/file.zip', None, 'file.zip'),
        ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view', tempfile.gettempdir(), 'file_from_drive.zip')
    ])
    @patch('flutes.network.tarfile.is_tarfile')
    @patch('flutes.network.zipfile.is_zipfile')
    @patch('flutes.network.os.path.exists', return_value=False)
    @patch('flutes.network._download', return_value='/temp/path/to/file')
    def test_valid_input(mock_download, mock_exists, mock_is_zipfile, mock_is_tarfile, url, save_dir, filename):
        # Mock the tarfile and zipfile checks to always return False since we want to simulate a new download
        mock_is_tarfile.return_value = False
        mock_is_zipfile.return_value = False
    
>       result = download(url, save_dir, filename, extract=False, progress=False)

flutes/Test4DT_tests/test_flutes_network_download_1_test_valid_input.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/network.py:70: in download
    filepath = _download_from_google_drive(url, filename, save_dir_str, bar_fn)
flutes/flutes/network.py:132: in _download_from_google_drive
    response = sess.get(gurl, params={'id': file_id}, stream=True)
/usr/local/lib/python3.11/site-packages/requests/sessions.py:602: in get
    return self.request("GET", url, **kwargs)
/usr/local/lib/python3.11/site-packages/requests/sessions.py:589: in request
    resp = self.send(prep, **send_kwargs)
/usr/local/lib/python3.11/site-packages/requests/sessions.py:703: in send
    r = adapter.send(request, **kwargs)
/usr/local/lib/python3.11/site-packages/requests/adapters.py:616: in send
    self.cert_verify(conn, request.url, verify, cert)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <requests.adapters.HTTPAdapter object at 0x7fac6f0ea150>
conn = <urllib3.connectionpool.HTTPSConnectionPool object at 0x7fac6f155750>
url = 'https://docs.google.com/uc?export=download&id=1aBcD2eF3gHiJkLmNoPqRsT'
verify = True, cert = None

    def cert_verify(self, conn, url, verify, cert):
        """Verify a SSL certificate. This method should not be called from user
        code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
    
        :param conn: The urllib3 connection object associated with the cert.
        :param url: The requested URL.
        :param verify: Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use
        :param cert: The SSL certificate to verify.
        """
        if url.lower().startswith("https") and verify:
            cert_loc = None
    
            # Allow self-specified cert location.
            if verify is not True:
                cert_loc = verify
    
            if not cert_loc:
                cert_loc = extract_zipped_paths(DEFAULT_CA_BUNDLE_PATH)
    
            if not cert_loc or not os.path.exists(cert_loc):
>               raise OSError(
                    f"Could not find a suitable TLS CA certificate bundle, "
                    f"invalid path: {cert_loc}"
                )
E               OSError: Could not find a suitable TLS CA certificate bundle, invalid path: /usr/local/lib/python3.11/site-packages/certifi/cacert.pem

/usr/local/lib/python3.11/site-packages/requests/adapters.py:303: OSError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network_download_1_test_valid_input.py::test_valid_input[http:/example.com/file.zip-None-file.zip]
FAILED flutes/Test4DT_tests/test_flutes_network_download_1_test_valid_input.py::test_valid_input[https:/drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view-/tmp-file_from_drive.zip]
============================== 2 failed in 0.30s ===============================
"""