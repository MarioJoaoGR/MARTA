
import pytest
from unittest.mock import patch, Mock
from httpie.uploads import ChunkedUploadStream

def test_invalid_inputs():
    stream = 'not iterable'
    callback = Mock()
    
    with pytest.raises(TypeError):
        uploader = ChunkedUploadStream(stream, callback)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_ChunkedUploadStream___iter___0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        stream = 'not iterable'
        callback = Mock()
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_ChunkedUploadStream___iter___0_test_invalid_inputs.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_ChunkedUploadStream___iter___0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.20s ===============================
"""