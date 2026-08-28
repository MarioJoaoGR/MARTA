
import pytest
from pkg_resources import Requirement

# Test cases for _is_present function
def test_valid_case_1():
    req = Requirement('requests', '2.25.1')
    installed_pkgs = ['requests==2.25.1', 'setuptools']
    module = None
    pkg_command = None
    assert _is_present(module, req, installed_pkgs, pkg_command) == True

def test_valid_case_2():
    req = Requirement('requests', '2.24.0')
    installed_pkgs = ['requests==2.25.1', 'setuptools']
    module = None
    pkg_command = None
    assert _is_present(module, req, installed_pkgs, pkg_command) == False

def test_valid_case_3():
    req = Requirement('setuptools')
    installed_pkgs = ['requests==2.25.1', 'setuptools']
    module = None
    pkg_command = None
    assert _is_present(module, req, installed_pkgs, pkg_command) == True

def test_missing_case_1():
    req = Requirement('nonexistentpackage', '1.0')
    installed_pkgs = ['requests==2.25.1', 'setuptools']
    module = None
    pkg_command = None
    assert _is_present(module, req, installed_pkgs, pkg_command) == False

def test_missing_case_2():
    req = Requirement('requests', '2.25.1')
    installed_pkgs = []
    module = None
    pkg_command = None
    assert _is_present(module, req, installed_pkgs, pkg_command) == False

def test_missing_case_3():
    req = Requirement('requests', '2.25.1')
    installed_pkgs = None
    module = None
    pkg_command = None
    assert _is_present(module, req, installed_pkgs, pkg_command) == False

def test_error_case_1():
    req = 'invalid_requirement'
    installed_pkgs = ['requests==2.25.1', 'setuptools']
    module = None
    pkg_command = None
    with pytest.raises(TypeError):
        _is_present(module, req, installed_pkgs, pkg_command)

def test_error_case_2():
    req = Requirement('requests', '2.25.1')
    installed_pkgs = 123
    module = None
    pkg_command = None
    with pytest.raises(TypeError):
        _is_present(module, req, installed_pkgs, pkg_command)
