
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
import re

def to_text(s, errors='strict'):
    return s

def to_native(s):
    return s

class TestAnsibleCollectionRef:
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.collection_ref = AnsibleCollectionRef('my_namespace.my_collection', 'subdir1.subdir2', 'mymodule', 'module')

    def test_valid_case(self):
        assert self.collection_ref.collection == 'my_namespace.my_collection'
        assert self.collection_ref.subdirs == 'subdir1.subdir2'
        assert self.collection_ref.resource == 'mymodule'
        assert self.collection_ref.ref_type == 'module'

    def test_edge_case(self):
        edge_collection_ref = AnsibleCollectionRef('my_namespace.my_collection', None, '', '')
        assert edge_collection_ref.collection == 'my_namespace.my_collection'
        assert edge_collection_ref.subdirs == ''
        assert edge_collection_ref.resource == ''
        assert edge_collection_ref.ref_type == ''

    def test_error_case(self):
        with pytest.raises(ValueError) as excinfo:
            invalid_collection_ref = AnsibleCollectionRef('invalid_namespace', 'subdir1.subdir2', 'mymodule', 'module')
        assert str(excinfo.value) == 'invalid collection name (must be of the form namespace.collection): invalid_namespace'

        with pytest.raises(ValueError) as excinfo:
            invalid_ref_type_ref = AnsibleCollectionRef('my_namespace.my_collection', 'subdir1.subdir2', 'mymodule', 'invalid_type')
        assert str(excinfo.value) == 'invalid collection ref_type: invalid_type'

        with pytest.raises(ValueError) as excinfo:
            invalid_subdirs_ref = AnsibleCollectionRef('my_namespace.my_collection', 'invalid_subdir', 'mymodule', 'module')
        assert str(excinfo.value) == 'invalid subdirs entry: invalid_subdir (must be empty/None or of the form subdir1.subdir2)'
