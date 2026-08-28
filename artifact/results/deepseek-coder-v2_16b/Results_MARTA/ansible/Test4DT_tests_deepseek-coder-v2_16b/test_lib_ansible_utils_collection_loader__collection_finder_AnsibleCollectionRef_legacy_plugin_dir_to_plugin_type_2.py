
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
import re


def test_invalid_ref_type():
    with pytest.raises(ValueError):
        AnsibleCollectionRef('my_namespace.my_collection', None, '', '')


def test_invalid_subdirs():
    with pytest.raises(ValueError):
        AnsibleCollectionRef('my_namespace.my_collection', 'invalid_subdir', 'mymodule', 'module')