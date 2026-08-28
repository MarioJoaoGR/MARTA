
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
import re


def test_invalid_collection_name():
    with pytest.raises(ValueError):
        AnsibleCollectionRef('invalid-namespace', 'subdir1.subdir2', 'mymodule', 'module')

def test_invalid_ref_type():
    with pytest.raises(ValueError):
        AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'invalid_type')

def test_invalid_subdirs():
    with pytest.raises(ValueError):
        AnsibleCollectionRef('ansible.sample', 'invalid-subdirs', 'mymodule', 'module')


def test_legacy_plugin_dir_to_plugin_type():
    module_type = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins')
    assert module_type == 'action'