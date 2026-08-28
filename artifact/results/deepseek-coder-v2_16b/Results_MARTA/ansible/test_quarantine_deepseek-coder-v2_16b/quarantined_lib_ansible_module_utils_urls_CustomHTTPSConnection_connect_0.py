
import pytest
from ansible.module_utils.urls import CustomHTTPSConnection


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_CustomHTTPSConnection_connect_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_customhttpsconnection_basic _______________________

    def test_customhttpsconnection_basic():
        conn = CustomHTTPSConnection('example.com', 443)
        assert hasattr(conn, 'context'), "Expected the connection to have an SSL context"
>       assert not hasattr(conn, 'cert_file') and not hasattr(conn, 'key_file'), "Expected no certificate or key files to be set"
E       AssertionError: Expected no certificate or key files to be set
E       assert (not True)
E        +  where True = hasattr(<ansible.module_utils.urls.CustomHTTPSConnection object at 0x7f7f762fb280>, 'cert_file')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_CustomHTTPSConnection_connect_0.py:8: AssertionError
____________________ test_customhttpsconnection_with_certs _____________________

    def test_customhttpsconnection_with_certs():
>       conn = CustomHTTPSConnection('secure.example.com', 443, cert_file='path/to/cert.pem', key_file='path/to/key.pem')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_CustomHTTPSConnection_connect_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:519: in __init__
    httplib.HTTPSConnection.__init__(self, *args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.module_utils.urls.CustomHTTPSConnection object at 0x7f7f761f2e30>
host = 'secure.example.com', port = 443, key_file = 'path/to/key.pem'
cert_file = 'path/to/cert.pem', timeout = <object object at 0x7f7f784bd080>
source_address = None

    def __init__(self, host, port=None, key_file=None, cert_file=None,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                 source_address=None, *, context=None,
                 check_hostname=None, blocksize=8192):
        super(HTTPSConnection, self).__init__(host, port, timeout,
                                              source_address,
                                              blocksize=blocksize)
        if (key_file is not None or cert_file is not None or
                    check_hostname is not None):
            import warnings
            warnings.warn("key_file, cert_file and check_hostname are "
                          "deprecated, use a custom context instead.",
                          DeprecationWarning, 2)
        self.key_file = key_file
        self.cert_file = cert_file
        if context is None:
            context = ssl._create_default_https_context()
            # send ALPN extension to indicate HTTP/1.1 protocol
            if self._http_vsn == 11:
                context.set_alpn_protocols(['http/1.1'])
            # enable PHA for TLS 1.3 connections if available
            if context.post_handshake_auth is not None:
                context.post_handshake_auth = True
        will_verify = context.verify_mode != ssl.CERT_NONE
        if check_hostname is None:
            check_hostname = context.check_hostname
        if check_hostname and not will_verify:
            raise ValueError("check_hostname needs a SSL context with "
                             "either CERT_OPTIONAL or CERT_REQUIRED")
        if key_file or cert_file:
>           context.load_cert_chain(cert_file, key_file)
E           FileNotFoundError: [Errno 2] No such file or directory

/opt/conda/envs/test4py_env/lib/python3.10/http/client.py:1456: FileNotFoundError
=============================== warnings summary ===============================
test_lib_ansible_module_utils_urls_CustomHTTPSConnection_connect_0.py::test_customhttpsconnection_with_certs
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:519: DeprecationWarning: key_file, cert_file and check_hostname are deprecated, use a custom context instead.
    httplib.HTTPSConnection.__init__(self, *args, **kwargs)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_CustomHTTPSConnection_connect_0.py::test_customhttpsconnection_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_CustomHTTPSConnection_connect_0.py::test_customhttpsconnection_with_certs
========================= 2 failed, 1 warning in 0.45s =========================
"""