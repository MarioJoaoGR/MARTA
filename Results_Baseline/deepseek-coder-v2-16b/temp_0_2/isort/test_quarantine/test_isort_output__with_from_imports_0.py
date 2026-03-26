
# Module: isort.output
# test_isort_output.py
from isort.output import _with_from_imports
from isort.api import ParsedContent
from isort.settings import Config
import pytest

@pytest.fixture
def parsed_content():
    return ParsedContent()

@pytest.fixture
def config():
    return Config()

def test_with_from_imports_basic(parsed_content, config):
    result = _with_from_imports(
        parsed=parsed_content,
        config=config,
        from_modules=['os', 'sys'],
        section='section_name',
        remove_imports=[],
        import_type='import'
    )
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(item, str) for item in result)

def test_with_from_imports_remove_imports(parsed_content, config):
    result = _with_from_imports(
        parsed=parsed_content,
        config=config,
        from_modules=['os', 'sys'],
        section='section_name',
        remove_imports=['os'],
        import_type='import'
    )
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == "from sys import *"

def test_with_from_imports_only_sections(parsed_content, config):
    config.only_sections = True
    result = _with_from_imports(
        parsed=parsed_content,
        config=config,
        from_modules=['os', 'sys'],
        section='section_name',
        remove_imports=[],
        import_type='import'
    )
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(item, str) for item in result)

def test_with_from_imports_force_single_line(parsed_content, config):
    config.force_single_line = True
    result = _with_from_imports(
        parsed=parsed_content,
        config=config,
        from_modules=['os', 'sys'],
        section='section_name',
        remove_imports=[],
        import_type='import'
    )
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(item, str) for item in result)

def test_with_from_imports_no_inline_sort(parsed_content, config):
    config.no_inline_sort = True
    result = _with_from_imports(
        parsed=parsed_content,
        config=config,
        from_modules=['os', 'sys'],
        section='section_name',
        remove_imports=[],
        import_type='import'
    )
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(item, str) for item in result)

def test_with_from_imports_reverse_sort(parsed_content, config):
    config.reverse_sort = True
    result = _with_from_imports(
        parsed=parsed_content,
        config=config,
        from_modules=['os', 'sys'],
        section='section_name',
        remove_imports=[],
        import_type='import'
    )
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(item, str) for item in result)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_output__with_from_imports_0
isort/Test4DT_tests/test_isort_output__with_from_imports_0.py:5:0: E0611: No name 'ParsedContent' in module 'isort.api' (no-name-in-module)


"""