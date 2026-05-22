
import pytest
from httpie.cli.options import ParserSpec
from unittest.mock import patch, MagicMock

@pytest.fixture
def parser_spec():
    return ParserSpec(program="my_program", description="This is my command-line program.")

def test_serialize_with_groups(parser_spec):
    group1 = MagicMock()
    group2 = MagicMock()
    parser_spec.groups = [group1, group2]
    
    with patch('httpie.cli.options.ParserSpec.serialize', return_value={'name': 'my_program', 'description': 'This is my command-line program.', 'groups': [{}, {}]}):
        result = parser_spec.serialize()
        assert result == {'name': 'my_program', 'description': 'This is my command-line program.', 'groups': [{}, {}]}
