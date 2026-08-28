
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

# Test cases for the __init__ method of AnsibleCollectionRef class

def test_valid_initialization():
    acr = AnsibleCollectionRef('ansible.demo', 'roles', 'mymodule', 'module')
    assert acr.collection == 'ansible.demo'
    assert acr.subdirs == 'roles'
    assert acr.resource == 'mymodule'
    assert acr.ref_type == 'module'

def test_valid_initialization_with_subdirs():
    acr = AnsibleCollectionRef('ansible.demo', 'roles.subdir1', 'mymodule', 'module')
    assert acr.collection == 'ansible.demo'
    assert acr.subdirs == 'roles.subdir1'
    assert acr.resource == 'mymodule'
    assert acr.ref_type == 'module'

def test_valid_initialization_without_subdirs():
    acr = AnsibleCollectionRef('ansible.demo', None, 'mymodule', 'module')
    assert acr.collection == 'ansible.demo'
    assert acr.subdirs == ''
    assert acr.resource == 'mymodule'
    assert acr.ref_type == 'module'

def test_invalid_collection_name():
    with pytest.raises(ValueError) as e:
        acr = AnsibleCollectionRef('invalid.name', 'roles', 'mymodule', 'module')
    assert str(e.value) == "invalid collection name (must be of the form namespace.collection): invalid.name"

def test_invalid_ref_type():
    with pytest.raises(ValueError) as e:
        acr = AnsibleCollectionRef('ansible.demo', 'roles', 'mymodule', 'invalid_type')
    assert str(e.value) == "invalid collection ref_type: invalid_type"

def test_invalid_subdirs():
    with pytest.raises(ValueError) as e:
        acr = AnsibleCollectionRef('ansible.demo', 'invalid.subdirs', 'mymodule', 'module')
    assert str(e.value) == "invalid subdirs entry: invalid.subdirs (must be empty/None or of the form subdir1.subdir2)"

def test_from_fqcr():
    acr = AnsibleCollectionRef.from_fqcr('ansible.demo.roles.mymodule', 'module')
    assert acr.collection == 'ansible.demo'
    assert acr.subdirs == 'roles'
    assert acr.resource == 'mymodule'
    assert acr.ref_type == 'module'

def test_from_fqcr_with_subdirs():
    acr = AnsibleCollectionRef.from_fqcr('ansible.demo.roles.subdir1.mymodule', 'module')
    assert acr.collection == 'ansible.demo'
    assert acr.subdirs == 'roles.subdir1'
    assert acr.resource == 'mymodule'
    assert acr.ref_type == 'module'

def test_from_fqcr_without_subdirs():
    acr = AnsibleCollectionRef.from_fqcr('ansible.demo.roles.mymodule', 'module')
    assert acr.collection == 'ansible.demo'
    assert acr.subdirs == 'roles'
    assert acr.resource == 'mymodule'
    assert acr.ref_type == 'module'

def test_invalid_fqcr():
    with pytest.raises(ValueError) as e:
        acr = AnsibleCollectionRef.from_fqcr('invalid.collection.reference', 'module')
    assert str(e.value) == "invalid collection reference"
