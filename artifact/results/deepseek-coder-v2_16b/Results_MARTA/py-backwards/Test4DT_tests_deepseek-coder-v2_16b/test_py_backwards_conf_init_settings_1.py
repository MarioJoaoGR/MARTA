
import pytest
from argparse import Namespace
from py_backwards.conf import init_settings, settings

def test_valid_input_with_debug_true():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
