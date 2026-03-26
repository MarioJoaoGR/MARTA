
# Module: string_utils.manipulation
# test_string_utils.py
from string_utils.manipulation import strip_margin, InvalidInputError

def test_strip_margin_basic():
    input_string = '''
        line 1
        line 2
        line 3
    '''
    expected_output = '''
line 1
line 2
line 3
'''
    assert strip_margin(input_string) == expected_output, "Test failed for basic multi-line input."

def test_strip_margin_single_quoted():
    input_string = """
        line 1
        line 2
        line 3
    """
    expected_output = '''
line 1
line 2
line 3
'''
    assert strip_margin(input_string) == expected_output, "Test failed for single-quoted multi-line input."

def test_strip_margin_empty():
    input_string = ''
    expected_output = ''
    assert strip_margin(input_string) == expected_output, "Test failed for empty string."

def test_strip_margin_complex():
    input_string = '''
        line 1
          indented line 2
        line 3
    '''
    expected_output = '''
line 1
indented line 2
line 3
'''