
import pytest
from ansible.galaxy.api import CollectionVersionMetadata


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