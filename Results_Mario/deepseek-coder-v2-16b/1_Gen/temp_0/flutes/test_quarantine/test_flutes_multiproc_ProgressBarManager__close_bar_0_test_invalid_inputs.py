
import pytest
from flutes.multiproc import ProgressBarManager

def test_close_bar_with_valid_worker_id(progress_bar_manager):
    # Arrange
    worker_id = 1
    bar = progress_bar_manager._proxy
    bar.new(total=100, desc="Test Bar")
    
    # Act
    progress_bar_manager._close_bar(worker_id)
    
    # Assert
    assert worker_id in progress_bar_manager.progress_bars

def test_close_bar_with_invalid_worker_id(progress_bar_manager):
    # Arrange
    worker_id = 999
    
    # Act & Assert
    with pytest.raises(KeyError):
        progress_bar_manager._close_bar(worker_id)

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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_invalid_inputs.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
____________ ERROR at setup of test_close_bar_with_valid_worker_id _____________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_invalid_inputs.py, line 5
  def test_close_bar_with_valid_worker_id(progress_bar_manager):
E       fixture 'progress_bar_manager' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_invalid_inputs.py:5
___________ ERROR at setup of test_close_bar_with_invalid_worker_id ____________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_invalid_inputs.py, line 17
  def test_close_bar_with_invalid_worker_id(progress_bar_manager):
E       fixture 'progress_bar_manager' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_invalid_inputs.py:17
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_invalid_inputs.py::test_close_bar_with_valid_worker_id
ERROR flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_invalid_inputs.py::test_close_bar_with_invalid_worker_id
============================== 2 errors in 0.09s ===============================
"""