
import pytest
from string_utils.manipulation import strip_html, InvalidInputError

def test_happy_path():
    input_string = 'test: <a href="foo/bar">click here</a>'
    
    # Test with keep_tag_content=False
    result = strip_html(input_string, keep_tag_content=False)
    assert result == 'test: '
    
    # Test with keep_tag_content=True
    result = strip_html(input_string, keep_tag_content=True)
    assert result == 'test: click here'

def test_edge_cases():
    # Test with empty string
    result = strip_html('')
    assert result == ''
    
    # Test with None (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        strip_html(None)
    
    # Test with no HTML tags
    result = strip_html('No HTML here')
    assert result == 'No HTML here'
    
    # Test with empty HTML tag
    result = strip_html('<p></p>')
    assert result == ''

def test_invalid_inputs():
    # Test with integer input (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        strip_html(12345)
    
    # Test with list input (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        strip_html([1, 2, 3])
    
    # Test with dictionary input (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        strip_html({'key': 'value'})
