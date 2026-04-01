
import pytest
from docstring_parser.numpydoc import _KVSection, DocstringMeta

@pytest.fixture
def kvsection():
    return _KVSection()

def test_valid_input(kvsection):
    text = """
    Parameters
    ----------
    param1 : int
        Description of param1.
        
    Returns
    -------
    result : float
        The computed result.
        
    Raises
    ------
    ValueError : When input does not meet certain criteria.
    """
    parsed_sections = list(kvsection.parse(text))
    assert len(parsed_sections) == 3
    
    # Check the first section (Parameters)
    param1_meta = parsed_sections[0]
    assert isinstance(param1_meta, DocstringMeta)
    assert param1_meta.key == 'param1'
    assert param1_meta.type == 'int'
    assert param1_meta.description == 'Description of param1.'
    
    # Check the second section (Returns)
    result_meta = parsed_sections[1]
    assert isinstance(result_meta, DocstringMeta)
    assert result_meta.key == 'result'
    assert result_meta.type == 'float'
    assert result_meta.description == 'The computed result.'
    
    # Check the third section (Raises)
    raises_meta = parsed_sections[2]
    assert isinstance(raises_meta, DocstringMeta)
    assert raises_meta.key == 'ValueError'
    assert raises_meta.type is None
    assert raises_meta.description == 'When input does not meet certain criteria.'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc__KVSection_parse_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__KVSection_parse_0_test_valid_input.py:7:11: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__KVSection_parse_0_test_valid_input.py:7:11: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""