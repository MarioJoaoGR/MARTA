
import pytest
from flutes.multiproc import PoolType

def square(x):
    return x ** 2

@pytest.fixture(autouse=True)
def pool():
    return PoolType()

@pytest.mark.parametrize("pool", [PoolType()], indirect=True)
def test_valid_inputs(pool, mocker):
    mock = mocker.MagicMock()
    result_iterator = pool.imap_unordered(square, range(5), chunksize=1, args=(), kwds={})
    results = list(result_iterator)
    assert results == [0, 1, 4, 9, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_valid_inputs.py E [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_valid_inputs[pool0] __________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_valid_inputs.py, line 12
  @pytest.mark.parametrize("pool", [PoolType()], indirect=True)
  def test_valid_inputs(pool, mocker):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pool, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_valid_inputs.py:12
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_valid_inputs.py::test_valid_inputs[pool0]
=============================== 1 error in 0.46s ===============================
"""