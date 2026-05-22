
import pytest
from httpie.utils import JsonDictPreservingDuplicateKeys
from collections import OrderedDict

def test_invalid_input():
    with pytest.raises(TypeError):
        items = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
        jdpdk = JsonDictPreservingDuplicateKeys(items)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys_items_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys_items_2_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys_items_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""