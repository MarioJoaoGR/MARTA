
import pytest
from httpie.encoding import smart_encode

@pytest.mark.parametrize("content, encoding", [
    ("Héllö, wørld!", "ascii")
])
def test_invalid_encoding(content, encoding):
    with pytest.raises(ValueError):
        smart_encode(content, encoding)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_invalid_encoding.py F [100%]

=================================== FAILURES ===================================
_____________ test_invalid_encoding[H\xe9ll\xf6, w\xf8rld!-ascii] ______________

content = 'Héllö, wørld!', encoding = 'ascii'

    @pytest.mark.parametrize("content, encoding", [
        ("Héllö, wørld!", "ascii")
    ])
    def test_invalid_encoding(content, encoding):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_invalid_encoding.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_invalid_encoding.py::test_invalid_encoding[H\xe9ll\xf6, w\xf8rld!-ascii]
============================== 1 failed in 0.14s ===============================
"""