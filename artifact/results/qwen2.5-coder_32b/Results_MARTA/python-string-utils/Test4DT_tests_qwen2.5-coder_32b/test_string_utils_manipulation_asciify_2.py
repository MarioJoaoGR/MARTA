
import pytest
from string_utils.manipulation import asciify

def test_asciify_whitespace_string():
    assert asciify(' ') == ' '


def test_asciify_accented_word():
    assert asciify('naïve') == 'naive'

def test_asciify_special_characters():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'

def test_asciify_cafe():
    assert asciify('café') == 'cafe'

def test_asciify_empty_string():
    assert asciify('') == ''

def test_asciify_non_string_input():
    with pytest.raises(TypeError):
        asciify(123)