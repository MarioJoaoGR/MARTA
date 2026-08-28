
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.chroot import is_chroot

def test_is_chroot_in_debian_chroot():
    with patch('os.environ', {'debian_chroot': True}):
        assert is_chroot() == True

