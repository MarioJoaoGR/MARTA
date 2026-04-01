
import pytest

from isort.settings import Config


def test_valid_inputs():
    with pytest.raises(ValueError) as excinfo:
        valid_config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'buck-out', '.direnv', '.bzr', 'venv', '.pytype'}), format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
    assert str(excinfo.value) == "The python version py3 is not supported. You can set a python version with the -py or --python-version flag. The following versions are supported: ('all', '2', '27', '3', '310', '311', '312', '313', '314', '36', '37', '38', '39')"
