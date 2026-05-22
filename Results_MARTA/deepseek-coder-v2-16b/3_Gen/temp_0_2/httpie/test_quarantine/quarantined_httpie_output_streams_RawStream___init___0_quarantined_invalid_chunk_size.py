
import pytest
from httpie.output.streams import RawStream

def test_invalid_chunk_size():
    with pytest.raises(ValueError):
        RawStream(chunk_size=-1)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0_test_invalid_chunk_size.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_chunk_size ____________________________

    def test_invalid_chunk_size():
        with pytest.raises(ValueError):
>           RawStream(chunk_size=-1)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0_test_invalid_chunk_size.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.streams.RawStream object at 0x7f4a92ffce50>
chunk_size = -1, kwargs = {}

    def __init__(self, chunk_size=CHUNK_SIZE, **kwargs):
>       super().__init__(**kwargs)
E       TypeError: BaseStream.__init__() missing 2 required positional arguments: 'msg' and 'output_options'

httpie/httpie/output/streams.py:95: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0_test_invalid_chunk_size.py::test_invalid_chunk_size
============================== 1 failed in 0.25s ===============================
"""