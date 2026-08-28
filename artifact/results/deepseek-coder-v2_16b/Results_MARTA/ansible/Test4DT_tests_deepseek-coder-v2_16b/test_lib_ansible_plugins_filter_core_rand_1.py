
import pytest
from ansible.plugins.filter.core import rand
from ansible.errors import AnsibleFilterError
from random import SystemRandom, Random
from unittest.mock import patch



def test_rand_invalid_parameters():
    with pytest.raises(AnsibleFilterError):
        rand(None, None)