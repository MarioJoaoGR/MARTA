
# Module: youtube_dl.extractor.archiveorg
import pytest
from youtube_dl.extractor import archiveorg

# Assuming get_optional should be defined here or imported correctly
def get_optional(metadata, field):
    if isinstance(metadata.get(field), list):
        return metadata[field][0]
    return metadata.get(field)

archiveorg.get_optional = get_optional  # Assuming this is the correct way to assign or define it

# Test Case 1: Retrieving a value from an existing dictionary field
def test_get_optional_existing_field():
    metadata = {'key': 'value'}
    field = 'key'
    result = archiveorg.get_optional(metadata, field)
    assert result == 'value'

# Test Case 2: Handling a non-existent field by returning None
def test_get_optional_non_existent_field():
    metadata = {}
    field = 'non_existent_key'
    result = archiveorg.get_optional(metadata, field)
    assert result is None

# Test Case 3: Retrieving the first element from a list in the dictionary
def test_get_optional_list_field():
    metadata = {'another_key': [1, 2, 3]}
    field = 'another_key'
    result = archiveorg.get_optional(metadata, field)
    assert result == 1

# Test Case 4: Retrieving a value from an existing dictionary field with different metadata structure
def test_get_optional_existing_field_different_structure():
    metadata = {'other_key': 'other_value'}
    field = 'other_key'
    result = archiveorg.get_optional(metadata, field)
    assert result == 'other_value'

# Test Case 5: Handling a non-existent field with default value of None by returning None
def test_get_optional_non_existent_field_default():
    metadata = {}
    field = 'non_existent_key'
    result = archiveorg.get_optional(metadata, field)
    assert result is None

# Test Case 6: Retrieving the first element from a list in the dictionary with different metadata structure
def test_get_optional_list_field_different_structure():
    metadata = {'another_key': [4, 5, 6]}
    field = 'another_key'
    result = archiveorg.get_optional(metadata, field)
    assert result == 4
