
import pytest
from thonny import jedi_utils
from typing import List, Dict

# Assuming the function `get_interpreter_completions` is defined in a module named `thonny.jedi_utils`
# and that `ThonnyCompletion` is a placeholder for the actual completion objects returned by Jedi.

def test_valid_input():
    source = "import os\nprint"
    namespaces = [{'os': None}]
    completions = jedi_utils.get_interpreter_completions(source, namespaces)
    
    assert len(completions) > 0, "Expected at least one completion but got none."
    for completion in completions:
        assert hasattr(completion, 'name'), "Completion object missing 'name' attribute."
        assert hasattr(completion, 'complete'), "Completion object missing 'complete' attribute."

def test_empty_namespace():
    source = "def myfunc():\n    pass"
    namespaces = []
    completions = jedi_utils.get_interpreter_completions(source, namespaces)
    
    assert len(completions) > 0, "Expected at least one completion but got none."
    for completion in completions:
        assert hasattr(completion, 'name'), "Completion object missing 'name' attribute."
        assert hasattr(completion, 'complete'), "Completion object missing 'complete' attribute."

def test_invalid_input():
    source = None
    namespaces = None
    with pytest.raises(TypeError):
        jedi_utils.get_interpreter_completions(source, namespaces)
