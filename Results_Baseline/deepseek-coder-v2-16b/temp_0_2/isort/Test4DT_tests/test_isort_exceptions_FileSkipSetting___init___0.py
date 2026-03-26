
# Module: isort.exceptions
# test_isort_exceptions.py
import pytest

from isort.exceptions import FileSkipSetting


def test_basic_usage():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting("example_file.py")
    assert str(exc_info.value) == "example_file.py was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

@pytest.mark.parametrize("custom_info", ["additional details"])
def test_with_custom_message(custom_info):
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting("example_file.py", custom_info=custom_info)
    assert str(exc_info.value) == "example_file.py was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"