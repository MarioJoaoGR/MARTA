
import ast
import pytest
from py_backwards.transformers.variables_annotations import VariablesAnnotationsTransformer, TransformationResult

def test_valid_input():
    source = 'a: int = 10\nb: int'
    tree = ast.parse(source)
    transformer = VariablesAnnotationsTransformer()
    result = transformer.transform(tree)
    assert isinstance(result, TransformationResult), "Expected a TransformationResult instance"

def test_edge_case():
    source = ''
    tree = ast.parse(source)
    transformer = VariablesAnnotationsTransformer()
    result = transformer.transform(tree)
    assert isinstance(result, TransformationResult), "Expected a TransformationResult instance"

def test_invalid_input():
    source = 'a: int = 10\nb: int\n'
    tree = ast.parse(source)
    transformer = VariablesAnnotationsTransformer()
    result = transformer.transform(tree)
    assert isinstance(result, TransformationResult), "Expected a TransformationResult instance"
