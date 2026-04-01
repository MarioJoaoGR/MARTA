
import argparse
from isort import main
import pytest

@pytest.fixture
def parser():
    return main._build_arg_parser()

def test_valid_inputs(parser):
    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(['--help'])
    assert excinfo.value.code == 0
