
import pytest
from string_utils.manipulation import slugify
from string_utils.errors import InvalidInputError

class TestSlugifyFunction:
    
    def test_slugify_typical_string(self):
        assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'

    def test_slugify_non_ascii_characters(self):
        assert slugify('Mönstér Mägnët') == 'monster-magnet'

    def test_slugify_custom_separator(self):
        assert slugify('Top 10 Reasons To Love Dogs!!!', '_') == 'top_10_reasons_to_love_dogs'

    def test_slugify_empty_string(self):
        assert slugify('') == ''

    def test_slugify_only_special_chars(self):
        assert slugify('!!!@#$%^&*()') == ''

    def test_slugify_already_lowercase(self):
        assert slugify('this is already lowercase') == 'this-is-already-lowercase'

    def test_slugify_with_numbers(self):
        assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'

    @pytest.mark.xfail(reason="Expected InvalidInputError for non-string input")
    def test_slugify_non_string_input(self):
        with pytest.raises(InvalidInputError):
            slugify(None)
