# Module: ansible.cli.doc
# test_doccli.py
from ansible.cli.doc import DocCLI
import pytest

@pytest.fixture
def cli():
    args = ['--list-modules']  # Assuming args is a list containing the command-line argument for listing modules.
    return DocCLI(args=args)

def test_init(cli):
    assert isinstance(cli, DocCLI), "DocCLI instance should be created successfully."

def test_get_role_man_text(cli):
    role = "some_role"
    role_json = {
        'entry_points': {
            'main': {'short_description': 'Main entry point'},
            'secondary': {'short_description': 'Secondary entry point'}
        },
        'path': '/path/to/role'
    }
    result = cli.get_role_man_text(role, role_json)
    assert isinstance(result, list), "The method should return a list of strings."
    assert len(result) > 0, "The list should contain at least one string."
    for line in result:
        assert isinstance(line, str), f"Each item in the list should be a string. Found: {type(line)}"

def test_get_role_man_text_no_entry_points(cli):
    role = "some_role"
    role_json = {'path': '/path/to/role'}
    result = cli.get_role_man_text(role, role_json)
    assert isinstance(result, list), "The method should return a list of strings."
    assert len(result) == 1, "There should be only one line if there are no entry points."
    assert result[0] == "> SOME_ROLE    (/path/to/role)\n", "The first line should indicate the role and path."

def test_get_role_man_text_with_options(cli):
    role = "some_role"
    role_json = {
        'entry_points': {'main': {'short_description': 'Main entry point'}},
        'path': '/path/to/role',
        'options': {
            'option1': {'mandatory': True, 'description': ['Option 1 description']},
            'option2': {'mandatory': False, 'description': ['Option 2 description']}
        }
    }
    result = cli.get_role_man_text(role, role_json)
    assert "OPTIONS (= is mandatory):\n" in result[1], "The options section should be included with the correct indentation."
    assert 'option1' in result[2], "The first option should be listed as mandatory."
    assert 'option2' in result[3], "The second option should be listed as not mandatory."

def test_get_role_man_text_with_attributes(cli):
    role = "some_role"
    role_json = {
        'entry_points': {'main': {'short_description': 'Main entry point'}},
        'path': '/path/to/role',
        'attributes': {'attr1': 'value1', 'attr2': 'value2'}
    }
    result = cli.get_role_man_text(role, role_json)
    assert "ATTRIBUTES:\n" in result[1], "The attributes section should be included with the correct indentation."
    assert 'attr1' in result[2], "The first attribute should be listed."
    assert 'attr2' in result[3], "The second attribute should be listed."
