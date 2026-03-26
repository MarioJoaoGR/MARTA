
import pytest
from flutes.io import progress_open
import io
import os

@pytest.fixture(scope="module")
def sample_file(tmpdir_factory):
    file_path = tmpdir_factory.mktemp("data").join("sample.txt")
    with open(str(file_path), "w") as f:
        f.write("Hello, world!")
    return str(file_path)

def test_happy_path(sample_file):
    with progress_open(sample_file, mode="r") as f:
        assert isinstance(f, io.TextIOWrapper)
        assert hasattr(f, "progress_bar")
        content = f.read()
        assert content == "Hello, world!"
