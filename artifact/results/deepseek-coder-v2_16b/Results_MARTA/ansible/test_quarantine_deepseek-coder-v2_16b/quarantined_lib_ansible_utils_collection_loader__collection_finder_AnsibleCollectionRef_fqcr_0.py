
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_fqcr_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
>       collection_ref = AnsibleCollectionRef('ansible.sample', None, 'mymodule', 'module')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_fqcr_0.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7fd4f50d2500>
collection_name = 'ansible.sample', subdirs = None, resource = 'mymodule'
ref_type = 'module'

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
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
>       collection_ref = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_fqcr_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7fd4f51672b0>
collection_name = 'ansible.sample', subdirs = 'subdir1.subdir2'
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
______________________________ test_error_case_3 _______________________________

    def test_error_case_3():
        with pytest.raises(ValueError) as e:
            collection_ref = AnsibleCollectionRef('ansible.sample', 'invalid_subdirs', 'mymodule', 'module')
>       assert str(e.value) == 'invalid subdirs entry: invalid_subdirs (must be empty/None or of the form subdir1.subdir2)'
E       AssertionError: assert 'invalid coll..._type: module' == 'invalid subd...dir1.subdir2)'
E         
E         - invalid subdirs entry: invalid_subdirs (must be empty/None or of the form subdir1.subdir2)
E         + invalid collection ref_type: module

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_fqcr_0.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_fqcr_0.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_fqcr_0.py::test_valid_case_2
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_fqcr_0.py::test_error_case_3
============================== 3 failed in 0.36s ===============================
"""