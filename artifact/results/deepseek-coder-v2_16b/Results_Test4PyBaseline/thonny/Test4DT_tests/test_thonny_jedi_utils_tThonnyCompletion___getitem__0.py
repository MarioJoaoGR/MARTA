# Module: thonny.jedi_utils
import pytest
from thonny.jedi_utils import ThonnyCompletion

# Test case for initializing a ThonnyCompletion instance
def test_thonny_completion_initialization():
    completion = ThonnyCompletion(name="example", complete="ex", type="function", description="An example function", parent=None, full_name="example.func")
    
    assert completion.name == "example"
    assert completion.complete == "ex"
    assert completion.type == "function"
    assert completion.description == "An example function"
    assert completion.parent is None
    assert completion.full_name == "example.func"

# Test case for accessing attributes using __getitem__ method
def test_thonny_completion_getitem():
    completion = ThonnyCompletion(name="example", complete="ex", type="function", description="An example function", parent=None, full_name="example.func")
    
    assert completion['name'] == "example"
    assert completion['complete'] == "ex"
    assert completion['type'] == "function"
    assert completion['description'] == "An example function"
    assert completion['parent'] is None
    assert completion['full_name'] == "example.func"

# Test case for accessing attributes directly after initialization
def test_thonny_completion_direct_access():
    completion = ThonnyCompletion(name="example", complete="ex", type="function", description="An example function", parent=None, full_name="example.func")
    
    assert completion.name == "example"
    assert completion.complete == "ex"
    assert completion.type == "function"
    assert completion.description == "An example function"
    assert completion.parent is None
    assert completion.full_name == "example.func"
