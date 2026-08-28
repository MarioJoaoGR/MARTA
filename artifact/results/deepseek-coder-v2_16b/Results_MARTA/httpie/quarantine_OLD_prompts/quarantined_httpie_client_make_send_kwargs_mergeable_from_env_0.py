
import pytest
import argparse
from httpie.client import make_send_kwargs_mergeable_from_env



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_send_kwargs_mergeable_from_env_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        args = argparse.Namespace(cert='path/to/cert', cert_key='path/to/cert_key', proxy=[{'key': 'http', 'value': 'http://proxy'}, {'key': 'https', 'value': 'https://proxy'}], verify='yes')
>       kwargs = make_send_kwargs_mergeable_from_env(args)

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_send_kwargs_mergeable_from_env_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/client.py:230: in make_send_kwargs_mergeable_from_env
    'proxies': {p.key: p.value for p in args.proxy},
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f3b62a33f40>

>       'proxies': {p.key: p.value for p in args.proxy},
        'stream': True,
        'verify': {
            'yes': True,
            'true': True,
            'no': False,
            'false': False,
        }.get(args.verify.lower(), args.verify),
        'cert': cert,
    }
E   AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/client.py:230: AttributeError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        args = argparse.Namespace(cert=None, cert_key=None, proxy=[], verify=None)
>       kwargs = make_send_kwargs_mergeable_from_env(args)

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_send_kwargs_mergeable_from_env_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = Namespace(cert=None, cert_key=None, proxy=[], verify=None)

    def make_send_kwargs_mergeable_from_env(args: argparse.Namespace) -> dict:
        cert = None
        if args.cert:
            cert = args.cert
            if args.cert_key:
                cert = cert, args.cert_key
        kwargs = {
            'proxies': {p.key: p.value for p in args.proxy},
            'stream': True,
            'verify': {
                'yes': True,
                'true': True,
                'no': False,
                'false': False,
>           }.get(args.verify.lower(), args.verify),
            'cert': cert,
        }
E       AttributeError: 'NoneType' object has no attribute 'lower'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/client.py:237: AttributeError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        args = argparse.Namespace(cert='path/to/cert', cert_key=123, proxy=[{'key': 'http', 'value': 'invalidurl'}], verify='invalid')
        with pytest.raises(TypeError):
>           make_send_kwargs_mergeable_from_env(args)

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_send_kwargs_mergeable_from_env_0.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/client.py:230: in make_send_kwargs_mergeable_from_env
    'proxies': {p.key: p.value for p in args.proxy},
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f3b62a86950>

>       'proxies': {p.key: p.value for p in args.proxy},
        'stream': True,
        'verify': {
            'yes': True,
            'true': True,
            'no': False,
            'false': False,
        }.get(args.verify.lower(), args.verify),
        'cert': cert,
    }
E   AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/client.py:230: AttributeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_send_kwargs_mergeable_from_env_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_send_kwargs_mergeable_from_env_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_send_kwargs_mergeable_from_env_0.py::test_invalid_inputs
========================= 3 failed, 1 warning in 0.43s =========================
"""