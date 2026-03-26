
import pytest
from flutes.multiproc import PoolType

def test_valid_inputs(pool):
    def square(x: int) -> int:
        return x ** 2
    
    iterable = [1, 2, 3, 4]
    result_iter = pool.imap_unordered(square, iterable)
    results = list(result_iter)  # Convert the iterator to a list
    
    assert len(results) == len(iterable), "The length of the results does not match the length of the input iterable."
    for i in range(len(iterable)):
        assert results[i] == square(iterable[i]), f"Result {results[i]} does not match expected result {square(iterable[i])}."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_valid_inputs.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_inputs ______________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_valid_inputs.py, line 5
  def test_valid_inputs(pool):
E       fixture 'pool' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_valid_inputs.py:5
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_valid_inputs.py::test_valid_inputs
=============================== 1 error in 0.07s ===============================
"""