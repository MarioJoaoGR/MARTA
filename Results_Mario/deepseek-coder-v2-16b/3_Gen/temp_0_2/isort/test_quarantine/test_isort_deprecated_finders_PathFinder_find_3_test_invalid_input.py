
import pytest
from isort.deprecated.finders import PathFinder
from unittest.mock import MagicMock

@pytest.mark.parametrize("module_name", ["invalid.module.name", "another.invalid.module"])
def test_invalid_input(mock_config, module_name):
    finder = PathFinder(config=mock_config)
    with pytest.raises(Exception):
        finder.find(module_name)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_3_test_invalid_input.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
__________ ERROR at setup of test_invalid_input[invalid.module.name] ___________
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_3_test_invalid_input.py, line 6
  @pytest.mark.parametrize("module_name", ["invalid.module.name", "another.invalid.module"])
  def test_invalid_input(mock_config, module_name):
E       fixture 'mock_config' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_3_test_invalid_input.py:6
_________ ERROR at setup of test_invalid_input[another.invalid.module] _________
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_3_test_invalid_input.py, line 6
  @pytest.mark.parametrize("module_name", ["invalid.module.name", "another.invalid.module"])
  def test_invalid_input(mock_config, module_name):
E       fixture 'mock_config' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_3_test_invalid_input.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_3_test_invalid_input.py::test_invalid_input[invalid.module.name]
ERROR isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_3_test_invalid_input.py::test_invalid_input[another.invalid.module]
============================== 2 errors in 0.12s ===============================
"""