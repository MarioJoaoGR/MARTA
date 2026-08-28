
import pytest
from flutils.codecs.raw_utf8_escape import encode


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_codecs_raw_utf8_escape_encode_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_encode_with_errors ____________________________

    def test_encode_with_errors():
        text = "中文文本"
        errors = 'ignore'
        expected_output = b'\xe4\xb8\xad\xe6\x96\x87\xe6\x9c\xac\xe6\x96\x87'
        result = encode(text, errors)
        assert isinstance(result[0], bytes), f"Expected bytes output but got {type(result[0])}"
>       assert result[0] == expected_output, f"Expected {expected_output}, but got {result[0]}"
E       AssertionError: Expected b'\xe4\xb8\xad\xe6\x96\x87\xe6\x9c\xac\xe6\x96\x87', but got b'\\xe4\\xb8\\xad\\xe6\\x96\\x87\\xe6\\x96\\x87\\xe6\\x9c\\xac'
E       assert b'\\xe4\\xb8\...xe6\\x9c\\xac' == b'\xe4\xb8\xa...c\xe6\x96\x87'
E         
E         At index 0 diff: b'\\' != b'\xe4'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_codecs_raw_utf8_escape_encode_0.py:11: AssertionError
___________________________ test_encode_invalid_text ___________________________

    def test_encode_invalid_text():
        text = "Hello, World!"
        errors = 'strict'
>       with pytest.raises(UnicodeEncodeError):
E       Failed: DID NOT RAISE <class 'UnicodeEncodeError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_codecs_raw_utf8_escape_encode_0.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_codecs_raw_utf8_escape_encode_0.py::test_encode_with_errors
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_codecs_raw_utf8_escape_encode_0.py::test_encode_invalid_text
============================== 2 failed in 0.06s ===============================
"""