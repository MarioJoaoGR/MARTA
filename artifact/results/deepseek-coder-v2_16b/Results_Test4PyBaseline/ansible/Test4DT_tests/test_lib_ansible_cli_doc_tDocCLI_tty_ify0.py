
import pytest
from ansible.cli.doc import DocCLI
import re

@pytest.fixture
def cli():
    args = ['--list-modules']  # Example argument for testing
    return DocCLI(args)

def test_tty_ify_italic(cli):
    text = "This is an example with I(italic) and some more I(words)."
    expected = re.sub(r'I\(([^)]+)\)', r"`\1'", text)
    assert cli.tty_ify(text) == expected

def test_tty_ify_bold(cli):
    text = "Bold words are B(important) and should be highlighted."
    expected = re.sub(r'B\(([^)]+)\)', r"*\1*", text)
    assert cli.tty_ify(text) == expected

def test_tty_ify_module(cli):
    text = "Modules are M(useful) for automation tasks."
    expected = re.sub(r'M\(([^)]+)\)', r"[\1]", text)
    assert cli.tty_ify(text) == expected

def test_tty_ify_link(cli):
    text = "Links are L(click here, http://example.com) and should be clickable."
    expected = re.sub(r'L\(([^)]+), ([^)]+)\)', r"\1 <\2>", text)
    assert cli.tty_ify(text) == expected

def test_tty_ify_url(cli):
    text = "URLs are U(http://example.com) and can be visited."
    expected = re.sub(r'U\(([^)]+)\)', r"\1", text)
    assert cli.tty_ify(text) == expected

def test_tty_ify_ref(cli):
    text = "References are R(click here, sphinx-ref) and should point to useful information."
    expected = re.sub(r'R\(([^)]+), ([^)]+)\)', r"\1", text)
    assert cli.tty_ify(text) == expected

def test_tty_ify_const(cli):
    text = "Constants are C(MAX_VALUE) and represent important values."
    expected = re.sub(r'C\(([^)]+)\)', r"`\1'", text)
    assert cli.tty_ify(text) == expected

def test_tty_ify_ruler(cli):
    text = "HORIZONTALLINE marks a break in the documentation."
    expected = "\n{0}\n".format("-" * 13)