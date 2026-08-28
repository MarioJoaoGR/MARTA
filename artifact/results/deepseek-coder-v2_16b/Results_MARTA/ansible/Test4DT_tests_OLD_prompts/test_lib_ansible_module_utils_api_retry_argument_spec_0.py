
import pytest
from ansible.module_utils.api import retry_argument_spec


def test_edge_cases():
    with pytest.raises(KeyError):
        retry_argument_spec()['non_existent_key']
