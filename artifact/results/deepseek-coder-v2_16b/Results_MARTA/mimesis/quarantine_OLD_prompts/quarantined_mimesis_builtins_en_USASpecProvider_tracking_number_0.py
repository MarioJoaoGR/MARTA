
import pytest
from unittest.mock import patch
from mimesis.builtins.en import USASpecProvider

@pytest.mark.parametrize("service, expected", [
    ('usps', '#### #### #### #### ####'),
    ('fedex', '#### #### ####'),
    ('ups', '1Z@####@##########')
])
def test_valid_input(provider, service, expected):
    with patch('mimesis.providers.BaseProvider.random', return_value=expected):
        assert provider.tracking_number(service) == expected

def test_invalid_input():
    provider = USASpecProvider()
    with pytest.raises(ValueError):
        provider.tracking_number('dhl')
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py E [ 25%]
EE.                                                                      [100%]

==================================== ERRORS ====================================
______ ERROR at setup of test_valid_input[usps-#### #### #### #### ####] _______
file /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py, line 6
  @pytest.mark.parametrize("service, expected", [
      ('usps', '#### #### #### #### ####'),
      ('fedex', '#### #### ####'),
      ('ups', '1Z@####@##########')
  ])
  def test_valid_input(provider, service, expected):
E       fixture 'provider' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py:6
___________ ERROR at setup of test_valid_input[fedex-#### #### ####] ___________
file /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py, line 6
  @pytest.mark.parametrize("service, expected", [
      ('usps', '#### #### #### #### ####'),
      ('fedex', '#### #### ####'),
      ('ups', '1Z@####@##########')
  ])
  def test_valid_input(provider, service, expected):
E       fixture 'provider' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py:6
__________ ERROR at setup of test_valid_input[ups-1Z@####@##########] __________
file /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py, line 6
  @pytest.mark.parametrize("service, expected", [
      ('usps', '#### #### #### #### ####'),
      ('fedex', '#### #### ####'),
      ('ups', '1Z@####@##########')
  ])
  def test_valid_input(provider, service, expected):
E       fixture 'provider' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py::test_valid_input[usps-#### #### #### #### ####]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py::test_valid_input[fedex-#### #### ####]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider_tracking_number_0.py::test_valid_input[ups-1Z@####@##########]
========================= 1 passed, 3 errors in 0.10s ==========================
"""