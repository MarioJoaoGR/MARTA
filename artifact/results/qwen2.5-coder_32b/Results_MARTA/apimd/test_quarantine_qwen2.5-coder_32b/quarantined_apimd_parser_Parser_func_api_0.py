
import pytest
from apimd.parser import Parser
import ast






"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 6 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        parser = Parser()
        args_node = ast.arguments(
            posonlyargs=[],
            args=[
                ast.arg(arg='self'),
                ast.arg(arg='param1')
            ],
            defaults=[]
        )
        returns_node = ast.Name(id='int')
>       parser.func_api(root='my_project', name='example_func', node=args_node, returns=returns_node, has_self=True, cls_method=False)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'example_func'
node = <ast.arguments object at 0x7f53b121c6d0>
returns = <ast.Name object at 0x7f53b121d660>

    def func_api(self, root: str, name: str, node: arguments,
                 returns: Optional[expr], *,
                 has_self: bool, cls_method: bool) -> None:
        """Create function API."""
        args = []
        default: list[Optional[expr]] = []
        if node.posonlyargs:
            args.extend(node.posonlyargs)
            args.append(arg('/', None))
            default.extend([None] * len(node.posonlyargs))
        args.extend(node.args)
        default.extend([None] * (len(node.args) - len(node.defaults)))
        default.extend(node.defaults)
        if node.vararg is not None:
            args.append(arg('*' + node.vararg.arg, node.vararg.annotation))
>       elif node.kwonlyargs:
E       AttributeError: 'arguments' object has no attribute 'kwonlyargs'. Did you mean: 'posonlyargs'?

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:433: AttributeError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        parser = Parser()
        args_node = ast.arguments(posonlyargs=[], args=[], defaults=[])
        returns_node = None
>       parser.func_api(root='my_project', name='no_args_no_return', node=args_node, returns=returns_node, has_self=False, cls_method=False)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'no_args_no_return'
node = <ast.arguments object at 0x7f53b1208310>, returns = None

    def func_api(self, root: str, name: str, node: arguments,
                 returns: Optional[expr], *,
                 has_self: bool, cls_method: bool) -> None:
        """Create function API."""
        args = []
        default: list[Optional[expr]] = []
        if node.posonlyargs:
            args.extend(node.posonlyargs)
            args.append(arg('/', None))
            default.extend([None] * len(node.posonlyargs))
        args.extend(node.args)
        default.extend([None] * (len(node.args) - len(node.defaults)))
        default.extend(node.defaults)
        if node.vararg is not None:
            args.append(arg('*' + node.vararg.arg, node.vararg.annotation))
>       elif node.kwonlyargs:
E       AttributeError: 'arguments' object has no attribute 'kwonlyargs'. Did you mean: 'posonlyargs'?

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:433: AttributeError
____________________________ test_keyword_only_args ____________________________

    def test_keyword_only_args():
        parser = Parser()
        args_node = ast.arguments(
            posonlyargs=[],
            args=[],
            kwonlyargs=[
                ast.arg(arg='param1'),
                ast.arg(arg='param2')
            ],
            kw_defaults=[
                ast.Constant(value=20),
                ast.Name(id='None')
            ]
        )
        returns_node = ast.Name(id='bool')
>       parser.func_api(root='my_project', name='keyword_only_args_with_return', node=args_node, returns=returns_node, has_self=False, cls_method=False)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'keyword_only_args_with_return'
node = <ast.arguments object at 0x7f53b10ebb80>
returns = <ast.Name object at 0x7f53b10ebb20>

    def func_api(self, root: str, name: str, node: arguments,
                 returns: Optional[expr], *,
                 has_self: bool, cls_method: bool) -> None:
        """Create function API."""
        args = []
        default: list[Optional[expr]] = []
        if node.posonlyargs:
            args.extend(node.posonlyargs)
            args.append(arg('/', None))
            default.extend([None] * len(node.posonlyargs))
        args.extend(node.args)
>       default.extend([None] * (len(node.args) - len(node.defaults)))
E       AttributeError: 'arguments' object has no attribute 'defaults'. Did you mean: 'kw_defaults'?

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:429: AttributeError
___________________________ test_var_positional_args ___________________________

    def test_var_positional_args():
        parser = Parser()
        args_node = ast.arguments(
            posonlyargs=[],
            args=[],
            vararg=ast.arg(arg='args')
        )
        returns_node = None
