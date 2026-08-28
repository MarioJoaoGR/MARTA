
import pytest
from apimd.parser import Parser
from types import ModuleType
from unittest.mock import MagicMock

def create_mock_module(attributes: dict) -> ModuleType:
    module = MagicMock()
    for attr_name, docstring in attributes.items():
        attr = MagicMock(__doc__=docstring)
        setattr(module, attr_name, attr)
    return module

def test_load_docstring_no_docstrings():
    p = Parser()
    root = ''
    m = create_mock_module({
        'some_function': None,
        'another_function': None
    })
    p.doc = {'some_function': '', 'another_function': ''}

    p.load_docstring(root, m)

    assert p.docstring == {}


def test_load_docstring_with_actual_docstrings():
    p = Parser()
    root = ''
    m = create_mock_module({
        'some_function': 'This is a docstring for some_function.',
        'another_function': 'This is a docstring for another_function.'
    })
    p.doc = {'some_function': '', 'another_function': ''}

    p.load_docstring(root, m)

    assert p.docstring == {
        'some_function': 'This is a docstring for some_function.',
        'another_function': 'This is a docstring for another_function.'
    }

def test_load_docstring_with_root_namespace():
    p = Parser()
    root = 'mypackage'
    m = create_mock_module({
        'some_function': 'This is a docstring for some_function.',
        'another_function': 'This is a docstring for another_function.'
    })
    p.doc = {'mypackage.some_function': '', 'mypackage.another_function': ''}

    p.load_docstring(root, m)

    assert p.docstring == {
        'mypackage.some_function': 'This is a docstring for some_function.',
        'mypackage.another_function': 'This is a docstring for another_function.'
    }

def test_load_docstring_with_irrelevant_attributes():
    p = Parser()
    root = 'mypackage'
    m = create_mock_module({
        'some_function': 'This is a docstring for some_function.',
        'another_function': 'This is a docstring for another_function.',
        'irrelevant_function': 'This should not be included.'
    })
    p.doc = {'mypackage.some_function': '', 'mypackage.another_function': ''}

    p.load_docstring(root, m)

    assert p.docstring == {
        'mypackage.some_function': 'This is a docstring for some_function.',
        'mypackage.another_function': 'This is a docstring for another_function.'
    }