
import os
import json
import pytest
from pytutils.log import get_config

@pytest.mark.parametrize("given, env_var, default, expected", [
    ('{"key": "value"}', None, None, {"key": "value"}),
    (None, 'LOG_CONFIG', {'default': 'config'}, {'default': 'config'}),
    (None, 'LOG_CONFIG', None, ValueError),
    ({'key': 'value'}, None, None, {'key': 'value'}),
])
def test_valid_inputs(mocker, given, env_var, default, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            get_config(given=given, env_var=env_var, default=default)
    else:
        result = get_config(given=given, env_var=env_var, default=default)
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
collected 4 items

../../../dev EEEE                                                        [100%]

==================================== ERRORS ====================================
__ ERROR at setup of test_valid_inputs[{"key": "value"}-None-None-expected0] ___
file /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_valid_inputs.py, line 7
  @pytest.mark.parametrize("given, env_var, default, expected", [
      ('{"key": "value"}', None, None, {"key": "value"}),
      (None, 'LOG_CONFIG', {'default': 'config'}, {'default': 'config'}),
      (None, 'LOG_CONFIG', None, ValueError),
      ({'key': 'value'}, None, None, {'key': 'value'}),
  ])
  def test_valid_inputs(mocker, given, env_var, default, expected):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_valid_inputs.py:7
___ ERROR at setup of test_valid_inputs[None-LOG_CONFIG-default1-expected1] ____
file /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_valid_inputs.py, line 7
  @pytest.mark.parametrize("given, env_var, default, expected", [
      ('{"key": "value"}', None, None, {"key": "value"}),
      (None, 'LOG_CONFIG', {'default': 'config'}, {'default': 'config'}),
      (None, 'LOG_CONFIG', None, ValueError),
      ({'key': 'value'}, None, None, {'key': 'value'}),
  ])
  def test_valid_inputs(mocker, given, env_var, default, expected):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_valid_inputs.py:7
_____ ERROR at setup of test_valid_inputs[None-LOG_CONFIG-None-ValueError] _____
file /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_valid_inputs.py, line 7
  @pytest.mark.parametrize("given, env_var, default, expected", [
      ('{"key": "value"}', None, None, {"key": "value"}),
      (None, 'LOG_CONFIG', {'default': 'config'}, {'default': 'config'}),
      (None, 'LOG_CONFIG', None, ValueError),
      ({'key': 'value'}, None, None, {'key': 'value'}),
  ])
  def test_valid_inputs(mocker, given, env_var, default, expected):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_valid_inputs.py:7
_______ ERROR at setup of test_valid_inputs[given3-None-None-expected3] ________
file /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_valid_inputs.py, line 7
  @pytest.mark.parametrize("given, env_var, default, expected", [
      ('{"key": "value"}', None, None, {"key": "value"}),
      (None, 'LOG_CONFIG', {'default': 'config'}, {'default': 'config'}),
      (None, 'LOG_CONFIG', None, ValueError),
      ({'key': 'value'}, None, None, {'key': 'value'}),
  ])
  def test_valid_inputs(mocker, given, env_var, default, expected):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_valid_inputs.py:7
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-vwo01v6e'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-d0tun16c'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-s2l5gm78'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev/::test_valid_inputs[{"key": "value"}-None-None-expected0]
ERROR ../../../dev/::test_valid_inputs[None-LOG_CONFIG-default1-expected1]
ERROR ../../../dev/::test_valid_inputs[None-LOG_CONFIG-None-ValueError]
ERROR ../../../dev/::test_valid_inputs[given3-None-None-expected3]
======================== 3 warnings, 4 errors in 0.07s =========================
"""