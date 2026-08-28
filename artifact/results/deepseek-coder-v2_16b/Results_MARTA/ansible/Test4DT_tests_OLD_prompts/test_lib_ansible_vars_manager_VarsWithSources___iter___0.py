
import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.manager import VarsWithSources


def test_edge_cases():
    vs = VarsWithSources({None: None, 'empty': []})
    with pytest.raises(KeyError):
        vs['non_existent_key']