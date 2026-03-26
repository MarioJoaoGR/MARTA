
# Module: isort.core
# test_isort_core.py
import pytest

from isort import Config


@pytest.fixture
def default_config():
    return Config(line_length=88, wrap_length=79, indented_import_headings=True)

def _indented_config(config: Config, indent: str) -> Config:
    if not indent:
        return config

    return Config(
        config=config,
        line_length=max(config.line_length - len(indent), 0),
        wrap_length=max(config.wrap_length - len(indent), 0),
        lines_after_imports=1,
        import_headings=config.import_headings if config.indented_import_headings else {},
        import_footers=config.import_footers if config.indented_import_headings else {},
    )

def test_indented_config_with_valid_indent(default_config):
    new_config = _indented_config(default_config, '    ')
    assert new_config.line_length == max(default_config.line_length - 4, 0)
    assert new_config.wrap_length == max(default_config.wrap_length - 4, 0)
    assert new_config.import_headings == default_config.import_headings
    assert new_config.import_footers == default_config.import_footers

def test_indented_config_with_empty_indent(default_config):
    unchanged_config = _indented_config(default_config, '')
    assert unchanged_config.line_length == default_config.line_length
    assert unchanged_config.wrap_length == default_config.wrap_length
    assert unchanged_config.import_headings == default_config.import_headings
    assert unchanged_config.import_footers == default_config.import_footers

def test_indented_config_with_negative_values(default_config):
    new_config = _indented_config(default_config, '   ')  # Indent more than the current length to ensure no negative values
    assert new_config.line_length == max(default_config.line_length - len('   '), 0)
    assert new_config.wrap_length == max(default_config.wrap_length - len('   '), 0)
    assert new_config.import_headings == default_config.import_headings
    assert new_config.import_footers == default_config.import_footers

def test_indented_config_with_zero_values(default_config):
    new_config = _indented_config(default_config, '    ')  # Indent with the same length as current to ensure no negative values
    assert new_config.line_length == max(default_config.line_length - len('    '), 0)
    assert new_config.wrap_length == max(default_config.wrap_length - len('    '), 0)
    assert new_config.import_headings == default_config.import_headings
    assert new_config.import_footers == default_config.import_footers
