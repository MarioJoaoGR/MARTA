
import pytest
from ansible.vars.manager import VarsWithSources


def test_invalid_input():
    with pytest.raises(KeyError):
        VarsWithSources().__getitem__('non_existent_key')