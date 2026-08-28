
import pytest
from httpie.output.streams import EncodedStream
from httpie.environment import Environment
from httpie.http_message import HTTPMessage
from unittest.mock import patch, MagicMock

def test_default_initialization():
    env = Environment()
    msg = HTTPMessage()
    encoded_stream = EncodedStream(env=env, msg=msg)
    
    assert hasattr(encoded_stream, 'output_encoding')
    assert encoded_stream.output_encoding == 'utf8' or encoded_stream.output_encoding == msg.encoding

def test_iter_body():
    env = Environment()
    msg = HTTPMessage()
    msg.iter_lines = MagicMock(return_value=[(b"line1", b"\n"), (b"line2", b"\n")])
    encoded_stream = EncodedStream(env=env, msg=msg)
    
    with patch('httpie.output.streams.EncodedStream.CHUNK_SIZE', 1):
        lines = list(encoded_stream.iter_body())
        
    assert len(lines) == 2
    assert lines[0] == b"line1\n"
    assert lines[1] == b"line2\n"

def test_binary_suppressed():
    env = Environment()
    msg = HTTPMessage()
    msg.iter_lines = MagicMock(return_value=[(b"line1", b"\n"), (b"lineline\x00e2", b"\n")])
    encoded_stream = EncodedStream(env=env, msg=msg)
    
    with pytest.raises(BinarySuppressedError):
        list(encoded_stream.iter_body())

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
___ ERROR collecting test_httpie_output_streams_EncodedStream_iter_body_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0.py:4: in <module>
    from httpie.environment import Environment
E   ModuleNotFoundError: No module named 'httpie.environment'
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.65s ==========================
"""