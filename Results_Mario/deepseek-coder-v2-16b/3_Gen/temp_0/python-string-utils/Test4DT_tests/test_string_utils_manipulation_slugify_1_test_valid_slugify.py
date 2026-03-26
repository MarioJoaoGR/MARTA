
import pytest
from string_utils import manipulation  # Assuming this is the correct module path

def test_valid_slugify():
    assert manipulation.slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert manipulation.slugify('Mönstér Mägnët') == 'monster-magnet'
