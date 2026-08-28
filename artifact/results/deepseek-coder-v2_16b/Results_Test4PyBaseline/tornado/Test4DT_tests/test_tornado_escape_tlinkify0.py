
import pytest
from typing import Union, Callable, List
from tornado.escape import linkify

# Test cases for the linkify function

def test_basic_usage():
    result = linkify("Visit our site at https://www.example.com")
    assert '<a href="https://www.example.com">' in result, "Expected a link to be created for the URL"

def test_shorten_urls():
    result = linkify("Check out a very long URL that should be shortened like http://this-is-a-very-long-url.com/with/many/parts")