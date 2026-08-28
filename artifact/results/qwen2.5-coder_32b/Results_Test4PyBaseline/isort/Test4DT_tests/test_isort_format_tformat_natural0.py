
from isort.format import format_natural


def test_simple_module_name():
    assert format_natural("os") == "import os"
    assert format_natural("math") == "import math"

def test_dotted_path():
    assert format_natural("numpy.random") == "from numpy import random"
    assert format_natural("sys.path") == "from sys import path"

def test_already_formatted_import_statement():
    assert format_natural("from math import sqrt") == "from math import sqrt"
    assert format_natural("import json") == "import json"

def test_leading_trailing_whitespace():
    assert format_natural("   pandas ") == "import pandas"
    assert format_natural(" collections  ") == "import collections"

def test_empty_string():
    assert format_natural("") == "import "

def test_single_dot():
    assert format_natural(".") == "from  import "

def test_double_dotted_path():
    assert format_natural("a.b.c") == "from a.b import c"
    assert format_natural("x.y.z.w") == "from x.y.z import w"

def test_invalid_import_statement():
    assert format_natural("os.path.join") == "from os.path import join"
    assert format_natural("datetime.datetime.now") == "from datetime.datetime import now"
