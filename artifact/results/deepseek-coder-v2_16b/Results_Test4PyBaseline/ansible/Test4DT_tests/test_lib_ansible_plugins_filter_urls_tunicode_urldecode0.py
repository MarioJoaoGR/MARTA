# Module: ansible.plugins.filter.urls
import pytest
from ansible.plugins.filter.urls import unicode_urldecode

def test_unicode_urldecode_python3():
    assert unicode_urldecode("Hello%20World") == 'Hello World'

def test_unicode_urldecode_python2():
    # Assuming Python 2 and a Unicode string for the input
    assert unicode_urldecode(u"Hello%20World") == 'Hello World'
