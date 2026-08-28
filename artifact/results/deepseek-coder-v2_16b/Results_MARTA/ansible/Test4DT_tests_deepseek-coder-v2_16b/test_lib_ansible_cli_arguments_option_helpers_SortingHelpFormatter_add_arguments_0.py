
import argparse
from lib.ansible.cli.arguments.option_helpers import SortingHelpFormatter
import pytest


def test_invalid_input():
    with pytest.raises(TypeError):
        SortingHelpFormatter().add_arguments([])