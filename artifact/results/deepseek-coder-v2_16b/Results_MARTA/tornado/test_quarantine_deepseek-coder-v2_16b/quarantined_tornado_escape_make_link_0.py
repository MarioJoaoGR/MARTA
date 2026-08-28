
import pytest
from tornado import escape
import re

def make_link(m: typing.Match, require_protocol=False, permitted_protocols=["http", "https"], extra_params=None, shorten=False) -> str:
    url = m.group(1)
    proto = m.group(2)
    if require_protocol and not proto:
        return url  # not protocol, no linkify

    if proto and proto not in permitted_protocols:
        return url  # bad protocol, no linkify

    href = m.group(1)
    if not proto:
        href = "http://" + href  # no proto specified, use http

    if callable(extra_params):
        params = " " + extra_params(href).strip()
    else:
        params = extra_params

    # clip long urls. max_len is just an approximation
    max_len = 30
    if shorten and len(url) > max_len:
        before_clip = url
        if proto:
            proto_len = len(proto) + 1 + len(m.group(3) or "")  # +1 for :
        else:
            proto_len = 0

        parts = url[proto_len:].split("/")
        if len(parts) > 1:
            # Grab the whole host part plus the first bit of the path
            # The path is usually not that interesting once shortened
            # (no more slug, etc), so it really just provides a little
            # extra indication of shortening.
            url = (
                url[:proto_len]
                + parts[0]
                + "/"
                + parts[1][:8].split("?")[0].split(".")[0]
            )

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

# Test cases for make_link function
def test_make_link_basic():
    pattern = re.compile(r'(https?://)?(www\.)?(\w+\.\w+)')
    match = pattern.match("http://example.com")
    assert make_link(match) == '<a href="http://example.com">example.com</a>'

def test_make_link_no_protocol():
    pattern = re.compile(r'(https?://)?(www\.)?(\w+\.\w+)')
    match = pattern.match("//example.com")
    assert make_link(match) == '<a href="http://example.com">example.com</a>'

def test_make_link_extra_params():
    def extra_params(url):
        return 'title="Click here" class="external"'
    
    pattern = re.compile(r'(https?://)?(www\.)?(\w+\.\w+)')
    match = pattern.match("http://example.com")
    assert make_link(match, extra_params=extra_params) == '<a href="http://example.com" title="Click here" class="external">example.com</a>'

def test_make_link_shorten():
    pattern = re.compile(r'(https?://)?(www\.)?(\w+\.\w+)')
    match = pattern.match("http://verylongurlwithmanycharacters.com/path/to/resource")
    assert make_link(match, shorten=True) == '<a href="http://verylongur..." title="Click here" class="external">verylongur...</a>'

def test_make_link_require_protocol():
    pattern = re.compile(r'(https?://)?(www\.)?(\w+\.\w+)')
    match = pattern.match("http://example.com")
    assert make_link(match, require_protocol=True, permitted_protocols=["http", "https"]) == '<a href="http://example.com">example.com</a>'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____________ ERROR collecting test_tornado_escape_make_link_0.py ______________
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_make_link_0.py:6: in <module>
    def make_link(m: typing.Match, require_protocol=False, permitted_protocols=["http", "https"], extra_params=None, shorten=False) -> str:
E   NameError: name 'typing' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_make_link_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""