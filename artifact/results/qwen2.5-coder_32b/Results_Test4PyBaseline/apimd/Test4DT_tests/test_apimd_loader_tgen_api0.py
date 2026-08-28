# Module: apimd.loader
import pytest
from apimd.loader import gen_api
from unittest.mock import patch, MagicMock
from os.path import isdir, join
from typing import Sequence

# Mocking necessary functions and modules
@patch('apimd.loader.sys_path')
@patch('apimd.loader.logger')
@patch('apimd.loader.mkdir')
@patch('apimd.loader._site_path')
@patch('apimd.loader.loader')
@patch('apimd.loader._write')
def test_gen_api_basic(
    mock_write, mock_loader, mock_site_path, mock_mkdir, mock_logger, mock_sys_path
):
    # Arrange
    root_names = {'Package One': 'package1', 'Package Two': 'package2'}
    mock_loader.return_value = "Generated API documentation"
    mock_site_path.return_value = "/site/path"

    # Act
    result = gen_api(root_names)

    # Assert
    assert len(result) == 2
    for title, name in root_names.items():
        expected_doc = f"# {title} API\n\nGenerated API documentation"
        assert expected_doc in result
        mock_loader.assert_any_call(name, "/site/path", True, 1, False)
        path = join('docs', f"{name.replace('_', '-')}-api.md")
        mock_write.assert_any_call(path, expected_doc)

@patch('apimd.loader.sys_path')
@patch('apimd.loader.logger')
@patch('apimd.loader.mkdir')
@patch('apimd.loader._site_path')
@patch('apimd.loader.loader')
@patch('apimd.loader._write')
def test_gen_api_custom_prefix(
    mock_write, mock_loader, mock_site_path, mock_mkdir, mock_logger, mock_sys_path
):
    # Arrange
    root_names = {'Package One': 'package1'}
    prefix = 'api-docs'
    mock_loader.return_value = "Generated API documentation"
    mock_site_path.return_value = "/site/path"

    # Act
    result = gen_api(root_names, prefix=prefix)

    # Assert
    assert len(result) == 1
    expected_doc = "# Package One API\n\nGenerated API documentation"
    assert expected_doc in result
    path = join(prefix, "package1-api.md")
    mock_write.assert_called_once_with(path, expected_doc)

@patch('apimd.loader.sys_path')
@patch('apimd.loader.logger')
@patch('apimd.loader.mkdir')
@patch('apimd.loader._site_path')
@patch('apimd.loader.loader')
@patch('apimd.loader._write')
def test_gen_api_link_toc_level(
    mock_write, mock_loader, mock_site_path, mock_mkdir, mock_logger, mock_sys_path
):
    # Arrange
    root_names = {'Package One': 'package1'}
    link = True
    level = 3
    toc = True
    mock_loader.return_value = "Generated API documentation"
    mock_site_path.return_value = "/site/path"

    # Act
    result = gen_api(root_names, link=link, level=level, toc=toc)

    # Assert
    assert len(result) == 1
    expected_doc = "### Package One API\n\nGenerated API documentation"
    assert expected_doc in result
    mock_loader.assert_called_once_with('package1', "/site/path", True, 3, True)
    path = join('docs', "package1-api.md")
    mock_write.assert_called_once_with(path, expected_doc)

@patch('apimd.loader.sys_path')
@patch('apimd.loader.logger')
@patch('apimd.loader.mkdir')
@patch('apimd.loader._site_path')
@patch('apimd.loader.loader')
@patch('apimd.loader._write')
def test_gen_api_pwd(
    mock_write, mock_loader, mock_site_path, mock_mkdir, mock_logger, mock_sys_path
):
    # Arrange
    root_names = {'Package One': 'package1'}
    pwd = '/path/to/site-packages'
    mock_loader.return_value = "Generated API documentation"
    mock_site_path.return_value = "/site/path"

    # Act
    result = gen_api(root_names, pwd=pwd)

    # Assert
    assert len(result) == 1
    expected_doc = "# Package One API\n\nGenerated API documentation"
    assert expected_doc in result
    mock_sys_path.append.assert_called_once_with(pwd)
    path = join('docs', "package1-api.md")
    mock_write.assert_called_once_with(path, expected_doc)

@patch('apimd.loader.sys_path')
@patch('apimd.loader.logger')
@patch('apimd.loader.mkdir')
@patch('apimd.loader._site_path')
@patch('apimd.loader.loader')
def test_gen_api_dry(
    mock_loader, mock_site_path, mock_mkdir, mock_logger, mock_sys_path
):
    # Arrange
    root_names = {'Package One': 'package1'}
    dry = True
    mock_loader.return_value = "Generated API documentation"
    mock_site_path.return_value = "/site/path"

    # Act
    result = gen_api(root_names, dry=dry)

    # Assert
    assert len(result) == 1
    expected_doc = "# Package One API\n\nGenerated API documentation"
    assert expected_doc in result
    mock_loader.assert_called_once_with('package1', "/site/path", True, 1, False)
    mock_logger.info.assert_any_call('=' * 12)
    mock_logger.info.assert_any_call(expected_doc)

@patch('apimd.loader.sys_path')
@patch('apimd.loader.logger')
@patch('apimd.loader.mkdir')
@patch('apimd.loader._site_path')
@patch('apimd.loader.loader', return_value="")
def test_gen_api_no_documentation(
    mock_loader, mock_site_path, mock_mkdir, mock_logger, mock_sys_path
):
    # Arrange
    root_names = {'Package One': 'package1'}
    mock_site_path.return_value = "/site/path"

    # Act
    result = gen_api(root_names)

    # Assert
    assert len(result) == 0
    mock_loader.assert_called_once_with('package1', "/site/path", True, 1, False)
    mock_logger.warning.assert_called_once_with("'package1' can not be found")
