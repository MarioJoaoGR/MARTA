# Module: apimd.parser
import pytest
from apimd.parser import _m

def test_module_path_joining():
    assert _m('package', 'submodule', 'function') == 'package.submodule.function'

def test_handling_empty_strings():
    assert _m('main', '', 'utils') == 'main.utils'
    assert _m('', 'core', '') == 'core'
    assert _m('', '', 'io') == 'io'

def test_single_module_name():
    assert _m('standalone_module') == 'standalone_module'

def test_no_parts_provided():
    assert _m('', '', '') == ''
    assert _m() == ''

def test_multiple_consecutive_empty_strings():
    assert _m('start', '', '', 'end') == 'start.end'
    assert _m('first', '', 'second', '', 'third') == 'first.second.third'

def test_mixed_empty_and_non_empty_strings():
    assert _m('', 'a', '', 'b', '', 'c', '') == 'a.b.c'
    assert _m('x', '', '', '', 'y', '', 'z') == 'x.y.z'

def test_all_parts_non_empty():
    assert _m('alpha', 'beta', 'gamma') == 'alpha.beta.gamma'
