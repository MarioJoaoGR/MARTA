
import pytest
from isort.main import _build_arg_parser

def test_invalid_input():
    with pytest.raises(SystemExit):
        try:
            parser = _build_arg_parser()
            parser.parse_args(["--invalid-option"])
        except SystemExit as e:
            assert e.code != 0, "Expected SystemExit to be raised with a non-zero exit code"
            raise
