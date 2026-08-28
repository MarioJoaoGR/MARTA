
import pytest
from isort.format import ask_whether_to_apply_changes_to_file
import sys



def test_user_decides_to_quit():
    # Mock input to simulate user deciding to quit the process
    with pytest.raises(SystemExit):
        with pytest.MonkeyPatch.context() as monkeypatch:
            monkeypatch.setattr('builtins.input', lambda _: 'q')
            ask_whether_to_apply_changes_to_file("example.txt")
    assert True  # No assertion needed, just checking for SystemExit