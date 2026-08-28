
import pytest
from flutils.txtutils import AnsiTextWrapper

# Test 1: Default initialization parameters
def test_default_initialization():
    wrapper = AnsiTextWrapper()
    assert wrapper.width == 70
    assert wrapper.initial_indent == ''
    assert wrapper.subsequent_indent == ''
    assert wrapper.expand_tabs is True
    assert wrapper.replace_whitespace is True
    assert wrapper.fix_sentence_endings is False
    assert wrapper.break_long_words is True
    assert wrapper.drop_whitespace is True
    assert wrapper.break_on_hyphens is True
    assert wrapper.tabsize == 8
    assert wrapper.max_lines is None
    assert wrapper.placeholder == ' [...]'

# Test 2: Custom initialization parameters
def test_custom_initialization():
    wrapper = AnsiTextWrapper(width=40, initial_indent="*** ", subsequent_indent="--- ")
    assert wrapper.width == 40
    assert wrapper.initial_indent == "*** "
    assert wrapper.subsequent_indent == "--- "
    assert wrapper.expand_tabs is True
    assert wrapper.replace_whitespace is True
    assert wrapper.fix_sentence_endings is False
    assert wrapper.break_long_words is True
    assert wrapper.drop_whitespace is True
    assert wrapper.break_on_hyphens is True
    assert wrapper.tabsize == 8
    assert wrapper.max_lines is None
    assert wrapper.placeholder == ' [...]'

# Test 3: Setting initial indent via method

# Test 4: Custom width and placeholder
def test_custom_width_and_placeholder():
    wrapper = AnsiTextWrapper(width=30, placeholder=" END")
    assert wrapper.width == 30
    assert wrapper.placeholder == " END"

# Test 5: Setting subsequent indent via method