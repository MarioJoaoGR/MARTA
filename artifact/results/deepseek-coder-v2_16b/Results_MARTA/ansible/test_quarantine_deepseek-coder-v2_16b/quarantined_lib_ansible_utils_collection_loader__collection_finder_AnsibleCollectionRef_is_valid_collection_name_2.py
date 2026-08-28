
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

class TestAnsibleCollectionRef:
    
    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module'),
        ('another.namespace', '', 'resource', 'action')
    ])
    def test_valid_inputs(self, collection_name, subdirs, resource, ref_type):
        acr = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        assert acr.collection == collection_name
        assert acr.subdirs == subdirs if subdirs else ''
    
    def test_invalid_subdirs(self):
        with pytest.raises(ValueError) as e:
            AnsibleCollectionRef('ansible.sample', 'invalid-subdirs', 'mymodule', 'module')
        assert str(e.value) == f'invalid subdirs entry: {to_native("invalid-subdirs")} (must be empty/None or of the form subdir1.subdir2)'
    
    @pytest.mark.parametrize("collection_name, subdirs", [
        ('ansible.sample', 'subdir1.subdir2'),
        ('another.namespace', '')
    ])
    def test_valid_subdirs(self, collection_name, subdirs):
        acr = AnsibleCollectionRef(collection_name, subdirs, 'mymodule', 'module')
        assert acr.collection == collection_name
        assert acr.subdirs == subdirs if subdirs else ''
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_ TestAnsibleCollectionRef.test_valid_inputs[ansible.sample-subdir1.subdir2-mymodule-module] _

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.TestAnsibleCollectionRef object at 0x7fbcc8801690>
collection_name = 'ansible.sample', subdirs = 'subdir1.subdir2'
resource = 'mymodule', ref_type = 'module'

    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module'),
        ('another.namespace', '', 'resource', 'action')
    ])
    def test_valid_inputs(self, collection_name, subdirs, resource, ref_type):
>       acr = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7fbcc87dbdc0>
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
_ TestAnsibleCollectionRef.test_valid_inputs[another.namespace--resource-action] _

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.TestAnsibleCollectionRef object at 0x7fbcc87db670>
collection_name = 'another.namespace', subdirs = '', resource = 'resource'
ref_type = 'action'

    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module'),
        ('another.namespace', '', 'resource', 'action')
    ])
    def test_valid_inputs(self, collection_name, subdirs, resource, ref_type):
        acr = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        assert acr.collection == collection_name
>       assert acr.subdirs == subdirs if subdirs else ''
E       AssertionError: assert ''

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py:14: AssertionError
________________ TestAnsibleCollectionRef.test_invalid_subdirs _________________

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.TestAnsibleCollectionRef object at 0x7fbcc87db880>

    def test_invalid_subdirs(self):
        with pytest.raises(ValueError) as e:
            AnsibleCollectionRef('ansible.sample', 'invalid-subdirs', 'mymodule', 'module')
>       assert str(e.value) == f'invalid subdirs entry: {to_native("invalid-subdirs")} (must be empty/None or of the form subdir1.subdir2)'
E       NameError: name 'to_native' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py:19: NameError
_ TestAnsibleCollectionRef.test_valid_subdirs[ansible.sample-subdir1.subdir2] __

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.TestAnsibleCollectionRef object at 0x7fbcc87dba60>
collection_name = 'ansible.sample', subdirs = 'subdir1.subdir2'

    @pytest.mark.parametrize("collection_name, subdirs", [
        ('ansible.sample', 'subdir1.subdir2'),
        ('another.namespace', '')
    ])
    def test_valid_subdirs(self, collection_name, subdirs):
>       acr = AnsibleCollectionRef(collection_name, subdirs, 'mymodule', 'module')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7fbcc7fae650>
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
_______ TestAnsibleCollectionRef.test_valid_subdirs[another.namespace-] ________

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.TestAnsibleCollectionRef object at 0x7fbcc87dbb80>
collection_name = 'another.namespace', subdirs = ''

    @pytest.mark.parametrize("collection_name, subdirs", [
        ('ansible.sample', 'subdir1.subdir2'),
        ('another.namespace', '')
    ])
    def test_valid_subdirs(self, collection_name, subdirs):
>       acr = AnsibleCollectionRef(collection_name, subdirs, 'mymodule', 'module')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7fbcc7febee0>
collection_name = 'another.namespace', subdirs = '', resource = 'mymodule'
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py::TestAnsibleCollectionRef::test_valid_inputs[ansible.sample-subdir1.subdir2-mymodule-module]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py::TestAnsibleCollectionRef::test_valid_inputs[another.namespace--resource-action]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py::TestAnsibleCollectionRef::test_invalid_subdirs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py::TestAnsibleCollectionRef::test_valid_subdirs[ansible.sample-subdir1.subdir2]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_is_valid_collection_name_2.py::TestAnsibleCollectionRef::test_valid_subdirs[another.namespace-]
============================== 5 failed in 0.79s ===============================
"""