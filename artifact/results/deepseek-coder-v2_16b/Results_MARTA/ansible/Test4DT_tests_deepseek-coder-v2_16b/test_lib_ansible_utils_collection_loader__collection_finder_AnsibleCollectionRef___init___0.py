
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
import re

def to_text(value, errors='strict'):
    return value

def to_native(value):
    return value

class TestAnsibleCollectionRef:
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.collection_ref = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module')

    def test_valid_inputs(self):
        collection_ref = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'module')
        assert collection_ref.collection == 'ansible.sample'
        assert collection_ref.subdirs == 'subdir1.subdir2'
        assert collection_ref.resource == 'mymodule'
        assert collection_ref.ref_type == 'module'

    def test_edge_cases(self):
        with pytest.raises(ValueError) as e:
            collection_ref = AnsibleCollectionRef('ansible.sample', None, '', 'module')
        assert str(e.value) == "invalid subdirs entry:  (must be empty/None or of the form subdir1.subdir2)"
        
        with pytest.raises(ValueError) as e:
            collection_ref = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', None, 'module')
        assert str(e.value) == "invalid resource entry:  (must be empty/None or a valid string)"
        
        with pytest.raises(ValueError) as e:
            collection_ref = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', None)
        assert str(e.value) == "invalid ref_type entry:  (must be empty/None or a valid string)"

    def test_invalid_inputs(self):
        with pytest.raises(ValueError) as e:
            collection_ref = AnsibleCollectionRef('invalid-namespace', 'subdir1.subdir2', 'mymodule', 'module')
        assert str(e.value) == "invalid collection name (must be of the form namespace.collection): invalid-namespace"
        
        with pytest.raises(ValueError) as e:
            collection_ref = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'invalid_type')
        assert str(e.value) == "invalid collection ref_type: invalid_type"
