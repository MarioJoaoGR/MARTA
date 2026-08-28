
import pytest
from mimesis.providers.address import Address
from unittest.mock import patch


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_edge_longitude_input ___________________________

    def test_edge_longitude_input():
        address = Address()
        with patch('mimesis.random.Random.uniform', return_value=180):
            result = address._get_fs(key='lg', dms=True)
            assert isinstance(result, str), "Expected a string in DMS format"
            expected_dms = "180º00'00.000\" E"
>           assert result == expected_dms, f"Unexpected DMS format: {result}"
E           AssertionError: Unexpected DMS format: 180º0'0.000"E
E           assert '180º0\'0.000"E' == '180º00\'00.000" E'
E             
E             - 180º00'00.000" E
E             ?      - -      -
E             + 180º0'0.000"E

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py:12: AssertionError
____________________________ test_invalid_key_input ____________________________

    def test_invalid_key_input():
        address = Address()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py::test_edge_longitude_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py::test_invalid_key_input
============================== 2 failed in 0.10s ===============================
"""