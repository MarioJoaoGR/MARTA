
import pytest
from httpie.cli.argparser import HTTPieHelpFormatter
import argparse
import sys
from unittest.mock import patch

def test_invalid_inputs():
    with pytest.raises(TypeError):
        formatter = HTTPieHelpFormatter(max_help_position='invalid')
