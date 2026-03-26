
import sys
from isort.main import parse_args
import pytest

def test_parse_args():
    # Test with no arguments
    argv = []
    args = parse_args(argv)
    assert isinstance(args, dict), "Expected a dictionary"
    assert not args, "Expected an empty dictionary for no arguments"

    # Test with specific arguments
    argv = ["--order-by-type"]
    args = parse_args(argv)
    assert "order_by_type" in args, "Expected order_by_type to be in the returned dictionary"
    assert args["order_by_type"], "Expected order_by_type to be True"

    # Test with deprecated arguments
    argv = ["--dont-order-by-type"]
    args = parse_args(argv)
    assert not args.get("order_by_type", True), "Expected order_by_type to be False after deprecation handling"

    # Test with multiple arguments
    argv = ["--order-by-type", "--float-to-top"]
    args = parse_args(argv)
    assert args.get("order_by_type", False), "Expected order_by_type to be True"
    assert args.get("float_to_top", False), "Expected float_to_top to be True"

    # Test with invalid multi-line output value
    argv = ["--multi-line-output=invalid"]
    with pytest.raises(SystemExit):
        parse_args(argv)

if __name__ == "__main__":
    sys.exit(pytest.main([sys.argv[0]]))
