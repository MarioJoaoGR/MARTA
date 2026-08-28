
import pytest
from argparse import Namespace
from py_backwards.conf import settings

def init_settings(args: Namespace) -> None:
    if args.debug:
        settings.debug = True

@pytest.fixture
def setup_valid_input():
    return Namespace(debug=False)

def test_valid_input_with_debug_false(setup_valid_input):
    init_settings(setup_valid_input)
    assert not settings.debug, "Debug mode should be set to False"
