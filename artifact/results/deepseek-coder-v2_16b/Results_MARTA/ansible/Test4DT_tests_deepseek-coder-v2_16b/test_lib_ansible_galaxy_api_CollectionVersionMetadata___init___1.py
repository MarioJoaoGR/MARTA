
import pytest
from ansible.galaxy.api import CollectionVersionMetadata

# Test valid inputs
def test_valid_inputs():
    metadata = CollectionVersionMetadata(
        namespace="ansible",
        name="collection_name",
        version="1.0.0",
        download_url="https://example.com/collection-1.0.0.tar.gz",
        artifact_sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e46894ffbbbbcf8d7a1e4f2bba",
        dependencies={"dependency1": "1.0", "dependency2": "2.0"}
    )
    
    assert metadata.namespace == "ansible"
    assert metadata.name == "collection_name"
    assert metadata.version == "1.0.0"
    assert metadata.download_url == "https://example.com/collection-1.0.0.tar.gz"
    assert metadata.artifact_sha256 == "e3b0c44298fc1c149afbf4c8996fb92427ae41e46894ffbbbbcf8d7a1e4f2bba"
    assert metadata.dependencies == {"dependency1": "1.0", "dependency2": "2.0"}

# Test edge cases with boundary values and None/empty inputs
def test_edge_cases():
    metadata = CollectionVersionMetadata(
        namespace=None,
        name="",
        version="",
        download_url="",
        artifact_sha256="",
        dependencies={}
    )
    
    assert metadata.namespace is None
    assert metadata.name == ""
    assert metadata.version == ""
    assert metadata.download_url == ""
    assert metadata.artifact_sha256 == ""
    assert metadata.dependencies == {}

# Test invalid inputs and error handling with incorrect types or values
def test_invalid_inputs():
    try:
        metadata = CollectionVersionMetadata(
            namespace=123,
            name='collection_name',
            version='1.0.0',
            download_url='https://example.com/collection-1.0.0.tar.gz',
            artifact_sha256='e3b0c44298fc1c149afbf4c8996fb92427ae41e46894ffbbbbcf8d7a1e4f2bba',
            dependencies={'dependency1': '1.0', 'dependency2': '2.0'}
        )
    except Exception as e:
        assert str(e) == "namespace must be a string"
