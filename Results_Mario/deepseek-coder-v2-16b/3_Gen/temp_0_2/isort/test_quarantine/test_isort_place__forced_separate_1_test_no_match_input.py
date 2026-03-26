
import pytest
from isort.place import fnmatch
from config import Config

def _forced_separate(name: str, config: Config) -> tuple[str, str] | None:
    for forced_separate in config.forced_separate:
        # Ensure all forced_separate patterns will match to end of string
        path_glob = forced_separate
        if not forced_separate.endswith("*"):
            path_glob = f"{forced_separate}*"

        if fnmatch(name, path_glob) or fnmatch(name, "." + path_glob):
            return (forced_separate, f"Matched forced_separate ({forced_separate}) config value.")

    return None

@pytest.mark.parametrize("name, expected", [
    ("example.log", ('*.log', "Matched forced_separate (*.log) config value.")),
    ("structure/data.csv", None),
    ("anotherfile.txt", None),
])
def test_no_match_input(name, expected):
    config = Config({'forced_separate': ['*.log', 'data.*']})
    result = _forced_separate(name, config)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__forced_separate_1_test_no_match_input
isort/Test4DT_tests/test_isort_place__forced_separate_1_test_no_match_input.py:4:0: E0401: Unable to import 'config' (import-error)


"""