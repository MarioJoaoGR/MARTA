
import pytest
from youtube_dl.options import parseOpts


def test_parseOpts_with_override():
    override_args = ['--username', 'user123', '--password', 'pass123']
    parser, opts, args = parseOpts(overrideArguments=override_args)
    assert hasattr(opts, 'username'), "Expected option '--username' to be present"
    assert opts.username == 'user123', "Expected option '--username' to be set to 'user123'"
    assert hasattr(opts, 'password'), "Expected option '--password' to be present"
    assert opts.password == 'pass123', "Expected option '--password' to be set to 'pass123'"
