
import sys
from isort import main
import pytest

def test_invalid_inputs():
    # Test invalid argument
    with pytest.raises(SystemExit):
        main.parse_args(["--invalid-arg"])
