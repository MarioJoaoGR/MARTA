
import pytest
from pytutils.mappings import format_dict_recursively

def test_edge_case_none():
    c = dict(wat='wat{omg}', omg=True)
    formatted_dict = format_dict_recursively(c)
    assert formatted_dict == {'omg': True, 'wat': 'watTrue'}

    # Test handling missing keys in format strings
    c = dict(wat='wat{omg}', omg=True, fail='no{whale}')
    with pytest.raises(ValueError):
        format_dict_recursively(c)
    
    formatted_dict = format_dict_recursively(c, raise_unresolvable=False)
    assert formatted_dict == {'fail': 'no{whale}', 'omg': True, 'wat': 'watTrue'}

    formatted_dict = format_dict_recursively(c, raise_unresolvable=False, strip_unresolvable=True)
    assert formatted_dict == {'omg': True, 'wat': 'watTrue'}

    # Test conversion example
    c = dict(num='{num} is {val}', num=10, val='a number')
    formatted_dict = format_dict_recursively(c)
    assert formatted_dict == {'num': '10 is a number', 'val': 'a number'}
    
    conversions = {'a number': True}
    formatted_dict = format_dict_recursively(c, conversions=conversions)
    assert formatted_dict == {'num': '10 is True', 'val': 'True'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/usr/local/lib/python3.11/site-packages/_pytest/python.py:493: in importtestmodule
    mod = import_path(
/usr/local/lib/python3.11/site-packages/_pytest/pathlib.py:582: in import_path
    importlib.import_module(module_name)
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1204: in _gcd_import
    ???
<frozen importlib._bootstrap>:1176: in _find_and_load
    ???
<frozen importlib._bootstrap>:1147: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:690: in _load_unlocked
    ???
/usr/local/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:165: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
/usr/local/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:347: in _rewrite_test
    co = compile(tree, strfn, "exec", dont_inherit=True)
E     File "/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_edge_case_none.py", line 22
E       c = dict(num='{num} is {val}', num=10, val='a number')
E                                      ^^^^^^
E   SyntaxError: keyword argument repeated: num
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-czfcki1f'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-blor62mn'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-jlef3xu1'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.18s =========================
"""