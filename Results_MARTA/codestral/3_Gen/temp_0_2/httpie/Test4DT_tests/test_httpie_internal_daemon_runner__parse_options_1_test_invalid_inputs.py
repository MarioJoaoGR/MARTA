
import pytest
import argparse
from typing import List

def _parse_options(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('task_id')
    parser.add_argument('--daemon', action='store_true')
    return parser.parse_known_args(args)[0]

def test_invalid_inputs():
    with pytest.raises(SystemExit):
        _parse_options(['--invalid-option'])
