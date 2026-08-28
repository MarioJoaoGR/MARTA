
import pytest
from thonny.jedi_utils import get_interpreter_completions


def test_basic_usage():
    source = "import os\nprint"
    namespaces = [{'os': None}]
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) > 0, "Expected some completions but got none."

def test_empty_namespace():
    source = "def myfunc():\n    pass"
    namespaces = []
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) > 0, "Expected some completions but got none."

def test_custom_system_path():
    source = "import os\nprint"
    namespaces = [{'os': None}]
    sys_path = ["/custom/path"]
    completions = get_interpreter_completions(source, namespaces, sys_path)
    assert len(completions) > 0, "Expected some completions but got none."

def test_complex_source_code():
    source = "def myfunc():\n    return some_variable"
    namespaces = [{'some_variable': None}]
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) > 0, "Expected some completions but got none."
