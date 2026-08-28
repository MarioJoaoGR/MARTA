
import pytest
from ansible.module_utils.urls import _dnsname_match
from ansible.errors import CertificateError

def test__dnsname_match_valid_wildcard():
    assert _dnsname_match('*.example.org', 'subdomain.example.org') is True

def test__dnsname_match_invalid_too_many_wildcards():
    with pytest.raises(CertificateError) as excinfo:
        _dnsname_match('*.example.org', 'www.example.org')
    assert str(excinfo.value) == "too many wildcards in certificate DNS name: '*.example.org'"

def test__dnsname_match_invalid_wildcard_not_leftmost():
    with pytest.raises(CertificateError) as excinfo:
        _dnsname_match('*.example.org', 'a.b.example.org')
    assert str(excinfo.value) == "wildcard can only be present in the leftmost label: '*.example.org'."

def test__dnsname_match_invalid_sole_wildcard():
    with pytest.raises(CertificateError) as excinfo:
        _dnsname_match('*.example.org', 'example.org')
    assert str(excinfo.value) == "sole wildcard without additional labels are not support: '*.example.org'."

def test__dnsname_match_invalid_partial_wildcard():
    with pytest.raises(CertificateError) as excinfo:
        _dnsname_match('subdomain.*.example.org', 'subdomain.example.org')
    assert str(excinfo.value) == "partial wildcards in leftmost label are not supported: 'subdomain.*.example.org'."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___ ERROR collecting test_lib_ansible_module_utils_urls__dnsname_match_1.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls__dnsname_match_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls__dnsname_match_1.py:3: in <module>
    from ansible.module_utils.urls import _dnsname_match
E   ImportError: cannot import name '_dnsname_match' from 'ansible.module_utils.urls' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls__dnsname_match_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.83s ===============================
"""