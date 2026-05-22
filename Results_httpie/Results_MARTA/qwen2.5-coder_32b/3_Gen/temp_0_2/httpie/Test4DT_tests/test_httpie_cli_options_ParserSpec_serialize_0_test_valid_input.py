
import pytest
from httpie.cli.options import ParserSpec
from unittest.mock import patch, MagicMock

@pytest.fixture
def parser_spec():
    return ParserSpec(program="my_program", description="This is my command-line program.")

def test_serialize(parser_spec):
    # Add a mock group to the parser specification for testing
    mock_group = MagicMock()
    mock_group.serialize = MagicMock(return_value={'name': 'mock_group'})
    parser_spec.groups.append(mock_group)
    
    expected_output = {
        'name': 'my_program',
        'description': 'This is my command-line program.',
        'groups': [{'name': 'mock_group'}]
    }
    
    assert parser_spec.serialize() == expected_output
