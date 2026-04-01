
import pytest
from pytutils.tlds import split_domain_into_subdomains, ensure_decoded_text

def test_edge_case_none():
    # Test when domain is None
    with pytest.raises(TypeError):  # Expecting a TypeError since the function expects a string and not None
        assert split_domain_into_subdomains(None) == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        # Test when domain is None
        with pytest.raises(TypeError):  # Expecting a TypeError since the function expects a string and not None
>           assert split_domain_into_subdomains(None) == []

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_edge_case_none.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/site-packages/cachetools/_cachedmethod.py:125: in __call__
    return self.__wrapper(*args, **kwargs)
/usr/local/lib/python3.11/site-packages/cachetools/_cachedmethod.py:358: in wrapper
    v = method(self, *args, **kwargs)
pytutils/pytutils/tlds.py:22: in split_domain_into_subdomains
    domain = ensure_decoded_text(domain)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = None, encoding = 'utf-8', errors = 'strict'
allowed_types = (<class 'str'>,)

    def ensure_decoded_text(s, encoding='utf-8', errors='strict', allowed_types=(six.text_type,)):
        """
        Ensure string is decoded (eg unicode); convert using specified parameters if we have to.
    
        :param str|bytes|bytesarray|memoryview s: string/bytes
        :param str encoding: Decode using this encoding
        :param str errors: How to handle errors
        :return bytes|bytesarray|memoryview: Decoded string as bytes
    
        :return: Encoded string
        :rtype: bytes
        """
        if not isinstance(s, allowed_types):
>           return s.decode(encoding=encoding, errors=errors)
E           AttributeError: 'NoneType' object has no attribute 'decode'

pytutils/pytutils/pythree.py:32: AttributeError
=============================== warnings summary ===============================
Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_edge_case_none.py::test_edge_case_none
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_edge_case_none.py:8: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    assert split_domain_into_subdomains(None) == []

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_edge_case_none.py::test_edge_case_none
========================= 1 failed, 1 warning in 0.13s =========================
"""