
import pytest
from pytutils.pythree import ensure_decoded_text
import six

def test_error_handling_invalid_allowed_types():
    with pytest.raises(TypeError):
        ensure_decoded_text("Hello", allowed_types=(int,))  # Invalid type for allowed_types

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

pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_1_test_error_handling_invalid_allowed_types.py F [100%]

=================================== FAILURES ===================================
__________________ test_error_handling_invalid_allowed_types ___________________

    def test_error_handling_invalid_allowed_types():
        with pytest.raises(TypeError):
>           ensure_decoded_text("Hello", allowed_types=(int,))  # Invalid type for allowed_types

pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_1_test_error_handling_invalid_allowed_types.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = 'Hello', encoding = 'utf-8', errors = 'strict'
allowed_types = (<class 'int'>,)

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
E           AttributeError: 'str' object has no attribute 'decode'

pytutils/pytutils/pythree.py:32: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_1_test_error_handling_invalid_allowed_types.py::test_error_handling_invalid_allowed_types
============================== 1 failed in 0.06s ===============================
"""