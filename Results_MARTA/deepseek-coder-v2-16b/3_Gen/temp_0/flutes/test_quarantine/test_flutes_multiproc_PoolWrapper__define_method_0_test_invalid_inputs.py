
import pytest
from flutes.multiproc import PoolWrapper

def test_starmap_invalid_args(pool_wrapper):
    with pytest.raises(TypeError):
        pool_wrapper.starmap(lambda x, y: x + y, [(1,)])  # Invalid because the function expects two arguments but only one is provided

def test_starmap_async_invalid_args(pool_wrapper):
    with pytest.raises(TypeError):
        pool_wrapper.starmap_async(lambda x, y: x + y, [(1,)])  # Invalid because the function expects two arguments but only one is provided

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_invalid_inputs.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_________________ ERROR at setup of test_starmap_invalid_args __________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_invalid_inputs.py, line 5
  def test_starmap_invalid_args(pool_wrapper):
E       fixture 'pool_wrapper' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_invalid_inputs.py:5
______________ ERROR at setup of test_starmap_async_invalid_args _______________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_invalid_inputs.py, line 9
  def test_starmap_async_invalid_args(pool_wrapper):
E       fixture 'pool_wrapper' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_invalid_inputs.py:9
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_invalid_inputs.py::test_starmap_invalid_args
ERROR flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_invalid_inputs.py::test_starmap_async_invalid_args
============================== 2 errors in 0.08s ===============================

"""