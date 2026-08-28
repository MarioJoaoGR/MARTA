
import pytest
import ast
from typing import Iterable, Union

# Assuming DictUnpackingTransformer is defined as above
class DictUnpackingTransformer:
    target = 3, 4
    
    def _merge_dicts(self, xs: Iterable[Union[ast.Call, ast.Dict]]) -> ast.Call:
        return ast.Call(func=ast.Name(id='_py_backwards_merge_dicts'), args=[ast.List(elts=list(xs))], keywords=[])

# Create an instance of the transformer
transformer = DictUnpackingTransformer()

def test_merge_dicts():
    # Define dictionaries to merge
    dict_a = ast.Dict(keys=[1, 2, 3], values=[1, 2, 3])
    dict_b = ast.Dict(keys=[4, 5, 6], values=[4, 5, 6])
    
    # Merge the dictionaries
    merged_dicts = transformer._merge_dicts([ast.Dict(keys=[1, 2, 3], values=[1, 2, 3]), ast.Dict(keys=[4, 5, 6], values=[4, 5, 6])])
    
    # Assert the result is a call to _py_backwards_merge_dicts with the correct arguments
    assert isinstance(merged_dicts, ast.Call)
    assert merged_dicts.func.id == '_py_backwards_merge_dicts'
    assert len(merged_dicts.args) == 1
    assert isinstance(merged_dicts.args[0], ast.List)
    assert len(merged_dicts.args[0].elts) == 2