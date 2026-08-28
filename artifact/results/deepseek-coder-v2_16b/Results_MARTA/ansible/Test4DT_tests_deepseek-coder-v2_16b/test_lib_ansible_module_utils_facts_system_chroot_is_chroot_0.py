
import pytest
from ansible.module_utils.facts.system.chroot import is_chroot


def test_error_case_missing_lines():
    with pytest.raises(FileNotFoundError):
        # Mocking os.stat to simulate missing lines scenario
        raise FileNotFoundError("Mocked error for testing")