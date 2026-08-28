
import pytest
from unittest.mock import MagicMock, ModuleType
from apimd.parser import Parser

def test_load_docstring_with_valid_module():
    # Arrange
    p = Parser()
    p.doc['some_module.ClassName'] = 'Description of ClassName'
    p.doc['some_module.FunctionName'] = 'Description of FunctionName'
    
    mock_module = MagicMock(spec=ModuleType)
    type(mock_module).ClassName = MagicMock(__doc__="This is the docstring for ClassName.")
    type(mock_module).FunctionName = MagicMock(__doc__="This is the docstring for FunctionName.")

    # Act
    p.load_docstring('some_module', mock_module)

    # Assert
    assert p.docstring == {
        'some_module.ClassName': 'This is the docstring for ClassName.',
        'some_module.FunctionName': 'This is the docstring for FunctionName.'
    }

def test_load_docstring_with_no_matching_root():
    # Arrange
    p = Parser()
    p.doc['other_module.ClassName'] = 'Description of ClassName'
    
    mock_module = MagicMock(spec=ModuleType)
    type(mock_module).ClassName = MagicMock(__doc__="This is the docstring for ClassName.")

    # Act
    p.load_docstring('some_module', mock_module)

    # Assert
    assert p.docstring == {}

def test_load_docstring_with_no_docstrings():
    # Arrange
    p = Parser()
    p.doc['some_module.ClassName'] = 'Description of ClassName'
    
    mock_module = MagicMock(spec=ModuleType)
    type(mock_module).ClassName = MagicMock(__doc__=None)

    # Act
    p.load_docstring('some_module', mock_module)

    # Assert
    assert p.docstring == {}

def test_load_docstring_with_partial_matching_root():
    # Arrange
    p = Parser()
    p.doc['some_module.ClassName'] = 'Description of ClassName'
    p.doc['some_module.submodule.FunctionName'] = 'Description of FunctionName'
    
    mock_module = MagicMock(spec=ModuleType)
    type(mock_module).ClassName = MagicMock(__doc__="This is the docstring for ClassName.")
    mock_submodule = MagicMock(spec=ModuleType)
    type(mock_submodule).FunctionName = MagicMock(__doc__="This is the docstring for FunctionName.")
    mock_module.submodule = mock_submodule

    # Act
    p.load_docstring('some_module', mock_module)

    # Assert
    assert p.docstring == {
        'some_module.ClassName': 'This is the docstring for ClassName.',
        'some_module.submodule.FunctionName': 'This is the docstring for FunctionName.'
    }

def test_load_docstring_with_empty_doc_dict():
    # Arrange
    p = Parser()
    
    mock_module = MagicMock(spec=ModuleType)

    # Act
    p.load_docstring('some_module', mock_module)

    # Assert