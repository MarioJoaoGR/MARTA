
import pytest
from ansible.modules.pip import Package
import re



def test_canonicalize_name():
    canonicalized_name = Package.canonicalize_name("setuptools")
    assert canonicalized_name == "setuptools"