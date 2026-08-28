
import pytest
from sanic import Sanic
from sanic.cookies import _quote


def test_none_input():
    assert _quote(None) is None

def test_legal_key():
    legal_key = "hello"
    assert _quote(legal_key) == legal_key