
import pytest
from youtube_dl.extractor.archiveorg import get_optional

def test_get_optional_basic():
    metadata = {'key': 'value'}
    assert get_optional(metadata, 'key') == 'value'

def test_get_optional_nonexistent_key():
    metadata = {}
    assert get_optional(metadata, 'non_existent_key') is None

def test_get_optional_list_as_default():
    metadata = {'another_key': [1, 2]}
    assert get_optional(metadata, 'another_key') == 1

def test_get_optional_dictionary_with_multiple_keys():
    metadata = {'a': {'b': 'c'}, 'd': {'e': 'f'}}
    assert get_optional(metadata, 'a') == {'b': 'c'}

def test_get_optional_handling_none_type():
    metadata = {'key': None}
    assert get_optional(metadata, 'key') is None

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
___ ERROR collecting test_youtube_dl_extractor_archiveorg_get_optional_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_archiveorg_get_optional_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_archiveorg_get_optional_0.py:3: in <module>
    from youtube_dl.extractor.archiveorg import get_optional
E   ImportError: cannot import name 'get_optional' from 'youtube_dl.extractor.archiveorg' (/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/archiveorg.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_archiveorg_get_optional_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.66s ===============================
"""