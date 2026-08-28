
import pytest
from httpie.output.streams import RawStream




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
____________________ test_raw_stream_default_initialization ____________________

    def test_raw_stream_default_initialization():
>       raw_stream = RawStream()

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.streams.RawStream object at 0x7f17d3a7b460>
chunk_size = 102400, kwargs = {}

    def __init__(self, chunk_size=CHUNK_SIZE, **kwargs):
>       super().__init__(**kwargs)
E       TypeError: BaseStream.__init__() missing 1 required positional argument: 'msg'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/streams.py:82: TypeError
_____________________ test_raw_stream_specified_chunk_size _____________________

    def test_raw_stream_specified_chunk_size():
>       raw_stream = RawStream(chunk_size=512)

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.streams.RawStream object at 0x7f17d315bd30>
chunk_size = 512, kwargs = {}

    def __init__(self, chunk_size=CHUNK_SIZE, **kwargs):
>       super().__init__(**kwargs)
E       TypeError: BaseStream.__init__() missing 1 required positional argument: 'msg'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/streams.py:82: TypeError
_________________________ test_raw_stream_read_default _________________________

    def test_raw_stream_read_default():
>       raw_stream = RawStream()

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.streams.RawStream object at 0x7f17d315e350>
chunk_size = 102400, kwargs = {}

    def __init__(self, chunk_size=CHUNK_SIZE, **kwargs):
>       super().__init__(**kwargs)
E       TypeError: BaseStream.__init__() missing 1 required positional argument: 'msg'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/streams.py:82: TypeError
_____________________ test_raw_stream_read_specified_lines _____________________

    def test_raw_stream_read_specified_lines():
>       raw_stream = RawStream()

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.streams.RawStream object at 0x7f17d315c250>
chunk_size = 102400, kwargs = {}

    def __init__(self, chunk_size=CHUNK_SIZE, **kwargs):
>       super().__init__(**kwargs)
E       TypeError: BaseStream.__init__() missing 1 required positional argument: 'msg'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/streams.py:82: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py::test_raw_stream_default_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py::test_raw_stream_specified_chunk_size
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py::test_raw_stream_read_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream___init___0.py::test_raw_stream_read_specified_lines
========================= 4 failed, 1 warning in 0.63s =========================
"""