
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
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
>       collection_ref = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7ffa2d1333d0>
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
_________________________ test_invalid_collection_name _________________________

    def test_invalid_collection_name():
        with pytest.raises(ValueError) as e:
            AnsibleCollectionRef('invalid_namespace.sample', 'subdir1.subdir2', 'mymodule', 'module')
>       assert str(e.value) == 'invalid collection name (must be of the form namespace.collection): invalid_namespace.sample'
E       AssertionError: assert 'invalid coll..._type: module' == 'invalid coll...espace.sample'
E         
E         - invalid collection name (must be of the form namespace.collection): invalid_namespace.sample
E         + invalid collection ref_type: module

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py:15: AssertionError
_____________________________ test_invalid_subdirs _____________________________

    def test_invalid_subdirs():
        with pytest.raises(ValueError) as e:
            AnsibleCollectionRef('ansible.sample', 'invalid_subdir', 'mymodule', 'module')
>       assert str(e.value) == 'invalid subdirs entry: invalid_subdir (must be empty/None or of the form subdir1.subdir2)'
E       AssertionError: assert 'invalid coll..._type: module' == 'invalid subd...dir1.subdir2)'
E         
E         - invalid subdirs entry: invalid_subdir (must be empty/None or of the form subdir1.subdir2)
E         + invalid collection ref_type: module

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py:20: AssertionError
____________________________ test_parse_valid_fqcr _____________________________

    def test_parse_valid_fqcr():
>       parsed_ref = AnsibleCollectionRef.from_fqcr('ansible.sample.mymodule', 'module')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/collection_loader/_collection_finder.py:810: in from_fqcr
    return AnsibleCollectionRef(collection_name, subdirs, resource + ext, ref_type)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7ffa2c9aabc0>
collection_name = 'ansible.sample', subdirs = '', resource = 'mymodule'
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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py::test_invalid_collection_name
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py::test_invalid_subdirs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_1.py::test_parse_valid_fqcr
============================== 4 failed in 0.71s ===============================
"""