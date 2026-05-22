
import argparse
from unittest.mock import patch, MagicMock
import pytest

def _parse_options(args: list) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('task_id')
    parser.add_argument('--daemon', action='store_true')
    return parser.parse_known_args(args)[0]

@pytest.mark.parametrize("input_args, expected_task_id, expected_daemon", [
    (['1234'], '1234', False),
    (['--daemon', '1234'], '1234', True)
])
def test_valid_input(input_args, expected_task_id, expected_daemon):
    with patch('argparse.ArgumentParser.parse_known_args', return_value=(argparse.Namespace(task_id=expected_task_id, daemon=expected_daemon), [])):
        parsed_args = _parse_options(input_args)
        assert parsed_args.task_id == expected_task_id
        assert parsed_args.daemon == expected_daemon
