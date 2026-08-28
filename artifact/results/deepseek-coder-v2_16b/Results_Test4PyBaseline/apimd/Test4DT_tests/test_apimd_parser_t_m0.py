# Module: apimd.parser
# test_parser.py
from apimd.parser import _m

def test_combine_two_module_names():
    assert _m('os', 'path') == 'os.path'

def test_include_empty_string_and_non_empty_string():
    assert _m('math', '', 'random') == 'math.random'

def test_no_arguments_provided():
    assert _m() == ''
