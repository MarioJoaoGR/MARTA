
import pytest
from isort.format import format_simplified


def test_from_import_statement():
    assert format_simplified("from math import sqrt") == "math.sqrt"

def test_import_statement():
    assert format_simplified("import os") == "os"

def test_from_import_with_spaces():
    assert format_simplified("   from collections import defaultdict   ") == "collections.defaultdict"

def test_import_with_spaces():
    assert format_simplified("   import datetime   ") == "datetime"


def test_empty_string_input():
    assert format_simplified("") == ""
