
from isort._vendored.tomli._parser import parse_multiline_str, Pos
from typing import Tuple

def test_valid_basic_multiline_string():
    # Test a valid basic multiline string
    src = '"""this is a test"""'
    pos = Pos(0)
    literal = False
    
    expected_pos = len('"""this is a test"""')
    expected_result = "this is a test"
    
    result_pos, result_str = parse_multiline_str(src, pos, literal=literal)
    
    assert result_pos == expected_pos
    assert result_str == expected_result
