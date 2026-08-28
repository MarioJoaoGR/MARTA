
# Module: ansible.module_utils.common.text.formatters
from ansible.module_utils.common.text.formatters import lenient_lowercase

def test_lenient_lowercase_with_none():
    assert lenient_lowercase([None, 'Hello', None]) == [None, 'hello', None]

def test_lenient_lowercase_with_empty_string():
    assert lenient_lowercase(['Hello', '', 'World']) == ['hello', '', 'world']

def test_lenient_lowercase_with_special_chars():
    assert lenient_lowercase(['Hello!', '@world', '#python']) == ['hello!', '@world', '#python']

def test_lenient_lowercase_all_caps():
    assert lenient_lowercase(['HELLO', 'WORLD', 123]) == ['hello', 'world', 123]

def test_lenient_lowercase_mixed_case():
    assert lenient_lowercase(['Mixed', 'CASE', 456]) == ['mixed', 'case', 456]

def test_lenient_lowercase_with_unicode():
    assert lenient_lowercase(['Héllo', 'Wôrld', 'Pythön']) == ['héllo', 'wôrld', 'pythön']
