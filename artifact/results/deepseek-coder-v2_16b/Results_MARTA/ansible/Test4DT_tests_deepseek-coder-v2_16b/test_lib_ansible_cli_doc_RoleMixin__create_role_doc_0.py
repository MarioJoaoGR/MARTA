
import pytest
from ansible.cli.doc import RoleMixin

class MockRoleMixin(RoleMixin):
    def __init__(self, roles=None, paths=None):
        self.roles = roles if roles else []
        self.paths = paths if paths else []

    def _find_all_normal_roles(self, role_paths, name_filters=None):
        return [(role, path) for role, path in zip(self.roles, self.paths)]

    def _find_all_collection_roles(self, name_filters=None):
        return [(role, 'collection', 'collection_path') for role in self.roles]

    def _load_argspec(self, role, role_path=None, collection_path=None):
        return {}

    def _build_doc(self, role, role_path, collection, argspec, entry_point=None):
        return (role, {'collection': collection, 'entry_points': [entry_point], 'path': role_path})

def test_valid_inputs_happy_path():
    mock_mixin = MockRoleMixin(roles=['role1', 'role2'], paths=['path1', 'path2'])
    doc = mock_mixin._create_role_doc(('role1', 'role2'), ('path1', 'path2'))
    assert isinstance(doc, dict)
    assert len(doc) == 2
