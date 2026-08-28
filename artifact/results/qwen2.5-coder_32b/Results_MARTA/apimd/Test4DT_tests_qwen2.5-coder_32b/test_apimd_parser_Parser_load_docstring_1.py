
"""Test file for Parser class and its load_docstring method."""

import pytest
from apimd.parser import Parser
from types import ModuleType
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

# Helper function to create a mock module from source code
def create_mock_module(name: str, source_code: str) -> ModuleType:
    spec = spec_from_loader(name, SourceFileLoader(name, "<string>"))
    module = module_from_spec(spec)
    exec(source_code, module.__dict__)
    return module

# Test case 1: Basic docstring loading
def test_load_docstring_basic():
    # Create a mock module with a simple function and docstring
    source_code = """
def sample_function():
    \"\"\"This is a sample function.\"\"\"
    pass
"""
    mock_module = create_mock_module("example_pkg", source_code)
    
    # Initialize Parser and set up the internal state
    p = Parser()
    p.doc = {'example_pkg.sample_function': 'This is a sample function.'}
    
    # Load docstring from the mock module
    p.load_docstring('example_pkg', mock_module)
    
    # Assert that the docstring was loaded correctly
    assert p.docstring['example_pkg.sample_function'] == "This is a sample function."

# Test case 2: No matching root namespace
def test_load_docstring_no_matching_root():
    # Create a mock module with a simple function and docstring
    source_code = """
def sample_function():
    \"\"\"This is a sample function.\"\"\"
    pass
"""
    mock_module = create_mock_module("example_pkg", source_code)
    
    # Initialize Parser and set up the internal state with a different root namespace
    p = Parser()
    p.doc = {'different_root.sample_function': 'This is a sample function.'}
    
    # Load docstring from the mock module
    p.load_docstring('example_pkg', mock_module)
    
    # Assert that no docstring was loaded because of mismatched root namespace
    assert not p.docstring

# Test case 3: Multiple functions with docstrings
def test_load_docstring_multiple_functions():
    # Create a mock module with multiple functions and docstrings
    source_code = """
def function_one():
    \"\"\"This is the first function.\"\"\"
    pass

def function_two():
    \"\"\"This is the second function.\"\"\"
    pass
"""
    mock_module = create_mock_module("example_pkg", source_code)
    
    # Initialize Parser and set up the internal state
    p = Parser()
    p.doc = {
        'example_pkg.function_one': 'This is the first function.',
        'example_pkg.function_two': 'This is the second function.'
    }
    
    # Load docstring from the mock module
    p.load_docstring('example_pkg', mock_module)
    
    # Assert that both docstrings were loaded correctly
    assert p.docstring['example_pkg.function_one'] == "This is the first function."
    assert p.docstring['example_pkg.function_two'] == "This is the second function."

# Test case 4: Function with no docstring
def test_load_docstring_no_docstring():
    # Create a mock module with a function that has no docstring
    source_code = """
def sample_function():
    pass
"""
    mock_module = create_mock_module("example_pkg", source_code)
    
    # Initialize Parser and set up the internal state
    p = Parser()
    p.doc = {'example_pkg.sample_function': 'This is a sample function.'}
    
    # Load docstring from the mock module
    p.load_docstring('example_pkg', mock_module)
    
    # Assert that no docstring was loaded because the function has no docstring
    assert not p.docstring.get('example_pkg.sample_function')
