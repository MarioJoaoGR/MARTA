
import pytest
import datetime
from pypara.dcc import _has_leap_day

@pytest.mark.parametrize("start_date, end_date, expected", [
    (datetime.date(2020, 1, 1), datetime.date(2024, 12, 31), True),
    (datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), False),
    (datetime.date(2024, 12, 31), datetime.date(2020, 1, 1), False)
])
def test_has_leap_day(_has_leap_day, start_date, end_date, expected):
    assert _has_leap_day(start_date, end_date) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
_______ ERROR at setup of test_has_leap_day[start_date0-end_date0-True] ________
file /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py, line 6
  @pytest.mark.parametrize("start_date, end_date, expected", [
      (datetime.date(2020, 1, 1), datetime.date(2024, 12, 31), True),
      (datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), False),
      (datetime.date(2024, 12, 31), datetime.date(2020, 1, 1), False)
  ])
  def test_has_leap_day(_has_leap_day, start_date, end_date, expected):
E       fixture '_has_leap_day' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py:6
_______ ERROR at setup of test_has_leap_day[start_date1-end_date1-False] _______
file /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py, line 6
  @pytest.mark.parametrize("start_date, end_date, expected", [
      (datetime.date(2020, 1, 1), datetime.date(2024, 12, 31), True),
      (datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), False),
      (datetime.date(2024, 12, 31), datetime.date(2020, 1, 1), False)
  ])
  def test_has_leap_day(_has_leap_day, start_date, end_date, expected):
E       fixture '_has_leap_day' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py:6
_______ ERROR at setup of test_has_leap_day[start_date2-end_date2-False] _______
file /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py, line 6
  @pytest.mark.parametrize("start_date, end_date, expected", [
      (datetime.date(2020, 1, 1), datetime.date(2024, 12, 31), True),
      (datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), False),
      (datetime.date(2024, 12, 31), datetime.date(2020, 1, 1), False)
  ])
  def test_has_leap_day(_has_leap_day, start_date, end_date, expected):
E       fixture '_has_leap_day' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py::test_has_leap_day[start_date0-end_date0-True]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py::test_has_leap_day[start_date1-end_date1-False]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__has_leap_day_0.py::test_has_leap_day[start_date2-end_date2-False]
============================== 3 errors in 0.05s ===============================
"""