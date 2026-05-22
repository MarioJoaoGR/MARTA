
import pytest
from httpie.uploads import ChunkedUploadStream
from threading import Event
from unittest.mock import patch, MagicMock

def my_callback(chunk):
    pass

data_stream = 'not iterable'
with pytest.raises(ValueError) as e:
    uploader = ChunkedUploadStream(data_stream, my_callback)
assert str(e.value) == "The provided stream is not iterable."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests_codestral/test_httpie_uploads_ChunkedUploadStream___init___1_test_invalid_inputs.py _
httpie/Test4DT_tests_codestral/test_httpie_uploads_ChunkedUploadStream___init___1_test_invalid_inputs.py:11: in <module>
    with pytest.raises(ValueError) as e:
E   Failed: DID NOT RAISE <class 'ValueError'>
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_codestral/test_httpie_uploads_ChunkedUploadStream___init___1_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""