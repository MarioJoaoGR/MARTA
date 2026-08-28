
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

class TestAnsibleCollectionRef:
    
    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module')
    ])
    def test_valid_case_1(self, collection_name, subdirs, resource, ref_type):
        collection_ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        assert collection_ref.collection == 'ansible.sample'
        assert collection_ref.subdirs == 'subdir1.subdir2'
        assert collection_ref.resource == 'mymodule'
        assert collection_ref.ref_type == 'module'
    
    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', None, '', '')
    ])
    def test_error_case_3(self, collection_name, subdirs, resource, ref_type):
        with pytest.raises(ValueError) as e:
            AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        assert str(e.value) == 'invalid subdirs entry:  (must be empty/None or of the form subdir1.subdir2)'
    
    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', None, 'a_role', 'role')
    ])
    def test_valid_case_2(self, collection_name, subdirs, resource, ref_type):
        role_ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        assert role_ref.collection == 'ansible.sample'
        assert role_ref.subdirs == ''
        assert role_ref.resource == 'a_role'
        assert role_ref.ref_type == 'role'
    
    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', None, 'myplaybook', 'playbook')
    ])
    def test_valid_case_3(self, collection_name, subdirs, resource, ref_type):
        playbook_ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        assert playbook_ref.collection == 'ansible.sample'
        assert playbook_ref.subdirs == ''
        assert playbook_ref.resource == 'myplaybook'
        assert playbook_ref.ref_type == 'playbook'
    
    @pytest.mark.parametrize("fqcr, ref_type", [
        ('ansible.sample.mymodule', 'module')
    ])
    def test_valid_case_4(self, fqcr, ref_type):
        parsed_ref = AnsibleCollectionRef.from_fqcr(fqcr, ref_type)
        assert parsed_ref.collection == 'ansible.sample'
        assert parsed_ref.subdirs == ''
        assert parsed_ref.resource == 'mymodule'
        assert parsed_ref.ref_type == 'module'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.py F [ 20%]
F..F                                                                     [100%]

=================================== FAILURES ===================================
_ TestAnsibleCollectionRef.test_valid_case_1[ansible.sample-subdir1.subdir2-mymodule-module] _

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.TestAnsibleCollectionRef object at 0x7fbd63d8a0e0>
collection_name = 'ansible.sample', subdirs = 'subdir1.subdir2'
resource = 'mymodule', ref_type = 'module'

    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module')
    ])
    def test_valid_case_1(self, collection_name, subdirs, resource, ref_type):
>       collection_ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7fbd63d8ada0>
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
______ TestAnsibleCollectionRef.test_error_case_3[ansible.sample-None--] _______

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.TestAnsibleCollectionRef object at 0x7fbd63d8a3e0>
collection_name = 'ansible.sample', subdirs = None, resource = '', ref_type = ''

    @pytest.mark.parametrize("collection_name, subdirs, resource, ref_type", [
        ('ansible.sample', None, '', '')
    ])
    def test_error_case_3(self, collection_name, subdirs, resource, ref_type):
        with pytest.raises(ValueError) as e:
            AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
>       assert str(e.value) == 'invalid subdirs entry:  (must be empty/None or of the form subdir1.subdir2)'
E       AssertionError: assert 'invalid coll...on ref_type: ' == 'invalid subd...dir1.subdir2)'
E         
E         - invalid subdirs entry:  (must be empty/None or of the form subdir1.subdir2)
E         + invalid collection ref_type:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.py:23: AssertionError
__ TestAnsibleCollectionRef.test_valid_case_4[ansible.sample.mymodule-module] __

self = <test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.TestAnsibleCollectionRef object at 0x7fbd63d8a020>
fqcr = 'ansible.sample.mymodule', ref_type = 'module'

    @pytest.mark.parametrize("fqcr, ref_type", [
        ('ansible.sample.mymodule', 'module')
    ])
    def test_valid_case_4(self, fqcr, ref_type):
>       parsed_ref = AnsibleCollectionRef.from_fqcr(fqcr, ref_type)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.py:49: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/collection_loader/_collection_finder.py:810: in from_fqcr
    return AnsibleCollectionRef(collection_name, subdirs, resource + ext, ref_type)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'AnsibleCollectionRef' object has no attribute 'collection'") raised in repr()] AnsibleCollectionRef object at 0x7fbd63bf2080>
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.py::TestAnsibleCollectionRef::test_valid_case_1[ansible.sample-subdir1.subdir2-mymodule-module]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.py::TestAnsibleCollectionRef::test_error_case_3[ansible.sample-None--]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder_AnsibleCollectionRef_from_fqcr_0.py::TestAnsibleCollectionRef::test_valid_case_4[ansible.sample.mymodule-module]
========================= 3 failed, 2 passed in 0.42s ==========================
"""