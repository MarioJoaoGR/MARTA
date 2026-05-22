
import sys
from collections import OrderedDict
from httpie.utils import JsonDictPreservingDuplicateKeys, Items

class TestJsonDictPreservingDuplicateKeys:
    def test_valid_input(self):
        items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
        jdpdk = JsonDictPreservingDuplicateKeys(items)
        
        with patch('httpie.utils.sys') as mock_sys:
            mock_sys.version_info = (3, 8)
            assert jdpdk.SUPPORTS_SORTING is True
        
        assert jdpdk.items() == OrderedDict([('a', 1), ('b', 2), ('a', 3)])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_JsonDictPreservingDuplicateKeys_items_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_JsonDictPreservingDuplicateKeys_items_0_test_valid_input.py:11:13: E0602: Undefined variable 'patch' (undefined-variable)


"""