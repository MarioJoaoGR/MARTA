
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.pip import Requirement, Package
import re



def test_canonicalize_name():
    name = "setuptools"
    canonicalized_name = Package.canonicalize_name(name)
    assert canonicalized_name == "setuptools"