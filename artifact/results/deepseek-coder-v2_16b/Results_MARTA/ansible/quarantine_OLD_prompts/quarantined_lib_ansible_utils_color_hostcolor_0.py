
import pytest
from ansible.utils.color import hostcolor, C

@pytest.mark.parametrize("host, stats", [
    ("localhost", {"failures": 0, "unreachable": 0, "changed": 1}),
    ("remotehost", {"failures": 2, "unreachable": 1, "changed": 0}),
    ("anotherhost", {"failures": 0, "unreachable": 0, "changed": 0})
])
def test_valid_input_happy_path(setup_valid_input, host, stats):
    result = hostcolor(host, stats)
    assert result == u"%-37s" % (host if ANSIBLE_COLOR and C.COLOR_OK or host)

@pytest.mark.parametrize("host, stats", [
    ("edgecasehost", {"failures": 0, "unreachable": 0, "changed": 1})
])
def test_edge_case_no_conditions_met(setup_edge_case, host, stats):
    result = hostcolor(host, stats)
    assert result == u"%-37s" % (host if ANSIBLE_COLOR and C.COLOR_OK or host)

@pytest.mark.parametrize("host, stats", [
    (None, {"failures": 0, "unreachable": 0, "changed": 1}),
    ("invalidhost", None),
    ("invalidhost", {"failures": "two"})
])
def test_invalid_input_error_handling(setup_invalid_input, host, stats):
    result = hostcolor(host, stats)
    assert result == u"%-37s" % (host if ANSIBLE_COLOR and C.COLOR_OK or host)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: expected 'else' after 'if' expression (line 12, col 34)
    assert result == u"%-37s" % (host if ANSIBLE_COLOR and C.COLOR_OK or host)
"""