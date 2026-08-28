
import pytest
from youtube_dl.extractor.linuxacademy import random_string

def test_random_string():
    # Test that the length of the generated string is 32 characters
    assert len(random_string()) == 32
    
    # Test that the generated string contains only valid characters
    allowed_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz-._~'
    assert all(char in allowed_chars for char in random_string())
    
    # Test that the generated string is unique (this is probabilistic and could fail rarely)
    first_random_string = random_string()
    second_random_string = random_string()
    assert first_random_string != second_random_string

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
__ ERROR collecting test_youtube_dl_extractor_linuxacademy_random_string_0.py __
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_random_string_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_random_string_0.py:3: in <module>
    from youtube_dl.extractor.linuxacademy import random_string
E   ImportError: cannot import name 'random_string' from 'youtube_dl.extractor.linuxacademy' (/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/linuxacademy.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_random_string_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.61s ===============================
"""