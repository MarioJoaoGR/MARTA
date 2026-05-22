
import pytest
from httpie.cli.options import ParserSpec
from unittest.mock import patch, MagicMock

@pytest.fixture
def parser_spec():
    return ParserSpec(program="my_program", description="This is my command-line program.")

def test_serialize(parser_spec):
    # Create a mock group for testing
    mock_group = MagicMock()
    mock_group.serialize = MagicMock(return_value={'name': 'mock_group'})
    
    # Add the mock group to the parser specification
    parser_spec.groups.append(mock_group)
    
    # Patch the serialize method of the Group class to return a mocked result
    with patch('httpie.cli.options.Group.serialize', side_effect=lambda: {'name': 'mock_group'}):
        serialized = parser_spec.serialize()
        
        assert serialized == {
            'name': 'my_program',
            'description': 'This is my command-line program.',
            'groups': [{'name': 'mock_group'}],
        }
