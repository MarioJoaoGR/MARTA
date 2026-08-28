
import pytest
from httpie.output.streams import BaseStream
from models import HTTPMessage

# Test initialization with default settings
def test_base_stream_default_init():
    msg = HTTPMessage()
    base_stream = BaseStream(msg=msg)
    assert hasattr(base_stream, 'with_headers')
    assert hasattr(base_stream, 'with_body')
    assert base_stream.with_headers is True
    assert base_stream.with_body is True
    assert base_stream.on_body_chunk_downloaded is None

# Test initialization with only headers included
def test_base_stream_init_with_headers():
    msg = HTTPMessage()
    base_stream = BaseStream(msg=msg, with_headers=True, with_body=False)
    assert hasattr(base_stream, 'with_headers')
    assert hasattr(base_stream, 'with_body')
    assert base_stream.with_headers is True
    assert base_stream.with_body is False
    assert base_stream.on_body_chunk_downloaded is None

# Test initialization with a custom callback for body chunks
def test_base_stream_init_with_callback():
    msg = HTTPMessage()
    def log_chunk(chunk: bytes):
        print(f"Chunk downloaded: {len(chunk)} bytes")
    
    base_stream = BaseStream(msg=msg, on_body_chunk_downloaded=log_chunk)
    assert hasattr(base_stream, 'on_body_chunk_downloaded')
    assert callable(base_stream.on_body_chunk_downloaded)

# Test initialization with both headers and body included
def test_base_stream_init_with_headers_and_body():
    msg = HTTPMessage()
    base_stream = BaseStream(msg=msg, with_headers=True, with_body=True)
    assert hasattr(base_stream, 'with_headers')
    assert hasattr(base_stream, 'with_body')
    assert base_stream.with_headers is True
    assert base_stream.with_body is True
    assert base_stream.on_body_chunk_downloaded is None

# Test initialization with both headers and body excluded (should raise AssertionError)
def test_base_stream_init_without_headers_and_body():
    msg = HTTPMessage()
    with pytest.raises(AssertionError):
        BaseStream(msg=msg, with_headers=False, with_body=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____ ERROR collecting test_httpie_output_streams_BaseStream_iter_body_0.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_BaseStream_iter_body_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_BaseStream_iter_body_0.py:4: in <module>
    from models import HTTPMessage
E   ModuleNotFoundError: No module named 'models'
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_BaseStream_iter_body_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.49s ==========================
"""