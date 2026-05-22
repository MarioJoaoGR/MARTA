
import pytest
from httpie.manager.tasks.plugins import PluginInstaller

def test_error_handling(mock_env):
    with pytest.raises(NotImplementedError):
        installer = PluginInstaller(env=mock_env, debug=True)
        installer.list()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_error_handling.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_error_handling _____________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_error_handling.py, line 5
  def test_error_handling(mock_env):
E       fixture 'mock_env' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_error_handling.py:5
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_error_handling.py::test_error_handling
=============================== 1 error in 0.28s ===============================
"""