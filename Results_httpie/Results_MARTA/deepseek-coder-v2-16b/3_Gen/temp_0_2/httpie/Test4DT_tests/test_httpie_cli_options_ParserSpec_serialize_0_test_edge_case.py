
import pytest
from httpie.cli.options import ParserSpec
from unittest.mock import patch
from typing import List, Optional, Dict, Any

@pytest.fixture
def parser_spec():
    return ParserSpec(program="my_program", description="This is my command-line program.")

def test_serialize_basic(parser_spec):
    # Add a group to the parser specification for testing
    from httpie.cli.options import Group
    group = Group(name="test_group")
    parser_spec.groups.append(group)
    
    with patch('httpie.cli.options.Group.serialize', return_value={'name': 'test_group'}):
        result = parser_spec.serialize()
        assert result == {
            'name': 'my_program',
            'description': 'This is my command-line program.',
            'groups': [{'name': 'test_group'}]
        }
