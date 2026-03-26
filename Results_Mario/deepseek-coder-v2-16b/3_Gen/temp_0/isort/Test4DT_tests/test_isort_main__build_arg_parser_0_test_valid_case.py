
import argparse
from unittest.mock import patch

import pytest

from isort.main import _build_arg_parser


@pytest.fixture(autouse=True)
def mock_argparse():
    with patch('isort.main._build_arg_parser') as mock:
        yield mock

def test_valid_case():
    parser = _build_arg_parser()
    assert isinstance(parser, argparse.ArgumentParser)
