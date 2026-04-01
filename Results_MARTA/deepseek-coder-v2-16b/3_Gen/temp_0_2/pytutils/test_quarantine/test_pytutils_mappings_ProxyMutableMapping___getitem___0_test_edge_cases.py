
from pytutils.mappings import ProxyMutableMapping

class TestProxyMutableMappingGetitem:
    def setup_method(self):
        self.mapping = {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}
        self.proxy = ProxyMutableMapping(self.mapping)

    def test_getitem_existing_key(self):
        assert self.proxy['whoa'] == True

    def test_getitem_nonexistent_key(self):
        with pytest.raises(KeyError):
            self.proxy['non_existent_key']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableMapping___getitem___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___getitem___0_test_edge_cases.py:13:13: E0602: Undefined variable 'pytest' (undefined-variable)


"""