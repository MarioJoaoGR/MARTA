
import argparse
import pytest
from ansible.cli.arguments.option_helpers import add_inventory_options

# Test valid inputs
def test_valid_inputs():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(['--list-hosts'])
    assert args.listhosts is True
    
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(['-l', 'pattern'])
    assert args.subset == 'pattern'
    
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(['-i', 'host1,host2'])
    assert args.inventory == ['host1', 'host2']

# Test edge cases
def test_edge_cases():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(['--list-hosts'])
    assert args.listhosts is True
    
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args([])
    assert args.subset == C.DEFAULT_SUBSET
    
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(['-i'])
    assert args.inventory is None

# Test invalid inputs
def test_invalid_inputs():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    with pytest.raises(SystemExit):
        parser.parse_args(['--invalid-option'])
    
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    with pytest.raises(SystemExit):
        parser.parse_args(['-i', 'host1,host2', '--invalid-option'])
    
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    with pytest.raises(SystemExit):
        parser.parse_args(['-l', 'pattern', '-i', 'host1,host2', '--invalid-option'])
