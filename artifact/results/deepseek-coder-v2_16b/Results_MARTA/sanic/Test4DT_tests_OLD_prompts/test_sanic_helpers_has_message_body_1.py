
import pytest
from sanic.helpers import has_message_body

def test_has_message_body_valid():
    assert has_message_body(200) == True  # Status 200 should have a message body

def test_has_message_body_invalid_1xx():
    assert has_message_body(105) == False  # Status 105 is in the range 100 <= status < 200

def test_has_message_body_invalid_204():
    assert has_message_body(204) == False  # Status 204 should not have a message body

def test_has_message_body_invalid_304():
    assert has_message_body(304) == False  # Status 304 should not have a message body
