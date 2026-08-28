
import ast
from typing import List, Iterable, Union
import pytest

class StarredUnpackingTransformer(ast.NodeTransformer):
    def _has_starred(self, xs: List[ast.expr]) -> bool:
        for x in xs:
            if isinstance(x, ast.Starred):
                return True
        return False

    def _split_by_starred(self, xs: Iterable[ast.expr]) -> List['Splitted']:
        lists = [[]]  # type: List[Splitted]
        for x in xs:
            if isinstance(x, ast.Starred):
                lists.append([])
            else:
                assert isinstance(lists[-1], list)
                lists[-1].append(x)
        return lists

    def _prepare_lists(self, xs: List['Splitted']) -> Iterable[Union[ast.Call, ast.List]]:
        for x in xs:
            if isinstance(x, ast.Starred):
                yield ast.Call(func=ast.Name(id='list'), args=[x.value], keywords=[])
            elif x:
                yield ast.List(elts=x)

    def _merge_lists(self, xs: List[Union[ast.BinOp, ast.expr]]) -> Union[ast.BinOp, ast.expr]:
        if len(xs) == 1:
            return xs[0]
        result = ast.BinOp(left=xs[0], right=xs[1], op=ast.Add())
        for x in xs[2:]:
            result = ast.BinOp(left=result, right=x, op=ast.Add())
        return result

    def _to_sum_of_lists(self, xs: List[ast.expr]) -> Union[ast.BinOp, ast.expr]:
        splitted = self._split_by_starred(xs)
        prepared = list(self._prepare_lists(splitted))
        return self._merge_lists(prepared)

    def visit_List(self, node: ast.List) -> ast.List:
        if not self._has_starred(node.elts):
            return self.generic_visit(node)  # type: ignore
        self._tree_changed = True
        return self.generic_visit(self._to_sum_of_lists(node.elts))  # type: ignore

    def visit_Call(self, node: ast.Call) -> ast.Call:
        if not self._has_starred(node.args):
            return self.generic_visit(node)  # type: ignore
        self._tree_changed = True
        args = self._to_sum_of_lists(node.args)
        node.args = [ast.Starred(value=args)]
        return self.generic_visit(node)  # type: ignore

# Test cases for _merge_lists method
def test_merge_lists():
    transformer = StarredUnpackingTransformer()
    
    # Test case with a single element list
    xs = [ast.List(elts=[1, 2, 3])]
    assert isinstance(transformer._merge_lists(xs), ast.List)
    assert len(transformer._merge_lists(xs).elts) == 3
    
    # Test case with multiple elements list
    xs = [ast.List(elts=[1, 2]), ast.List(elts=[3, 4])]
    merged = transformer._merge_lists(xs)
    assert isinstance(merged, ast.BinOp)
    assert len(merged.left.elts) == 2
    assert len(merged.right.elts) == 2
    
    # Test case with more than two elements list
    xs = [ast.List(elts=[1]), ast.List(elts=[2]), ast.List(elts=[3])]
    merged = transformer._merge_lists(xs)
    assert isinstance(merged, ast.BinOp)