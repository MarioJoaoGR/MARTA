
import pytest
from apimd.parser import Parser
from ast import AnnAssign, Assign, Name, Subscript, Index, Constant, Expr

def test_valid_annassign():
    parser = Parser()
    node = AnnAssign(
        target=Name(id='TYPE_ALIAS'),
        annotation=Subscript(value=Name(id='List'), slice=Index(value=Name(id='int'))),
        value=Constant(value=[1, 2, 3])
    )
    parser.globals('module', node)
    assert parser.alias['module.TYPE_ALIAS'] == '[1, 2, 3]'
    assert parser.root['module.TYPE_ALIAS'] == 'module'

def test_valid_assign():
    parser = Parser()
    node = Assign(
        targets=[Name(id='CONSTANT')],
        value=Constant(value=42),
        type_comment='int'
    )
    parser.globals('module', node)
    assert parser.alias['module.CONSTANT'] == '42'
    assert parser.root['module.CONSTANT'] == 'module'

def test_invalid_node_type():
    parser = Parser()
    node = Expr(value=Constant(value='This is a string'))
    parser.globals('module', node)
    assert not parser.alias
    assert not parser.root
