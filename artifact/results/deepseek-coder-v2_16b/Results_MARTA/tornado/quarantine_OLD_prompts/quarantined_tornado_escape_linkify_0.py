
import re
import pytest
from typing import Union, List, Callable
from unittest.mock import patch
from tornado.escape import xhtml_escape

# Define the regular expression for URLs
_URL_RE = re.compile(
    r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,15})/[\S]*)",
    re.IGNORECASE,
)

def linkify(
    text: Union[str, bytes],
    shorten: bool = False,
    extra_params: Union[str, Callable[[str], str]] = "",
    require_protocol: bool = False,
    permitted_protocols: List[str] = ["http", "https"],
) -> str:
    """Converts plain text into HTML with links."""
    if extra_params and not callable(extra_params):
        extra_params = " " + extra_params.strip()

    def make_link(m: re.Match) -> str:
        url = m.group(1)
        proto = m.group(2)
        if require_protocol and not proto:
            return url  # not protocol, no linkify

        if proto and proto not in permitted_protocols:
            return url  # bad protocol, no linkify

        href = url
        if not proto:
            href = "http://" + url  # no proto specified, use http

        if callable(extra_params):
            params = " " + extra_params(href).strip()
        else:
            params = extra_params

        # clip long urls. max_len is just an approximation
        max_len = 30
        if shorten and len(url) > max_len:
            before_clip = url
            proto_len = len(proto) + 1 + (m.group(3) or "").find("/")  # +1 for :
            parts = url[proto_len:].split("/")
            if len(parts) > 1:
                # Grab the whole host part plus the first bit of the path
                # The path is usually not that interesting once shortened
                # (no more slug, etc), so it really just provides a little
                # extra indication of shortening.
                url = url[:proto_len] + parts[0] + "/" + parts[1][:8].split("?")[0].split(".")[0]

            if len(url) > max_len * 1.5:  # still too long
                url = url[:max_len]

            if url != before_clip:
                amp = url.rfind("&")
                # avoid splitting html char entities
                if amp > max_len - 5:
                    url = url[:amp]
                url += "..."

                if len(url) >= len(before_clip):
                    url = before_clip
                else:
                    # full url is visible on mouse-over (for those who don't
                    # have a status bar, such as Safari by default)
                    params += ' title="%s"' % href

        return u'<a href="%s"%s>%s</a>' % (href, params, url)

    text = xhtml_escape(text)  # First HTML-escape so that our strings are all safe.
    return _URL_RE.sub(make_link, text)

# Test cases
@pytest.mark.parametrize("text, expected", [
    ("Hello http://tornadoweb.org!", "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!")
])
def test_valid_input(text, expected):
    assert linkify(text) == expected

@pytest.mark.parametrize("text", [None])
def test_none_input(text):
    assert linkify(text) is None

@pytest.mark.parametrize("text", ["Visit our site at www.example.com"])
def test_invalid_protocol(text):
    assert linkify(text, require_protocol=True) == text
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_linkify_0.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_ test_valid_input[Hello http://tornadoweb.org!-Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!] _

text = 'Hello http://tornadoweb.org!'
expected = 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'

    @pytest.mark.parametrize("text, expected", [
        ("Hello http://tornadoweb.org!", "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!")
    ])
    def test_valid_input(text, expected):
>       assert linkify(text) == expected
E       assert 'Hello http://tornadoweb.org!' == 'Hello <a hre...oweb.org</a>!'
E         
E         - Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!
E         + Hello http://tornadoweb.org!

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_linkify_0.py:83: AssertionError
____________________________ test_none_input[None] _____________________________

text = None

    @pytest.mark.parametrize("text", [None])
    def test_none_input(text):
>       assert linkify(text) is None

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_linkify_0.py:87: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_linkify_0.py:75: in linkify
    text = xhtml_escape(text)  # First HTML-escape so that our strings are all safe.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def xhtml_escape(value: Union[str, bytes]) -> str:
        """Escapes a string so it is valid within HTML or XML.
    
        Escapes the characters ``<``, ``>``, ``"``, ``'``, and ``&``.
        When used in attribute values the escaped strings must be enclosed
        in quotes.
    
        .. versionchanged:: 3.2
    
           Added the single quote to the list of escaped characters.
        """
>       return _XHTML_ESCAPE_RE.sub(
            lambda match: _XHTML_ESCAPE_DICT[match.group(0)], to_basestring(value)
        )
E       TypeError: expected string or bytes-like object

/opt/marta/baselines/codamosa/replication/test-apps/tornado/tornado/escape.py:54: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_linkify_0.py::test_valid_input[Hello http:/tornadoweb.org!-Hello <a href="http:/tornadoweb.org">http:/tornadoweb.org</a>!]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_linkify_0.py::test_none_input[None]
========================= 2 failed, 1 passed in 0.10s ==========================
"""