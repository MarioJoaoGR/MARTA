
import pytest
from string_utils.manipulation import slugify
try:
    from invalid_input_error import InvalidInputError
except ImportError:
    class InvalidInputError(Exception):
        pass
import re

# Assuming NO_LETTERS_OR_NUMBERS_RE and SPACES_RE are defined elsewhere in the module
NO_LETTERS_OR_NUMBERS_RE = re.compile(r'[^a-zA-Z0-9]')
SPACES_RE = re.compile(r'\s+')

def test_slugify_with_default_separator():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'

def test_slugify_with_specified_separator():
    assert slugify('Mönstér Mägnët', separator='|') == 'monster|magnet'

def test_slugify_lowercase():
    result = slugify('Top 10 Reasons To Love Dogs!!!')
    assert result.islower(), f"Expected lowercase string, but got {result}"

def test_slugify_no_spaces():
    result = slugify('Top 10 Reasons To Love Dogs!!!')