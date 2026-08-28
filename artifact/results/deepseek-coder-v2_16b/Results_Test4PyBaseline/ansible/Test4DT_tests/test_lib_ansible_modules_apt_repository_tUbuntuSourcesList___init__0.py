# Module: ansible.modules.apt_repository
# Import the function using its provided module name.
from ansible.modules.apt_repository import UbuntuSourcesList

import pytest
import unittest
from unittest.mock import MagicMock
import distro

# Mocking the necessary modules and classes for testing
class TestUbuntuSourcesList:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.module = MagicMock()
        self.module.params = {'codename': 'focal'}  # Example parameter
        self.add_ppa_signing_keys_callback = None  # No callback for simplicity
        self.instance = UbuntuSourcesList(self.module, self.add_ppa_signing_keys_callback)

    def test_init_with_codename(self):
        assert self.instance.module == self.module
        assert self.instance.add_ppa_signing_keys_callback is None
        assert self.instance.codename == 'focal'

    @pytest.mark.parametrize("params, expected", [
        ({}, 'focal'),  # No codename provided, should auto-detect
        ({'codename': 'bionic'}, 'bionic')  # Provided codename
    ])
    def test_init_with_auto_detection(self, params, expected):
        self.module.params = params
        instance = UbuntuSourcesList(self.module)
        assert instance.codename == expected

    @pytest.mark.parametrize("callback", [lambda: None])  # Example callback function
    def test_init_with_callback(self, callback):
        self.add_ppa_signing_keys_callback = callback
        instance = UbuntuSourcesList(self.module, self.add_ppa_signing_keys_callback)
        assert instance.add_ppa_signing_keys_callback == callback

if __name__ == '__main__':
    pytest.main()
