
import pytest
from docstring_parser import parse
import typing as T

def test_deprecation():
    """Test parsing deprecation notes with version and description."""
    source = """
        A short description.
        
        .. deprecated:: 1.0
            This function will be removed in version 1.0 of the library.
    """
    docstring = parse(source)
    assert docstring.deprecation is not None
    assert docstring.deprecation.version == "1.0"
    assert docstring.deprecation.description == "This function will be removed in version 1.0 of the library."

def test_deprecation_no_version():
    """Test parsing deprecation notes without specifying a version."""
    source = """
        A short description.
        
        .. deprecated::
            This function will be removed without specifying a version.
    """
    docstring = parse(source)
    assert docstring.deprecation is not None
    assert docstring.deprecation.version is None
    assert docstring.deprecation.description == "This function will be removed without specifying a version."

def test_deprecation_no_description():
    """Test parsing deprecation notes with only a version specified."""
    source = """
        A short description.
        
        .. deprecated:: 1.0
    """
    docstring = parse(source)
    assert docstring.deprecation is not None
    assert docstring.deprecation.version == "1.0"
    assert docstring.deprecation.description is None

def test_deprecation_no_content():
    """Test parsing a docstring without any deprecation note."""
    source = """
        A short description without any deprecation note.
    """
    docstring = parse(source)
    assert docstring.deprecation is None
