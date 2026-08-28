
import pytest
import yaml
from ansible.parsing.yaml.dumper import SafeDumper

@pytest.fixture(scope="module")
def safe_representer():
    dumper = SafeDumper()
    return dumper


def test_edge_case_none():
    # Define a YAML document with None value
    yaml_document = {
        'message': None
    }
    
    # Dump the YAML document using the default representer
    yaml_representation = yaml.dump(yaml_document)
    
    assert isinstance(yaml_representation, str), "Expected a string representation"
    assert yaml_representation == "message: null\n", f"Unexpected representation: {yaml_representation}"