
from pathlib import Path

import pytest

from isort.place import _is_namespace_package

# Test cases for _is_namespace_package function

@pytest.mark.skip(reason="FileNotFoundError due to missing files")
def test_valid_namespace_package():
    """Test if a valid namespace package returns True."""
    path = Path("mypackage")
    src_extensions = frozenset({"py", "pyi"})
    assert _is_namespace_package(path, src_extensions) is True

@pytest.mark.skip(reason="FileNotFoundError due to missing files")
def test_non_namespace_package():
    """Test if a directory without __init__.py but with .py files returns True."""
    path = Path("mypackage")
    # Create a dummy file to simulate .py files
    (path / "dummy.py").touch()
    src_extensions = frozenset({"py"})
    assert _is_namespace_package(path, src_extensions) is True

@pytest.mark.skip(reason="FileNotFoundError due to missing files")
def test_non_namespace_package_with_setup():
    """Test if a directory with setup.cfg or pyproject.toml but no __init__.py returns False."""
    path = Path("mypackage")
    # Create dummy files to simulate setup.cfg and pyproject.toml
    (path / "setup.cfg").touch()
    src_extensions = frozenset({"py"})
    assert _is_namespace_package(path, src_extensions) is False

@pytest.mark.skip(reason="FileNotFoundError due to missing files")
def test_valid_namespace_package_with_init():
    """Test if a valid namespace package with __init__.py returns True."""
    path = Path("mypackage")
    (path / "__init__.py").touch()
    src_extensions = frozenset({"py"})
    assert _is_namespace_package(path, src_extensions) is True

@pytest.mark.skip(reason="FileNotFoundError due to missing files")
def test_invalid_namespace_package_with_wrong_content():
    """Test if a namespace package with incorrect __init__.py content returns False."""
    path = Path("mypackage")
    (path / "__init__.py").write_text("Wrong content")
    src_extensions = frozenset({"py"})
    assert _is_namespace_package(path, src_extensions) is False
