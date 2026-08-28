
import pytest
import re
from ansible.plugins.filter.core import to_text

def regex_search(value, regex, *args, **kwargs):
    value = to_text(value, errors='surrogate_or_strict', nonstring='simplerepr')
    groups = list()
    for arg in args:
        if arg.startswith('\\g'):
            match = re.match(r'\\g<(\S+)>', arg).group(1)
            groups.append(match)
        elif arg.startswith('\\'):
            match = int(re.match(r'\\(\d+)', arg).group(1))
            groups.append(match)
        else:
            raise ValueError('Unknown argument')
    flags = 0
    if kwargs.get('ignorecase'):
        flags |= re.I
    if kwargs.get('multiline'):
        flags |= re.M
    match = re.search(regex, value, flags)
    if match:
        if not groups:
            return match.group()
        else:
            items = list()
            for item in groups:
                items.append(match.group(item))
            return items

# Test cases
def test_valid_input_basic():
    value = 'hello world'
    regex = r'world'
    result = regex_search(value, regex)
    assert result == 'world'

def test_valid_input_with_backreference_by_index():
    value = 'abc123def'
    regex = r'(\d+)'
    args = [1]
    result = regex_search(value, regex, *args)
    assert result == ['123']

def test_valid_input_with_backreference_by_name():
    value = 'abc123def'
    regex = r'(?P<num>\d+)'
    args = ['num']
    result = regex_search(value, regex, *args)
    assert result == ['123']

def test_invalid_input_none():
    value = None
    regex = 'some_regex'
    with pytest.raises(TypeError):
        regex_search(value, regex)

def test_invalid_input_empty_string():
    value = ''
    regex = r'\w+'
    result = regex_search(value, regex)
    assert result is None

def test_error_handling_unknown_arg():
    value = 'some_text'
    regex = r'pattern'
    args = ['unknown']
    with pytest.raises(ValueError):
        regex_search(value, regex, *args)

def test_case_insensitive_search():
    value = 'Hello World'
    regex = r'world'
    kwargs = {'ignorecase': True}
    result = regex_search(value, regex, **kwargs)
    assert result == 'World'

def test_multiline_search():
    value = 'line1\nline2'
    regex = r'line\d'
    kwargs = {'multiline': True}
    result = regex_search(value, regex, **kwargs)
    assert result == ['line1', 'line2']
