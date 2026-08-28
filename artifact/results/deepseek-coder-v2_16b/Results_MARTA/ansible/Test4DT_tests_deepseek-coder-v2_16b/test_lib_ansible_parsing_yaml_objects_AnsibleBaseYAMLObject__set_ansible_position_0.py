
import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject


def test_invalid_input():
    with pytest.raises(TypeError):
        AnsibleBaseYAMLObject("example.yaml", "ten", "twenty")