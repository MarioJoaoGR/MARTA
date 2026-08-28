
import pytest
from string_utils.manipulation import asciify


def test_asciify_naive():
    assert asciify('naïve') == 'naive'

def test_asciify_accents():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'

def test_asciify_cafe():
    assert asciify('café') == 'cafe'

def test_asciify_empty_string():
    assert asciify('') == ''

def test_asciify_ascii_only():
    assert asciify('ascii only') == 'ascii only'

def test_asciify_special_characters():
    assert asciify('!@#$%^&*()_+') == '!@#$%^&*()_+'
