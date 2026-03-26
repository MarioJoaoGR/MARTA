
import sys
from isort.main import parse_args
from argparse import ArgumentParser
from unittest.mock import patch

# Mocking DEPRECATED_SINGLE_DASH_ARGS for testing
DEPRECATED_SINGLE_DASH_ARGS = ["dont_order_by_type", "dont_follow_links"]

def test_invalid_inputs():
    with patch('sys.argv', ['script_name'] + [f"-{arg}" for arg in DEPRECATED_SINGLE_DASH_ARGS]):
        try:
            args = parse_args()
            assert "order_by_type" not in args, "Expected order_by_type to be False after remapping deprecated args"
            assert "follow_links" not in args, "Expected follow_links to be False after remapping deprecated args"
        except SystemExit as e:
            assert str(e) == "Can't set both --float-to-top and --dont-float-to-top.", "Unexpected SystemExit message"
