
import pytest
from apimd.loader import gen_api
from unittest.mock import patch

# Test scenario: Dry run enabled, no files should be written

# Test scenario: Dry run disabled, files should be written (mocking file writing to avoid actual I/O)
def test_gen_api_no_dry_run():
    root_names = {'Package One': 'package1'}
    with patch('apimd.loader.loader', return_value='## Package One API\nContent for package1'), \
         patch('os.path.isdir', return_value=False), \
         patch('os.mkdir'):
        generated_docs = gen_api(root_names, dry=False)
    
    # Assert that documentation files are written
    assert len(generated_docs) == 1

# Test scenario: Multiple packages with dry run enabled

# Test scenario: Multiple packages with dry run disabled
def test_gen_api_multiple_packages_no_dry_run():
    root_names = {'Package One': 'package1', 'Package Two': 'package2'}
    with patch('apimd.loader.loader', side_effect=['## Package One API\nContent for package1', '## Package Two API\nContent for package2']), \
         patch('os.path.isdir', return_value=False), \
         patch('os.mkdir'):
        generated_docs = gen_api(root_names, dry=False)
    
    # Assert that documentation files are written
    assert len(generated_docs) == 2

# Test scenario: Package not found (dry run enabled)
def test_gen_api_package_not_found_dry_run():
    root_names = {'Package One': 'package1'}
    with patch('apimd.loader.loader', return_value=''):
        generated_docs = gen_api(root_names, dry=True)
    
    # Assert that no documentation files are written
    assert len(generated_docs) == 0

# Test scenario: Package not found (dry run disabled)
def test_gen_api_package_not_found_no_dry_run():
    root_names = {'Package One': 'package1'}
    with patch('apimd.loader.loader', return_value=''), \
         patch('os.path.isdir', return_value=False), \
         patch('os.mkdir'):
        generated_docs = gen_api(root_names, dry=False)
    
    # Assert that no documentation files are written
    assert len(generated_docs) == 0

# Test scenario: Custom prefix directory (dry run enabled)

# Test scenario: Custom prefix directory (dry run disabled)
def test_gen_api_custom_prefix_no_dry_run():
    root_names = {'Package One': 'package1'}
    with patch('apimd.loader.loader', return_value='## Package One API\nContent for package1'), \
         patch('os.path.isdir', return_value=False), \
         patch('os.mkdir'):
        generated_docs = gen_api(root_names, prefix='custom-docs', dry=False)
    
    # Assert that documentation files are written
    assert len(generated_docs) == 1