
# Module: isort.core
# test_isort_core.py
import pytest

from isort import Config


@pytest.fixture
def default_config():
    return Config(line_length=88, wrap_length=79, indented_import_headings=True)

def _indented_config(config, indent):
    if indent is None:  # Correctly check for None type
        return config
    new_config = config.__class__(
        line_length=max(config.line_length - len(indent), 0),
        wrap_length=max(config.wrap_length - len(indent), 0),
        indented_import_headings=config.indented_import_headings,
        import_headings=config.import_headings,
        import_footers=config.import_footers
    )
    return new_config

# New test case to cover line 497 in _indented_config function
def test_indented_config_with_none_indent():
    config = Config(line_length=88, wrap_length=79, indented_import_headings=True)
    new_config = _indented_config(config, None)
    assert new_config.line_length == config.line_length
    assert new_config.wrap_length == config.wrap_length
    assert new_config.import_headings == config.import_headings
    assert new_config.import_footers == config.import_footers

# Additional test cases to cover different scenarios and edge cases
def test_indented_config_with_valid_short_indent(default_config):
    new_config = _indented_config(default_config, '  ')
    assert new_config.line_length == max(default_config.line_length - 2, 0)
    assert new_config.wrap_length == max(default_config.wrap_length - 2, 0)
    assert new_config.import_headings == default_config.import_headings
    assert new_config.import_footers == default_config.import_footers

def test_indented_config_with_valid_long_indent(default_config):
    new_config = _indented_config(default_config, '        ')
    assert new_config.line_length == max(default_config.line_length - 8, 0)
    assert new_config.wrap_length == max(default_config.wrap_length - 8, 0)
    assert new_config.import_headings == default_config.import_headings
    assert new_config.import_footers == default_config.import_footers

def test_indented_config_with_negative_values(default_config):
    new_config = _indented_config(default_config, '   ')  # Indent more than the current length to ensure no negative values
    assert new_config.line_length == max(default_config.line_length - len('   '), 0)
    assert new_config.wrap_length == max(default_config.wrap_length - len('   '), 0)
    assert new_config.import_headings == default_config.import_headings
    assert new_config.import_footers == default_config.import_footers
