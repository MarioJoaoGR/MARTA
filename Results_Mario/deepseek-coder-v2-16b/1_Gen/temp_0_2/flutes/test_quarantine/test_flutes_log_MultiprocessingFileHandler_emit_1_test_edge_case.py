
import pytest
from flutes.log import MultiprocessingFileHandler
import logging
import multiprocessing as mp
import threading
from pathlib import Path

@pytest.mark.parametrize("path, expected_error", [
    (None, TypeError),
    ("", ValueError),
])
def test_invalid_paths(logger, path, expected_error):
    with pytest.raises(expected_error):
        MultiprocessingFileHandler(path)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_edge_case.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_____________ ERROR at setup of test_invalid_paths[None-TypeError] _____________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_edge_case.py, line 9
  @pytest.mark.parametrize("path, expected_error", [
      (None, TypeError),
      ("", ValueError),
  ])
  def test_invalid_paths(logger, path, expected_error):
E       fixture 'logger' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_edge_case.py:9
______________ ERROR at setup of test_invalid_paths[-ValueError] _______________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_edge_case.py, line 9
  @pytest.mark.parametrize("path, expected_error", [
      (None, TypeError),
      ("", ValueError),
  ])
  def test_invalid_paths(logger, path, expected_error):
E       fixture 'logger' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_edge_case.py:9
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_edge_case.py::test_invalid_paths[None-TypeError]
ERROR flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_edge_case.py::test_invalid_paths[-ValueError]
============================== 2 errors in 0.08s ===============================
"""