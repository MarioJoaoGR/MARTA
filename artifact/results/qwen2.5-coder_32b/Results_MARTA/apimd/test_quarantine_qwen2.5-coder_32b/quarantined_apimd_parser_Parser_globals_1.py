
import pytest
from apimd.parser import Parser
from ast import AnnAssign, Assign, Name, Subscript, Tuple, Index, Constant, List

def _m(root: str, name: str) -> str:
    return f"{root}.{name}"





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
____________________________ test_valid_type_alias _____________________________

    def test_valid_type_alias():
        parser = Parser(root='example_package')
    
        ann_assign_node = AnnAssign(
            target=Name(id='TypeAlias'),
            annotation=Subscript(
                value=Name(id='Dict'),
                slice=Tuple(elts=[
                    Index(value=Constant(value=str)),
                    Index(value=Constant(value=int))
                ])
            ),
            value=Constant(value={})
        )
    
        parser.globals('example_package', ann_assign_node)
    
        assert parser.alias['example_package.TypeAlias'] == '{}'
>       assert parser.root.get('example_package.TypeAlias') is None
E       AttributeError: 'str' object has no attribute 'get'

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py:27: AttributeError
_____________________________ test_valid_constant ______________________________

    def test_valid_constant():
        parser = Parser(root='example_package')
    
        assign_node = Assign(
            targets=[Name(id='CONSTANT')],
            value=Constant(value=10)
        )
    
>       parser.globals('example_package', assign_node)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py:37: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root='example_package', alias={'example_package.CONSTANT': '10'}, const={})
root = 'example_package', node = <ast.Assign object at 0x7f2345aff4f0>

    def globals(self, root: str, node: _G) -> None:
        """Set up globals:
    
        + Type alias
        + Constants
        + `__all__` filter
        """
        if (
            isinstance(node, AnnAssign)
            and isinstance(node.target, Name)
            and node.value is not None
        ):
            left = node.target
            expression = unparse(node.value)
            ann = self.resolve(root, node.annotation)
        elif (
            isinstance(node, Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], Name)
        ):
            left = node.targets[0]
            expression = unparse(node.value)
            if node.type_comment is None:
                ann = const_type(node.value)
            else:
                ann = node.type_comment
        else:
            return
        name = _m(root, left.id)
        self.alias[name] = expression
        if left.id.isupper():
>           self.root[name] = root
E           TypeError: 'str' object does not support item assignment

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:372: TypeError
___________________________ test_invalid_type_alias ____________________________

    def test_invalid_type_alias():
        parser = Parser(root='example_package')
    
        ann_assign_node = AnnAssign(
            target=Name(id='InvalidType'),
            annotation=None,
            value=Constant(value={})
        )
    
>       parser.globals('example_package', ann_assign_node)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py:51: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:355: in globals
    ann = self.resolve(root, node.annotation)
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:516: in resolve
    return unparse(r.generic_visit(r.visit(node)))
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:418: in visit
    return visitor(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:489: in generic_visit
    for field, old_value in iter_fields(node):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = None

    def iter_fields(node):
        """
        Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
        that is present on *node*.
        """
>       for field in node._fields:
E       AttributeError: 'NoneType' object has no attribute '_fields'

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:260: AttributeError
__________________________ test_valid_all_assignment ___________________________

    def test_valid_all_assignment():
        parser = Parser(root='example_package')
    
        assign_node = Assign(
            targets=[Name(id='__all__')],
            value=Tuple(elts=[
                Constant(value='module1'),
                Constant(value='module2')
            ])
        )
    
>       parser.globals('example_package', assign_node)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py:67: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root='example_package', alias={'example_package.__all__': "('module1', 'module2')"}, const={})
root = 'example_package', node = <ast.Assign object at 0x7f23459ff7c0>

    def globals(self, root: str, node: _G) -> None:
        """Set up globals:
    
        + Type alias
        + Constants
        + `__all__` filter
        """
        if (
            isinstance(node, AnnAssign)
            and isinstance(node.target, Name)
            and node.value is not None
        ):
            left = node.target
            expression = unparse(node.value)
            ann = self.resolve(root, node.annotation)
        elif (
            isinstance(node, Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], Name)
        ):
            left = node.targets[0]
            expression = unparse(node.value)
            if node.type_comment is None:
                ann = const_type(node.value)
            else:
                ann = node.type_comment
        else:
            return
        name = _m(root, left.id)
        self.alias[name] = expression
        if left.id.isupper():
            self.root[name] = root
            if self.const.get(name, ANY) == ANY:
                self.const[name] = ann
        if left.id != '__all__' or not isinstance(node.value, (Tuple, List)):
            return
        for e in node.value.elts:
            if isinstance(e, Constant) and isinstance(e.value, str):
>               self.imp[root].add(_m(root, e.value))
E               KeyError: 'example_package'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:379: KeyError
_____________________ test_valid_all_assignment_with_list ______________________

    def test_valid_all_assignment_with_list():
        parser = Parser(root='example_package')
    
        assign_node = Assign(
            targets=[Name(id='__all__')],
            value=List(elts=[
                Constant(value='module1'),
                Constant(value='module2')
            ])
        )
    
>       parser.globals('example_package', assign_node)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py:83: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root='example_package', alias={'example_package.__all__': "['module1', 'module2']"}, const={})
root = 'example_package', node = <ast.Assign object at 0x7f2345783ac0>

    def globals(self, root: str, node: _G) -> None:
        """Set up globals:
    
        + Type alias
        + Constants
        + `__all__` filter
        """
        if (
            isinstance(node, AnnAssign)
            and isinstance(node.target, Name)
            and node.value is not None
        ):
            left = node.target
            expression = unparse(node.value)
            ann = self.resolve(root, node.annotation)
        elif (
            isinstance(node, Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], Name)
        ):
            left = node.targets[0]
            expression = unparse(node.value)
            if node.type_comment is None:
                ann = const_type(node.value)
            else:
                ann = node.type_comment
        else:
            return
        name = _m(root, left.id)
        self.alias[name] = expression
        if left.id.isupper():
            self.root[name] = root
            if self.const.get(name, ANY) == ANY:
                self.const[name] = ann
        if left.id != '__all__' or not isinstance(node.value, (Tuple, List)):
            return
        for e in node.value.elts:
            if isinstance(e, Constant) and isinstance(e.value, str):
>               self.imp[root].add(_m(root, e.value))
E               KeyError: 'example_package'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:379: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py::test_valid_type_alias
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py::test_valid_constant
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py::test_invalid_type_alias
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py::test_valid_all_assignment
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_globals_1.py::test_valid_all_assignment_with_list
============================== 5 failed in 0.17s ===============================
"""