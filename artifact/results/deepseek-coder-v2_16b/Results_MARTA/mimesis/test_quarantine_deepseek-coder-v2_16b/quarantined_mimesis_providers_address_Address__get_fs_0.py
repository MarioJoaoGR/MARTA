
import pytest
from mimesis.providers.address import Address

@pytest.fixture(scope="module")
def address():
    return Address()





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
___________________________ test_dms_format_latitude ___________________________

address = <mimesis.providers.address.Address object at 0x7f3a3e5ad1e0>

    def test_dms_format_latitude(address):
        key = 'lt'
        dms = True
        result = address._get_fs(key, dms)
        parts = result.split()
>       assert len(parts) == 3, "Expected three parts in DMS format"
E       AssertionError: Expected three parts in DMS format
E       assert 1 == 3
E        +  where 1 = len(['86º34\'7.867"N'])

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py:14: AssertionError
__________________________ test_dms_format_longitude ___________________________

address = <mimesis.providers.address.Address object at 0x7f3a3e5ad1e0>

    def test_dms_format_longitude(address):
        key = 'lg'
        dms = True
        result = address._get_fs(key, dms)
        parts = result.split()
>       assert len(parts) == 3, "Expected three parts in DMS format"
E       AssertionError: Expected three parts in DMS format
E       assert 1 == 3
E        +  where 1 = len(['110º46\'4.685"W'])

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py:21: AssertionError
____________________________ test_invalid_key_input ____________________________

address = <mimesis.providers.address.Address object at 0x7f3a3e5ad1e0>

    def test_invalid_key_input(address):
        key = 'unknown'
        dms = False
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py:26: Failed
___________________________ test_none_latitude_input ___________________________

address = <mimesis.providers.address.Address object at 0x7f3a3e5ad1e0>

    def test_none_latitude_input(address):
        key = None
        dms = False
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py:32: Failed
__________________________ test_none_longitude_input ___________________________

address = <mimesis.providers.address.Address object at 0x7f3a3e5ad1e0>

    def test_none_longitude_input(address):
        key = 'lg'
        dms = None
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py:38: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py::test_dms_format_latitude
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py::test_dms_format_longitude
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py::test_invalid_key_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py::test_none_latitude_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_address_Address__get_fs_0.py::test_none_longitude_input
============================== 5 failed in 0.12s ===============================
"""