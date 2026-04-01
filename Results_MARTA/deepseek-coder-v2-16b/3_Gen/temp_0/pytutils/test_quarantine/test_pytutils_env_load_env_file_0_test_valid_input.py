
import pytest
from pytutils.env import load_env_file
import os
import collections
import typing

@pytest.mark.parametrize("lines", [['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']])
def test_valid_input(lines, mocker):
    # Mock os.environ to return predefined values for HOME and PATH
    mocker.patch('os.environ', {
        'HOME': '/home/user',
        'PATH': '/usr/local/bin:/usr/bin'
    })

    result = load_env_file(lines)

    # Expected expanded values
    expected = collections.OrderedDict([
        ('TEST', '/home/user/yeee-/usr/local/bin:/usr/bin'),
        ('THISIS', '/a/test'),
        ('YOLO', '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ])

    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

../../../dev E                                                           [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_valid_input[lines0] __________________
file /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0_test_valid_input.py, line 8
  @pytest.mark.parametrize("lines", [['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']])
  def test_valid_input(lines, mocker):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0_test_valid_input.py:8
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-yc_jxheg'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-hiquwjnj'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-jobit6vn'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev/::test_valid_input[lines0]
========================= 3 warnings, 1 error in 0.04s =========================
"""