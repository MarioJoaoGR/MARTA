
import pytest
from apimd.parser import Parser

def test__is_immediate_family_direct_import():
    p = Parser()
    n1 = 'module_name'
    n2 = 'module_name.sub_module'
    p.root[n2] = n1
    assert p._Parser__is_immediate_family(n1, n2)

def test__is_immediate_family_indirect_import():
    p = Parser()
    n1 = 'module_name'
    n2 = 'module_name.sub_module.indirect_sub_module'
    p.root[n2] = n1