# Module: sanic.helpers
import pytest
from sanic.helpers import has_message_body

def test_has_message_body_with_status_204():
    assert not has_message_body(204), "Expected False for status code 204"

def test_has_message_body_with_status_205():
    assert has_message_body(205), "Expected True for status code 205"

def test_has_message_body_with_status_100():
    assert not has_message_body(100), "Expected False for status code 100"

def test_has_message_body_with_status_199():
    assert not has_message_body(199), "Expected False for status code 199 (just below the informational range)"

def test_has_message_body_with_status_304():
    assert not has_message_body(304), "Expected False for status code 304"

def test_has_message_body_with_invalid_input():
    with pytest.raises(TypeError):
        has_message_body("invalid input")
