
import pytest
from youtube_dl.options import _comma_separated_values_options_callback

def test_comma_separated_values_options_callback():
    # Create a mock argument parser and namespace object
    class MockParser:
        def __init__(self):
            self.values = MockNamespace()
    
    class MockNamespace:
        pass
    
    # Test with a single option value
    parser = MockParser()
    _comma_separated_values_options_callback(None, '--numbers', '1,2,3', parser)
    assert parser.values.numbers == ['1', '2', '3']
    
    # Test with multiple option values
    parser = MockParser()
    _comma_separated_values_options_callback(None, '--names', 'Alice,Bob', parser)
    assert parser.values.names == ['Alice', 'Bob']
    
    parser = MockParser()
    _comma_separated_values_options_callback(None, '--ids', '1,2', parser)
    assert parser.values.ids == ['1', '2']


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_youtube_dl_options__comma_separated_values_options_callback_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options__comma_separated_values_options_callback_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options__comma_separated_values_options_callback_0.py:3: in <module>
    from youtube_dl.options import _comma_separated_values_options_callback
E   ImportError: cannot import name '_comma_separated_values_options_callback' from 'youtube_dl.options' (/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/options.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options__comma_separated_values_options_callback_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.62s ===============================
"""