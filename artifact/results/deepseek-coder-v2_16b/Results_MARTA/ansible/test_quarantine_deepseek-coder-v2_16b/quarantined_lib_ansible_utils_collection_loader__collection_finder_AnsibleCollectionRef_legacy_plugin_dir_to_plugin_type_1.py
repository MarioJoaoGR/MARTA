
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

class TestAnsibleCollectionRef:
    
    @pytest.fixture
    def valid_case(self):
        return AnsibleCollectionRef('my_namespace.my_collection', 'subdir1.subdir2', 'mymodule', 'module')
    
    def test_valid_case(self, valid_case):
        assert valid_case.collection == 'my_namespace.my_collection'
        assert valid_case.subdirs == 'subdir1.subdir2'
        assert valid_case.resource == 'mymodule'
        assert valid_case.ref_type == 'module'
    
    @pytest.fixture
    def edge_case(self):
        return AnsibleCollectionRef('my_namespace.my_collection', None, '', '')
    
    def test_edge_case(self, edge_case):
        assert edge_case.collection == 'my_namespace.my_collection'
        assert edge_case.subdirs == ''
        assert edge_case.resource == ''
        assert edge_case.ref_type == ''
    
    @pytest.fixture
    def invalid_collection_name(self):
        with pytest.raises(ValueError) as e:
            return AnsibleCollectionRef('invalid_namespace', 'subdir1.subdir2', 'mymodule', 'module')
    
    def test_invalid_collection_name(self, invalid_collection_name):
        assert str(invalid_collection_name.exception) == "invalid collection name (must be of the form namespace.collection): invalid_namespace"
    
    @pytest.fixture
    def invalid_ref_type(self):
        with pytest.raises(ValueError) as e:
            return AnsibleCollectionRef('my_namespace.my_collection', 'subdir1.subdir2', 'mymodule', 'invalid_type')
    
    def test_invalid_ref_type(self, invalid_ref_type):
        assert str(invalid_ref_type.exception) == "invalid collection ref_type: invalid_type"
    
    @pytest.fixture
    def invalid_subdirs(self):
        with pytest.raises(ValueError) as e:
            return AnsibleCollectionRef('my_namespace.my_collection', 'invalid_subdir', 'mymodule', 'module')
    
    def test_invalid_subdirs(self, invalid_subdirs):
        assert str(invalid_subdirs.exception) == "invalid subdirs entry: invalid_subdir (must be empty/None or of the form subdir1.subdir2)"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py E [ 20%]
EFFF                                                                     [100%]

==================================== ERRORS ====================================
__________ ERROR at setup of TestAnsibleCollectionRef.test_valid_case __________

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.TestAnsibleCollectionRef object at 0x7f1eedf97190>

    @pytest.fixture
    def valid_case(self):
>       return AnsibleCollectionRef('my_namespace.my_collection', 'subdir1.subdir2', 'mymodule', 'module')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7f1eedf96ef0>
collection_name = 'my_namespace.my_collection', subdirs = 'subdir1.subdir2'
resource = 'mymodule', ref_type = 'module'

    def __init__(self, collection_name, subdirs, resource, ref_type):
        """
        Create an AnsibleCollectionRef from components
        :param collection_name: a collection name of the form 'namespace.collectionname'
        :param subdirs: optional subdir segments to be appended below the plugin type (eg, 'subdir1.subdir2')
        :param resource: the name of the resource being references (eg, 'mymodule', 'someaction', 'a_role')
        :param ref_type: the type of the reference, eg 'module', 'role', 'doc_fragment'
        """
        collection_name = to_text(collection_name, errors='strict')
        if subdirs is not None:
            subdirs = to_text(subdirs, errors='strict')
        resource = to_text(resource, errors='strict')
        ref_type = to_text(ref_type, errors='strict')
    
        if not self.is_valid_collection_name(collection_name):
            raise ValueError('invalid collection name (must be of the form namespace.collection): {0}'.format(to_native(collection_name)))
    
        if ref_type not in self.VALID_REF_TYPES:
>           raise ValueError('invalid collection ref_type: {0}'.format(ref_type))
E           ValueError: invalid collection ref_type: module

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/collection_loader/_collection_finder.py:723: ValueError
__________ ERROR at setup of TestAnsibleCollectionRef.test_edge_case ___________

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.TestAnsibleCollectionRef object at 0x7f1eedf972b0>

    @pytest.fixture
    def edge_case(self):
>       return AnsibleCollectionRef('my_namespace.my_collection', None, '', '')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7f1eeddffd00>
collection_name = 'my_namespace.my_collection', subdirs = None, resource = ''
ref_type = ''

    def __init__(self, collection_name, subdirs, resource, ref_type):
        """
        Create an AnsibleCollectionRef from components
        :param collection_name: a collection name of the form 'namespace.collectionname'
        :param subdirs: optional subdir segments to be appended below the plugin type (eg, 'subdir1.subdir2')
        :param resource: the name of the resource being references (eg, 'mymodule', 'someaction', 'a_role')
        :param ref_type: the type of the reference, eg 'module', 'role', 'doc_fragment'
        """
        collection_name = to_text(collection_name, errors='strict')
        if subdirs is not None:
            subdirs = to_text(subdirs, errors='strict')
        resource = to_text(resource, errors='strict')
        ref_type = to_text(ref_type, errors='strict')
    
        if not self.is_valid_collection_name(collection_name):
            raise ValueError('invalid collection name (must be of the form namespace.collection): {0}'.format(to_native(collection_name)))
    
        if ref_type not in self.VALID_REF_TYPES:
>           raise ValueError('invalid collection ref_type: {0}'.format(ref_type))
E           ValueError: invalid collection ref_type:

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/collection_loader/_collection_finder.py:723: ValueError
=================================== FAILURES ===================================
____________ TestAnsibleCollectionRef.test_invalid_collection_name _____________

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.TestAnsibleCollectionRef object at 0x7f1eedf97430>
invalid_collection_name = None

    def test_invalid_collection_name(self, invalid_collection_name):
>       assert str(invalid_collection_name.exception) == "invalid collection name (must be of the form namespace.collection): invalid_namespace"
E       AttributeError: 'NoneType' object has no attribute 'exception'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py:33: AttributeError
________________ TestAnsibleCollectionRef.test_invalid_ref_type ________________

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.TestAnsibleCollectionRef object at 0x7f1eedf975b0>
invalid_ref_type = None

    def test_invalid_ref_type(self, invalid_ref_type):
>       assert str(invalid_ref_type.exception) == "invalid collection ref_type: invalid_type"
E       AttributeError: 'NoneType' object has no attribute 'exception'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py:41: AttributeError
________________ TestAnsibleCollectionRef.test_invalid_subdirs _________________

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.TestAnsibleCollectionRef object at 0x7f1eedf97730>
invalid_subdirs = None

    def test_invalid_subdirs(self, invalid_subdirs):
>       assert str(invalid_subdirs.exception) == "invalid subdirs entry: invalid_subdir (must be empty/None or of the form subdir1.subdir2)"
E       AttributeError: 'NoneType' object has no attribute 'exception'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py:49: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py::TestAnsibleCollectionRef::test_invalid_collection_name
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py::TestAnsibleCollectionRef::test_invalid_ref_type
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py::TestAnsibleCollectionRef::test_invalid_subdirs
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py::TestAnsibleCollectionRef::test_valid_case
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type_1.py::TestAnsibleCollectionRef::test_edge_case
========================= 3 failed, 2 errors in 0.43s ==========================
"""