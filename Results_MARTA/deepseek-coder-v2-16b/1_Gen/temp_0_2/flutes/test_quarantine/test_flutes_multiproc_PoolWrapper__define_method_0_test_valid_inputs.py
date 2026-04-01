
import pytest
from flutes.multiproc import PoolWrapper
from multiprocessing import Pool, TimeoutError

def test_imap(pool):
    with pytest.raises(AttributeError):
        pool.imap(lambda x: x * x, [1, 2, 3])

def test_imap_unordered(pool):
    with pytest.raises(AttributeError):
        pool.imap_unordered(lambda x: x * x, [1, 2, 3])

def test_map(pool):
    results = list(pool.map(lambda x: x * x, [1, 2, 3]))
    assert results == [1, 4, 9]

def test_map_async(pool):
    pool.map_async(lambda x: x * x, [1, 2, 3], callback=lambda r: None)
    # No assertion needed as the async call should not raise an error

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py E [ 25%]
EEE                                                                      [100%]

==================================== ERRORS ====================================
_________________________ ERROR at setup of test_imap __________________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py, line 6
  def test_imap(pool):
E       fixture 'pool' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py:6
____________________ ERROR at setup of test_imap_unordered _____________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py, line 10
  def test_imap_unordered(pool):
E       fixture 'pool' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py:10
__________________________ ERROR at setup of test_map __________________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py, line 14
  def test_map(pool):
E       fixture 'pool' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py:14
_______________________ ERROR at setup of test_map_async _______________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py, line 18
  def test_map_async(pool):
E       fixture 'pool' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py:18
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py::test_imap
ERROR flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py::test_imap_unordered
ERROR flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py::test_map
ERROR flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py::test_map_async
============================== 4 errors in 0.11s ===============================
"""