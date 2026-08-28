
import pytest
from ansible.cli.doc import RoleMixin

# Test case for building documentation with an empty argspec dictionary
def test_build_doc_with_empty_argspec():
    role_mixin = RoleMixin()
    argspec = {}
    fqcn, doc = role_mixin._build_doc('role_name', 'path/to/role', 'collection_name', argspec, None)
    assert fqcn == 'collection_name.role_name'
    assert doc is None

# Test case for building documentation without an entry point