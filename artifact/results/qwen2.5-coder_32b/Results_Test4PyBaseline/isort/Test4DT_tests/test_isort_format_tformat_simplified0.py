
from isort.format import format_simplified


def test_from_import():
    assert format_simplified("from math import sqrt") == "math.sqrt"
    assert format_simplified("from collections import defaultdict") == "collections.defaultdict"
    assert format_simplified("from package.module import function") == "package.module.function"


def test_import_module():
    assert format_simplified("import os") == "os"
    assert format_simplified("import sys") == "sys"