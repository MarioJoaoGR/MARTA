
import pytest
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

def test_RoleMixin__build_doc_basic(role_mixin):
    argspec = {'entry_point': {}}
    fqcn, doc = role_mixin._build_doc('role_name', 'path/to/role', None, argspec, None)
    assert fqcn == 'role_name'
    assert doc['path'] == 'path/to/role'
    assert doc['collection'] is None
    assert len(doc['entry_points']) == 1
    assert list(doc['entry_points'].keys())[0] == 'entry_point'
