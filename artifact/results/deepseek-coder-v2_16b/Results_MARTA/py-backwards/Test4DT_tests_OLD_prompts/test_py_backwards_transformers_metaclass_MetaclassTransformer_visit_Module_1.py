
import ast
from unittest.mock import patch
import pytest
from py_backwards.transformers.metaclass import MetaclassTransformer


def test_edge_case_none():
    with pytest.raises(TypeError):
        MetaclassTransformer().visit_ClassDef(None)
