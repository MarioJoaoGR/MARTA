
import pytest
from pathlib import Path
from isort.place import _is_namespace_package

@pytest.fixture
def namespace_pkg_path():
    return Path("test_dir")

@pytest.fixture
def non_namespace_pkg_path():
    return Path("test_dir")

def test_is_namespace_package(namespace_pkg_path, non_namespace_pkg_path):
    # Create a mock directory for the namespace package
    (namespace_pkg_path / "__init__.py").touch()
    
    # Add content to __init__.py that indicates it's a namespace package
    (namespace_pkg_path / "__init__.py").write_text(
        "__import__('pkg_resources').declare_namespace(__name__)"
    )
    
    assert _is_namespace_package(namespace_pkg_path, frozenset(['py', 'cpp'])) == True

def test_non_namespace_package(non_namespace_pkg_path):
    # Create a mock directory for the non-namespace package
    (non_namespace_pkg_path / "__init__.py").touch()
    
    # Add content to __init__.py that does not indicate it's a namespace package
    (non_namespace_pkg_path / "__init__.py").write_text("This is just an init file.")
    
    assert _is_namespace_package(non_namespace_pkg_path, frozenset(['txt', 'md'])) == False
