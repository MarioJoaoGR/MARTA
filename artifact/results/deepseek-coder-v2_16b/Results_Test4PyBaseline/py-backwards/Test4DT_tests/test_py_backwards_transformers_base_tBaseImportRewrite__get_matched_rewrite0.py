
# Module: py_backwards.transformers.base
import pytest
from py_backwards.transformers.base import BaseImportRewrite

# Test cases for _get_matched_rewrite method
def test_exact_match():
    base_import = BaseImportRewrite(tree=None)  # Adding tree parameter to satisfy pylint error
    base_import.rewrites = [('math', 'mathematics'), ('os', 'operating_system')]
    assert base_import._get_matched_rewrite('math') == ('math', 'mathematics')

def test_prefix_match():
    base_import = BaseImportRewrite(tree=None)  # Adding tree parameter to satisfy pylint error
    base_import.rewrites = [('math', 'mathematics'), ('os', 'operating_system')]
    assert base_import._get_matched_rewrite('os.name') == ('os', 'operating_system')

def test_no_match():
    base_import = BaseImportRewrite(tree=None)  # Adding tree parameter to satisfy pylint error
    base_import.rewrites = [('math', 'mathematics'), ('os', 'operating_system')]
    assert base_import._get_matched_rewrite('random') is None

def test_none_input():
    base_import = BaseImportRewrite(tree=None)  # Adding tree parameter to satisfy pylint error
    base_import.rewrites = [('math', 'mathematics'), ('os', 'operating_system')]
    assert base_import._get_matched_rewrite(None) is None
