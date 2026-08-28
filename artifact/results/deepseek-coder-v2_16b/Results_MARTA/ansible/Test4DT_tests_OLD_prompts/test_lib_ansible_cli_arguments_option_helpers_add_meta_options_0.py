
import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_meta_options

def test_add_meta_options_without_args():
    parser = ArgumentParser()
    add_meta_options(parser)
    with pytest.raises(SystemExit) as e:
        args = parser.parse_args()
    assert str(e.value) == '2'

