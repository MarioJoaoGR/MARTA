
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

# Test cases for the __init__ method of AnsibleCollectionRef class

def test_valid_initialization():
    collection_ref = AnsibleCollectionRef('ansible.example', None, 'mymodule', 'module')
    assert collection_ref.collection == 'ansible.example'
    assert collection_ref.subdirs == ''
    assert collection_ref.resource == 'mymodule'
    assert collection_ref.ref_type == 'module'

def test_valid_initialization_with_subdirs():
    collection_ref = AnsibleCollectionRef('ansible.example', 'roles', 'mymodule', 'module')
    assert collection_ref.collection == 'ansible.example'
    assert collection_ref.subdirs == 'roles'
    assert collection_ref.resource == 'mymodule'
    assert collection_ref.ref_type == 'module'

def test_valid_initialization_with_empty_resource():
    collection_ref = AnsibleCollectionRef('ansible.example', 'roles', '', 'module')
    assert collection_ref.collection == 'ansible.example'
    assert collection_ref.subdirs == 'roles'
    assert collection_ref.resource == ''
    assert collection_ref.ref_type == 'module'

def test_valid_initialization_with_empty_ref_type():
    collection_ref = AnsibleCollectionRef('ansible.example', 'roles', 'mymodule', '')
    assert collection_ref.collection == 'ansible.example'
    assert collection_ref.subdirs == 'roles'
    assert collection_ref.resource == 'mymodule'
    assert collection_ref.ref_type == ''

def test_invalid_collection_name():
    with pytest.raises(ValueError) as e:
        collection_ref = AnsibleCollectionRef('invalid.name', 'roles', 'mymodule', 'module')
    assert str(e.value) == "invalid collection name (must be of the form namespace.collection): invalid.name"

def test_invalid_ref_type():
    with pytest.raises(ValueError) as e:
        collection_ref = AnsibleCollectionRef('ansible.example', 'roles', 'mymodule', 'invalid_type')
    assert str(e.value) == "invalid collection ref_type: invalid_type"

def test_invalid_subdirs_format():
    with pytest.raises(ValueError) as e:
        collection_ref = AnsibleCollectionRef('ansible.example', 'invalid-subdirs', 'mymodule', 'module')
    assert str(e.value) == "invalid subdirs entry: invalid-subdirs (must be empty/None or of the form subdir1.subdir2)"

# Test cases for the try_parse_fqcr method

def test_valid_try_parse_fqcr():
    collection_ref = AnsibleCollectionRef.try_parse_fqcr('ansible.example.roles.mymodule', 'module')
    assert isinstance(collection_ref, AnsibleCollectionRef)
    assert collection_ref.collection == 'ansible.example'
    assert collection_ref.subdirs == 'roles'
    assert collection_ref.resource == 'mymodule'
    assert collection_ref.ref_type == 'module'

def test_invalid_try_parse_fqcr():
    collection_ref = AnsibleCollectionRef.try_parse_fqcr('ansible.example.roles.invalid', 'module')
    assert collection_ref is None
