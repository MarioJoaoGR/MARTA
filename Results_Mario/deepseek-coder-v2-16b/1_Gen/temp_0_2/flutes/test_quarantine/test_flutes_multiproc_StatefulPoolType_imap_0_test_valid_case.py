
import pytest
from flutes.multiproc import StatefulPoolType

def test_valid_case(pool):
    def process_element(state, elem):
        state.append(elem)  # Example function that processes an element
        return elem * 2
    
    iterable = [1, 2, 3, 4]
    results = pool.imap(process_element, iterable, chunksize=2, args=(0,), kwds={})
    
    expected_results = list(map(lambda x: process_element([], x)[1], iterable))
    
    assert list(results) == expected_results

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

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_valid_case.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_case _______________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_valid_case.py, line 5
  def test_valid_case(pool):
E       fixture 'pool' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_valid_case.py:5
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_valid_case.py::test_valid_case
=============================== 1 error in 0.08s ===============================
"""