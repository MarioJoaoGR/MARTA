
import pytest
from ansible.parsing.yaml.loader import AnsibleLoader
import io


def test_edge_case():
    with pytest.raises(TypeError):
        loader = AnsibleLoader(None)
