
import pytest
from unittest.mock import patch
from httpie.encoding import smart_encode

@pytest.mark.parametrize("content, encoding, expected", [
    (None, "utf-8", b''),  # Test None input
    ("Hello, world!", None, b'Hello, world!'),  # Test None encoding
    ("Héllö, wørld!", "ascii", b'Hello, w??rld!')  # Existing test case
])
def test_smart_encode(content, encoding, expected):
    with patch('builtins.isinstance', return_value=False):  # Mock isinstance to avoid errors
        assert smart_encode(content, encoding) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_none_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_smart_encode[None-utf-8-] ________________________

content = None, encoding = 'utf-8', expected = b''

    @pytest.mark.parametrize("content, encoding, expected", [
        (None, "utf-8", b''),  # Test None input
        ("Hello, world!", None, b'Hello, world!'),  # Test None encoding
        ("Héllö, wørld!", "ascii", b'Hello, w??rld!')  # Existing test case
    ])
    def test_smart_encode(content, encoding, expected):
        with patch('builtins.isinstance', return_value=False):  # Mock isinstance to avoid errors
>           assert smart_encode(content, encoding) == expected

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_none_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

content = None, encoding = 'utf-8'

    def smart_encode(content: str, encoding: str) -> bytes:
        """Encode `content` using the given `encoding`.
    
        Unicode errors are replaced.
    
        """
>       return content.encode(encoding, 'replace')
E       AttributeError: 'NoneType' object has no attribute 'encode'

httpie/httpie/encoding.py:50: AttributeError
_____________ test_smart_encode[Hello, world!-None-Hello, world!] ______________

content = 'Hello, world!', encoding = None, expected = b'Hello, world!'

    @pytest.mark.parametrize("content, encoding, expected", [
        (None, "utf-8", b''),  # Test None input
        ("Hello, world!", None, b'Hello, world!'),  # Test None encoding
        ("Héllö, wørld!", "ascii", b'Hello, w??rld!')  # Existing test case
    ])
    def test_smart_encode(content, encoding, expected):
        with patch('builtins.isinstance', return_value=False):  # Mock isinstance to avoid errors
>           assert smart_encode(content, encoding) == expected

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_none_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

content = 'Hello, world!', encoding = None

    def smart_encode(content: str, encoding: str) -> bytes:
        """Encode `content` using the given `encoding`.
    
        Unicode errors are replaced.
    
        """
>       return content.encode(encoding, 'replace')
E       TypeError: encode() argument 'encoding' must be str, not None

httpie/httpie/encoding.py:50: TypeError
________ test_smart_encode[H\xe9ll\xf6, w\xf8rld!-ascii-Hello, w??rld!] ________

content = 'Héllö, wørld!', encoding = 'ascii', expected = b'Hello, w??rld!'

    @pytest.mark.parametrize("content, encoding, expected", [
        (None, "utf-8", b''),  # Test None input
        ("Hello, world!", None, b'Hello, world!'),  # Test None encoding
        ("Héllö, wørld!", "ascii", b'Hello, w??rld!')  # Existing test case
    ])
    def test_smart_encode(content, encoding, expected):
        with patch('builtins.isinstance', return_value=False):  # Mock isinstance to avoid errors
>           assert smart_encode(content, encoding) == expected

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_none_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:492: in _call_reprcompare
    custom = util._reprcompare(ops[i], each_obj[i], each_obj[i + 1])
/usr/local/lib/python3.11/site-packages/_pytest/assertion/__init__.py:151: in callbinrepr
    hook_result = ihook.pytest_assertrepr_compare(
/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py:512: in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
/usr/local/lib/python3.11/site-packages/pluggy/_manager.py:120: in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
/usr/local/lib/python3.11/site-packages/_pytest/assertion/__init__.py:192: in pytest_assertrepr_compare
    return util.assertrepr_compare(config=config, op=op, left=left, right=right)
/usr/local/lib/python3.11/site-packages/_pytest/assertion/util.py:174: in assertrepr_compare
    verbose = config.get_verbosity(Config.VERBOSITY_ASSERTIONS)
/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py:1748: in get_verbosity
    assert isinstance(global_level, int)
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='isinstance' id='139961973870992'>
args = (((((((...), <class 'str'>), <class 'str'>), <class 'str'>), <class 'str'>), <class 'str'>), <class 'str'>)
kwargs = {}

    def __call__(self, /, *args, **kwargs):
        # can't use self in-case a function / method we are mocking uses self
        # in the signature
>       self._mock_check_sig(*args, **kwargs)
E       RecursionError: maximum recursion depth exceeded

/usr/local/lib/python3.11/unittest/mock.py:1122: RecursionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_none_input.py::test_smart_encode[None-utf-8-]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_none_input.py::test_smart_encode[Hello, world!-None-Hello, world!]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_encoding_smart_encode_0_test_none_input.py::test_smart_encode[H\xe9ll\xf6, w\xf8rld!-ascii-Hello, w??rld!]
============================== 3 failed in 6.48s ===============================
"""