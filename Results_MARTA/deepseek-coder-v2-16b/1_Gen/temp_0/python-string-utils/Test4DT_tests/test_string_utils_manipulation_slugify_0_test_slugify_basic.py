
import re
from string_utils.manipulation import slugify, is_string, InvalidInputError

def test_slugify_basic():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
