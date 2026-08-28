
import pytest
from ansible.plugins.filter.urls import do_urldecode

# Test cases for Python 3 (ASCII input)
def test_do_urldecode_python3():
    assert do_urldecode("Hello%20World") == "Hello World"

# Test cases for Python 2 (Unicode input)
def test_do_urldecode_python2():
    assert do_urldecode(u"Hello%20World") == "Hello World"
