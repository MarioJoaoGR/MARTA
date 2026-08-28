
import pytest
from string_utils import asciify

def test_asciify_with_non_string_input():
    with pytest.raises(TypeError):
        asciify(None)

def test_asciify_with_integer_input():
    with pytest.raises(TypeError):
        asciify(12345)

def test_asciify_with_float_input():
    with pytest.raises(TypeError):
        asciify(123.456)

def test_asciify_with_list_input():
    with pytest.raises(TypeError):
        asciify(['a', 'b', 'c'])

def test_asciify_with_tuple_input():
    with pytest.raises(TypeError):
        asciify(('a', 'b', 'c'))

def test_asciify_with_dict_input():
    with pytest.raises(TypeError):
        asciify({'key': 'value'})

def test_asciify_with_set_input():
    with pytest.raises(TypeError):
        asciify({'a', 'b', 'c'})

def test_asciify_with_bytes_input():
    with pytest.raises(TypeError):
        asciify(b'bytes')

def test_asciify_with_bytearray_input():
    with pytest.raises(TypeError):
        asciify(bytearray(b'bytearray'))

def test_asciify_with_custom_object_input():
    class CustomObject:
        pass
    with pytest.raises(TypeError):
        asciify(CustomObject())

def test_asciify_with_empty_string():
    assert asciify('') == ''

def test_asciify_with_whitespace_string():
    assert asciify('   ') == '   '
    assert asciify('\t\n') == '\t\n'

def test_asciify_with_mixed_case_and_special_chars():
    assert asciify('Héllo Wörld! 123') == 'Hello World! 123'

def test_asciify_with_accented_chars():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
