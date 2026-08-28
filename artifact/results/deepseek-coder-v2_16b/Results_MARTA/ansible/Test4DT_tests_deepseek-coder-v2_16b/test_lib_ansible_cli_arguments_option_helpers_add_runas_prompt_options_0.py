
import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_runas_prompt_options



def test_default_values():
    parser = ArgumentParser()
    add_runas_prompt_options(parser)
    args = parser.parse_args([])
    assert not args.become_ask_pass