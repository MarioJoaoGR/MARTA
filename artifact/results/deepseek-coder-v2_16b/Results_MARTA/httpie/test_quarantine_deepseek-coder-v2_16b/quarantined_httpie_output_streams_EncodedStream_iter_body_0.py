
import pytest
from httpie.output.streams import EncodedStream
from httpie.environment import Environment
from httpie.http_message import HTTPMessage
from io import BytesIO

# Test initialization with default environment settings
def test_default_initialization():
    env = Environment()
    msg = HTTPMessage()
    stream = EncodedStream(env=env, msg=msg)
    
    assert hasattr(stream, 'output_encoding'), "EncodedStream should have an attribute output_encoding"
    assert isinstance(stream.output_encoding, str), "Attribute output_encoding should be a string"
    assert stream.output_encoding == 'utf8', "Default output encoding should be utf8"

# Test initialization with custom environment settings for tty stdout
def test_custom_configuration_with_tty_stdout():
    env = Environment()
    env.stdout_isatty = True
    env.stdout_encoding = 'utf-8'
    msg = HTTPMessage()
    stream = EncodedStream(env=env, msg=msg)
    
    assert stream.output_encoding == 'utf-8', "Output encoding should match the terminal's supported encoding"

# Test initialization with custom environment settings for non-tty stdout
def test_custom_configuration_with_non_tty_stdout():
    env = Environment()
    env.stdout_isatty = False
    msg = HTTPMessage(encoding='ascii')
    stream = EncodedStream(env=env, msg=msg)
    
    assert stream.output_encoding == 'ascii', "Output encoding should match the message's original encoding"

# Test iter_body method with binary data in the message
def test_iter_body_with_binary_data():
    env = Environment()
    msg = HTTPMessage()
    msg._lines = [b'\x00line1', b'line2']  # Mocking lines with a null byte for testing
    stream = EncodedStream(env=env, msg=msg)
    
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())

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
========================= 1 warning, 1 error in 0.46s ==========================
"""