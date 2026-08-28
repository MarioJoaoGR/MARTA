
import pytest
from blib2to3.pgen2.tokenize import get_normal_name as _get_normal_name

def test__get_normal_name_standard():
    assert _get_normal_name("UTF-8") == "utf-8"
    assert _get_normal_name("latin-1") == "iso-8859-1"
    assert _get_normal_name("ISO-Latin-1") == "iso-8859-1"

def test__get_normal_name_nonstandard():
    assert _get_normal_name("utf-8-variant") == "utf-8-variant"
    assert _get_normal_name("something-else") == "something-else"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___ ERROR collecting test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py:3: in <module>
    from blib2to3.pgen2.tokenize import get_normal_name as _get_normal_name
E   ImportError: cannot import name 'get_normal_name' from 'blib2to3.pgen2.tokenize' (/opt/marta/baselines/codamosa/replication/test-apps/black/src/blib2to3/pgen2/tokenize.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""