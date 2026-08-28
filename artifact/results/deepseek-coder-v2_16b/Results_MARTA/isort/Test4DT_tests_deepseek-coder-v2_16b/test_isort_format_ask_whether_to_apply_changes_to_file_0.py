
import pytest
from isort.format import ask_whether_to_apply_changes_to_file
import sys



def test_user_quits_the_process():
    # Mock input to simulate user quitting the process
    with pytest.raises(SystemExit) as exc_info:
        with pytest.MonkeyPatch.context() as monkeypatch:
            monkeypatch.setattr('builtins.input', lambda _: 'q')
            ask_whether_to_apply_changes_to_file("example.txt")
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 1