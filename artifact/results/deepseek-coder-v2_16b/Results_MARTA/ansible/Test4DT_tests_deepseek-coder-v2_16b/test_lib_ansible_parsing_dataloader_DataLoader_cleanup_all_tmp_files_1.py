
import pytest
from ansible.parsing.dataloader import DataLoader

@pytest.fixture(scope="module")
def setup_dl():
    dl = DataLoader()
    yield dl
    # Cleanup all temporary files after the tests are done
    dl.cleanup_all_tmp_files()

def test_valid_input(setup_dl):
    data_source = '{"key": "value"}'
    result = setup_dl.load(data_source)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
    assert result == {"key": "value"}, f"Unexpected content: {result}"
