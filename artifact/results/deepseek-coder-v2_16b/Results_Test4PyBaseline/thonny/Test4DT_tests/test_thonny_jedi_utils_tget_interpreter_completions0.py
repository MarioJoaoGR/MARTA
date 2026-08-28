
import pytest
from typing import List, Dict
from thonny.jedi_utils import get_interpreter_completions

# Test cases for get_interpreter_completions function

def test_basic_usage():
    source_code = "def my_function():\n    pass"
    namespaces_context = [{'my_function': None}]
    completions = get_interpreter_completions(source_code, namespaces_context)
    assert len(completions) > 0, "Expected at least one completion but got none."
    for completion in completions:
        assert isinstance(completion.name, str), f"Completion name should be a string, got {type(completion.name)}"