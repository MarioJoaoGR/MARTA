
import ast
from ast import Subscript, Name, Load, Tuple, BitOr, BinOp, Constant
from apimd.parser import Resolver




def test_non_typing_subscript():
    resolver = Resolver(root='my_project', alias={'np': 'numpy', 'pd': 'pandas'}, self_ty='MyClass')
    subscript_node = Subscript(
        value=Name('CustomType', Load()),
        slice=Name('int', Load()),
        ctx=Load()
    )
    transformed_node = resolver.visit_Subscript(subscript_node)
    assert ast.dump(transformed_node) == ast.dump(subscript_node)