>       parser.func_api(root='my_project', name='var_positional_args', node=args_node, returns=returns_node, has_self=False, cls_method=False)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'var_positional_args'
node = <ast.arguments object at 0x7f53b1208be0>, returns = None

    def func_api(self, root: str, name: str, node: arguments,
                 returns: Optional[expr], *,
                 has_self: bool, cls_method: bool) -> None:
        """Create function API."""
        args = []
        default: list[Optional[expr]] = []
        if node.posonlyargs:
            args.extend(node.posonlyargs)
            args.append(arg('/', None))
            default.extend([None] * len(node.posonlyargs))
        args.extend(node.args)
>       default.extend([None] * (len(node.args) - len(node.defaults)))
E       AttributeError: 'arguments' object has no attribute 'defaults'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:429: AttributeError
____________________________ test_var_keyword_args _____________________________

    def test_var_keyword_args():
        parser = Parser()
        args_node = ast.arguments(
            posonlyargs=[],
            args=[],
            kwarg=ast.arg(arg='kwargs')
        )
        returns_node = None
>       parser.func_api(root='my_project', name='var_keyword_args', node=args_node, returns=returns_node, has_self=False, cls_method=False)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py:64: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'var_keyword_args'
node = <ast.arguments object at 0x7f53b124c580>, returns = None

    def func_api(self, root: str, name: str, node: arguments,
                 returns: Optional[expr], *,
                 has_self: bool, cls_method: bool) -> None:
        """Create function API."""
        args = []
        default: list[Optional[expr]] = []
        if node.posonlyargs:
            args.extend(node.posonlyargs)
            args.append(arg('/', None))
            default.extend([None] * len(node.posonlyargs))
        args.extend(node.args)
>       default.extend([None] * (len(node.args) - len(node.defaults)))
E       AttributeError: 'arguments' object has no attribute 'defaults'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:429: AttributeError
____________________________ test_all_types_of_args ____________________________

    def test_all_types_of_args():
        parser = Parser()
        args_node = ast.arguments(
            posonlyargs=[
                ast.arg(arg='pos1'),
                ast.arg(arg='pos2')
            ],
            args=[
                ast.arg(arg='param1'),
                ast.arg(arg='param2')
            ],
            defaults=[
                ast.Constant(value=30)
            ],
            kwonlyargs=[
                ast.arg(arg='kwarg1'),
                ast.arg(arg='kwarg2')
            ],
            kw_defaults=[
                ast.Name(id='None'),
                ast.Constant(value=True)
            ],
            vararg=ast.arg(arg='var_args'),
            kwarg=ast.arg(arg='var_kwargs')
        )
        returns_node = ast.Subscript(
            value=ast.Name(id='List'),
            slice=ast.Index(ast.Name(id='str'))
        )
>       parser.func_api(root='my_project', name='all_types_of_args', node=args_node, returns=returns_node, has_self=False, cls_method=False)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'all_types_of_args'
node = <ast.arguments object at 0x7f53b10d0a30>
returns = <ast.Subscript object at 0x7f53b10d1030>

    def func_api(self, root: str, name: str, node: arguments,
                 returns: Optional[expr], *,
                 has_self: bool, cls_method: bool) -> None:
        """Create function API."""
        args = []
        default: list[Optional[expr]] = []
        if node.posonlyargs:
            args.extend(node.posonlyargs)
            args.append(arg('/', None))
            default.extend([None] * len(node.posonlyargs))
        args.extend(node.args)
        default.extend([None] * (len(node.args) - len(node.defaults)))
        default.extend(node.defaults)
        if node.vararg is not None:
            args.append(arg('*' + node.vararg.arg, node.vararg.annotation))
        elif node.kwonlyargs:
            args.append(arg('*', None))
        default.append(None)
        args.extend(node.kwonlyargs)
        default.extend([None] * (len(node.kwonlyargs) - len(node.kw_defaults)))
        default.extend(node.kw_defaults)
        if node.kwarg is not None:
            args.append(arg('**' + node.kwarg.arg, node.kwarg.annotation))
            default.append(None)
        args.append(arg('return', returns))
        default.append(None)
        ann = map(code, self.func_ann(root, args, has_self=has_self,
                                      cls_method=cls_method))
        has_default = all(d is None for d in default)
>       self.doc[name] += table(
            *(a.arg for a in args),
            items=[ann] if has_default else [ann, _defaults(default)])
E       KeyError: 'all_types_of_args'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:447: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py::test_keyword_only_args
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py::test_var_positional_args
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py::test_var_keyword_args
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_api_0.py::test_all_types_of_args
============================== 6 failed in 0.14s ===============================
"""