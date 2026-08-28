
import pytest
from ansible.modules.pip import Package
import re

@pytest.fixture
def package_with_version():
    return Package("requests", "2.25.1")

@pytest.fixture
def package_without_version():
    return Package("setuptools")

def test_package_name_with_version(package_with_version):
    assert package_with_version.package_name == "requests"

def test_package_name_without_version(package_without_version):
    assert package_without_version.package_name == "setuptools"

