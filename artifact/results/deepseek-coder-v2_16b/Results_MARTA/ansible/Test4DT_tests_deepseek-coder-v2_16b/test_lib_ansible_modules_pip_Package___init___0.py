
import pytest
from ansible.modules.pip import Package, Requirement


def test_package_with_version():
    pkg = Package("requests", "2.25.1")
    assert pkg.package_name == "requests"
    assert pkg._requirement.project_name == "requests"

def test_package_without_version():
    pkg = Package("setuptools")
    assert pkg.package_name == "setuptools"
    assert pkg._requirement.project_name == "setuptools"