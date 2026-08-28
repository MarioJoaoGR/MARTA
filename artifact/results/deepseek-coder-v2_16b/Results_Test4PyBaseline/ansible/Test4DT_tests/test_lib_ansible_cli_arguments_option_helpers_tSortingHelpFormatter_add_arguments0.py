
import pytest
import argparse
import operator
from ansible.cli.arguments.option_helpers import SortingHelpFormatter

@pytest.fixture
def setup_parser():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-a', '--alpha', help='Alpha option')
    parser.add_argument('-b', '--beta', help='Beta option')
    parser.add_argument('-c', '--charlie', help='Charlie option')
    return parser

def test_sorting_help_formatter(setup_parser):
    # Arrange
    parser = setup_parser
    
    # Act
    args = parser.parse_args(['-a', 'value_alpha', '-b', 'value_beta', '-c', 'value_charlie'])
    
    # Assert
    assert hasattr(args, 'alpha') and getattr(args, 'alpha') == 'value_alpha'
    assert hasattr(args, 'beta') and getattr(args, 'beta') == 'value_beta'
    assert hasattr(args, 'charlie') and getattr(args, 'charlie') == 'value_charlie'

def test_sorting_help_formatter_no_arguments(setup_parser):
    # Arrange
    parser = setup_parser
    
    # Act
    args = parser.parse_args([])
    
    # Assert
    assert not hasattr(args, 'alpha')
    assert not hasattr(args, 'beta')
    assert not hasattr(args, 'charlie')

def test_sorting_help_formatter_partial_arguments(setup_parser):
    # Arrange
    parser = setup_parser
    
    # Act
    args = parser.parse_args(['-a', 'value_alpha'])
    
    # Assert
    assert hasattr(args, 'alpha') and getattr(args, 'alpha') == 'value_alpha'
    assert not hasattr(args, 'beta')
    assert not hasattr(args, 'charlie')
