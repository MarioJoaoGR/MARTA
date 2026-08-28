
import pytest
from sanic import Sanic
from sanic.compat import Header
from typing import Dict, Union, Optional
from unittest.mock import patch

def parse_forwarded(headers, config) -> Optional[Dict[str, Union[int, str]]]:
    """Parse RFC 7239 Forwarded headers according to the specified configuration.

    This function processes the "Forwarded" HTTP header from a dictionary of request headers and a configuration object. It checks if the `by` or `secret` value matches the configured `FORWARDED_SECRET`. If they match, it parses the header content in reverse order for key-value pairs and returns them normalized according to specific rules.

    Parameters:
        headers (MultiDict): A dictionary-like object containing HTTP request headers, including the "Forwarded" header.
        config (Config): An object that contains configuration settings, specifically `FORWARDED_SECRET`.

    Returns:
        Optional[Dict[str, Union[int, str]]]: A dictionary with normalized key-value pairs from the parsed "Forwarded" header if a match is found; otherwise, returns None. The values are either integers or strings after normalization.

    Examples:
        >>> parse_forwarded({'forwarded': ['by=Example Corp', 'host=example.com']}, Config(FORWARDED_SECRET='secret'))
        {'by': 'Example Corp', 'host': 'example.com'}
        
        This example shows how the function parses a "Forwarded" header with two entries and returns them as a dictionary, using the configured secret for validation.
    """
    获取请求头中的活动代理信息，按照Sanic配置规范进行规范化处理。

# - `for` 和 `by` IPv6地址会被括号括起来
# - `port` 仅从端口头中设置（不从host中获取）
# - `path` 是url解码后的结果

可能还会从新的Forwarded头中获取额外的值。

:param headers: HTTP请求头，包含代理信息
:type headers: Dict[str, str]
:param config: Sanic应用程序配置
:type config: Config
:return: 转发的地址信息
:rtype: Optional[Dict[str, str]]
```

```python
import pytest
from sanic import Sanic
from sanic.compat import Header
from typing import Dict, Union, Optional

@pytest.mark.asyncio
def test_parse_forwarded_basic():
    app = Sanic("MyApp")
    headers = {'forwarded': ['by=Example Corp', 'host=example.com']}
    config = Config(FORWARDED_SECRET='secret')
    expected_result = {'by': 'Example Corp', 'host': 'example.com'}
    
    result = parse_forwarded(Header(headers), config)
    
    assert result == expected_result

@pytest.mark.asyncio
def test_parse_forwarded_no_match():
    app = Sanic("MyApp")
    headers = {'forwarded': ['by=Example Corp', 'host=example.com']}
    config = Config(FORWARDED_SECRET='wrong-secret')
    
    result = parse_forwarded(Header(headers), config)
    
    assert result is None

@pytest.mark.asyncio
def test_parse_forwarded_no_header():
    app = Sanic("MyApp")
    headers = {}
    config = Config(FORWARDED_SECRET='secret')
    
    result = parse_forwarded(Header(headers), config)
    
    assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid character '，' (U+FF0C) (line 26, col 18)
    获取请求头中的活动代理信息，按照Sanic配置规范进行规范化处理。
"""