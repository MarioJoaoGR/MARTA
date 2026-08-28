
import pytest
from ansible.cli.doc import RoleMixin
from ansible.errors import AnsibleError, AnsibleParserError
import os
from yaml import safe_load as from_yaml
from unittest.mock import patch

@pytest.fixture(scope="module")
def role_mixin():
    return RoleMixin()

def test_valid_input_standard_role(role_mixin):
    with pytest.raises(AnsibleError) as excinfo:
        result = role_mixin._load_argspec('my_standard_role')
    assert str(excinfo.value) == "A path is required to load argument specs for role 'my_standard_role'"
