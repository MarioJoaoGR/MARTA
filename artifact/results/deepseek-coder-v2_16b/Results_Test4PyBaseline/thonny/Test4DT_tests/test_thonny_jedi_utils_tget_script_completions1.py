
import pytest
from thonny.jedi_utils import get_script_completions

# Test cases for basic usage scenario
def test_basic_usage():
    source = "import os\nprint"
    completions = get_script_completions(source, 1, 7, "example.py")
    assert len(completions) > 0, "Expected at least one completion but got none."
    for completion in completions:
        assert hasattr(completion, 'name'), f"Completion {completion} does not have a name attribute."
        assert hasattr(completion, 'complete'), f"Completion {completion} does not have a complete attribute."

# Test cases for specific cursor position scenario
def test_specific_cursor_position():
    source = "import os\n# Here is the cursor"
    completions = get_script_completions(source, 1, 0, "example.py")
    assert len(completions) > 0, "Expected at least one completion but got none."
    for completion in completions:
        assert hasattr(completion, 'name'), f"Completion {completion} does not have a name attribute."
        assert hasattr(completion, 'complete'), f"Completion {completion} does not have a complete attribute."

# Test cases for with sys path scenario
def test_with_sys_path():
    source = "import os\nprint"
    completions = get_script_completions(source, 1, 7, "example.py", sys_path=["/custom/path"])
    assert len(completions) > 0, "Expected at least one completion but got none."
    for completion in completions:
        assert hasattr(completion, 'name'), f"Completion {completion} does not have a name attribute."
        assert hasattr(completion, 'complete'), f"Completion {completion} does not have a complete attribute."

# Test cases for edge cases scenario
def test_edge_cases():
    source = "import os\n# Incomplete statement"
    completions = get_script_completions(source, 1, 0, "example.py")
    assert len(completions) > 0, "Expected at least one completion but got none."
    for completion in completions:
        assert hasattr(completion, 'name'), f"Completion {completion} does not have a name attribute."