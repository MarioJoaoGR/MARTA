
import re
from string_utils.manipulation import slugify, asciify

def test_slugify_basic():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
