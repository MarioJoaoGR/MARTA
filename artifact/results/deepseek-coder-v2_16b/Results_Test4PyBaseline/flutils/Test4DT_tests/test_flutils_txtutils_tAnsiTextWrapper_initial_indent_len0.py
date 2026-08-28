
import pytest
from flutils.txtutils import AnsiTextWrapper

# Fixtures for different configurations of the wrapper
@pytest.fixture
def default_wrapper():
    return AnsiTextWrapper()

@pytest.fixture
def custom_wrapper():
    return AnsiTextWrapper(width=50, initial_indent="*** ", subsequent_indent="    ")

@pytest.fixture
def no_indents_expand_tabs():
    return AnsiTextWrapper(initial_indent="", subsequent_indent="", expand_tabs=True)

@pytest.fixture
def custom_tabsize_maxlines():
    return AnsiTextWrapper(tabsize=4, max_lines=10)

@pytest.fixture
def custom_placeholder():
    return AnsiTextWrapper(placeholder="... (continued)")

# Test cases for default parameters
def test_default_wrapper_initialization(default_wrapper):
    assert default_wrapper.width == 70
    assert default_wrapper.initial_indent == ''
    assert default_wrapper.subsequent_indent == ''
    assert default_wrapper.expand_tabs is True
    assert default_wrapper.replace_whitespace is True
    assert default_wrapper.fix_sentence_endings is False
    assert default_wrapper.break_long_words is True
    assert default_wrapper.drop_whitespace is True
    assert default_wrapper.break_on_hyphens is True
    assert default_wrapper.tabsize == 8
    assert default_wrapper.max_lines is None
    assert default_wrapper.placeholder == ' [...]'

# Test cases for custom parameters
def test_custom_wrapper_initialization(custom_wrapper):
    assert custom_wrapper.width == 50
    assert custom_wrapper.initial_indent == "*** "
    assert custom_wrapper.subsequent_indent == "    "
    assert custom_wrapper.expand_tabs is True
    assert custom_wrapper.replace_whitespace is True
    assert custom_wrapper.fix_sentence_endings is False
    assert custom_wrapper.break_long_words is True
    assert custom_wrapper.drop_whitespace is True
    assert custom_wrapper.break_on_hyphens is True
    assert custom_wrapper.tabsize == 8
    assert custom_wrapper.max_lines is None
    assert custom_wrapper.placeholder == ' [...]'

# Test cases for no indents and expand tabs
def test_no_indents_expand_tabs_initialization(no_indents_expand_tabs):
    assert no_indents_expand_tabs.width == 70
    assert no_indents_expand_tabs.initial_indent == ""
    assert no_indents_expand_tabs.subsequent_indent == ""
    assert no_indents_expand_tabs.expand_tabs is True
    assert no_indents_expand_tabs.replace_whitespace is True
    assert no_indents_expand_tabs.fix_sentence_endings is False
    assert no_indents_expand_tabs.break_long_words is True
    assert no_indents_expand_tabs.drop_whitespace is True
    assert no_indents_expand_tabs.break_on_hyphens is True
    assert no_indents_expand_tabs.tabsize == 8
    assert no_indents_expand_tabs.max_lines is None
    assert no_indents_expand_tabs.placeholder == ' [...]'

# Test cases for custom tab size and max lines
def test_custom_tabsize_maxlines_initialization(custom_tabsize_maxlines):
    assert custom_tabsize_maxlines.width == 70
    assert custom_tabsize_maxlines.initial_indent == ''
    assert custom_tabsize_maxlines.subsequent_indent == ''
    assert custom_tabsize_maxlines.expand_tabs is True
    assert custom_tabsize_maxlines.replace_whitespace is True
    assert custom_tabsize_maxlines.fix_sentence_endings is False
    assert custom_tabsize_maxlines.break_long_words is True
    assert custom_tabsize_maxlines.drop_whitespace is True
    assert custom_tabsize_maxlines.break_on_hyphens is True
    assert custom_tabsize_maxlines.tabsize == 4
    assert custom_tabsize_maxlines.max_lines == 10
    assert custom_tabsize_maxlines.placeholder == ' [...]'

# Test cases for custom placeholder
def test_custom_placeholder_initialization(custom_placeholder):
    assert custom_placeholder.width == 70
    assert custom_placeholder.initial_indent == ''
    assert custom_placeholder.subsequent_indent == ''
    assert custom_placeholder.expand_tabs is True
    assert custom_placeholder.replace_whitespace is True
    assert custom_placeholder.fix_sentence_endings is False
    assert custom_placeholder.break_long_words is True
    assert custom_placeholder.drop_whitespace is True
    assert custom_placeholder.break_on_hyphens is True
    assert custom_placeholder.tabsize == 8
    assert custom_placeholder.max_lines is None
    assert custom_placeholder.placeholder == "... (continued)"

# Additional test case for initial_indent_len method
def test_initial_indent_len_method(default_wrapper):
    default_wrapper.initial_indent = "*** \x1b[31m\x1b[1mHello\x1b[0m"