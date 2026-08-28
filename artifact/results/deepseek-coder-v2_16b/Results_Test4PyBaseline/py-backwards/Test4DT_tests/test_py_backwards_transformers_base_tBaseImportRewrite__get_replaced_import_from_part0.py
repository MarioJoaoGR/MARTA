
import ast
from typing import Dict, Tuple
import pytest

class BaseImportRewrite:
    rewrites = []
    
    def _get_replaced_import_from_part(self, node: ast.ImportFrom, alias: ast.alias,
                                       names_to_replace: Dict[str, Tuple[str, str]]) -> ast.ImportFrom:
        """Returns import from statement with changed module or alias."""
        full_name = '{}.{}'.format(node.module, alias.name)
        if full_name in names_to_replace:
            full_name = full_name.replace(names_to_replace[full_name][0],
                                          names_to_replace[full_name][1],
                                          1)
        module_name = '.'.join(full_name.split('.')[:-1])
        name = full_name.split('.')[-1]
        return ast.ImportFrom(
            module=module_name,
            names=[ast.alias(name=name,
                             asname=alias.asname or alias.name)],
            level=node.level)

# Fixture to create a mock AST ImportFrom node and alias for testing
@pytest.fixture
def mock_import_from():
    return ast.parse("from math import sin as s").body[0]

@pytest.fixture
def mock_alias():
    return ast.alias(name='sin', asname='s')

@pytest.fixture
def names_to_replace():
    return {'math': ('m', 'mathematics')}

# Test case to check if the function returns the correct modified AST ImportFrom node
def test__get_replaced_import_from_part(mock_import_from, mock_alias, names_to_replace):
    base_import = BaseImportRewrite()
    modified_node = base_import._get_replaced_import_from_part(mock_import_from, mock_alias, names_to_replace)
    expected_node = ast.parse("from mathematics import s").body[0]
    assert isinstance(modified_node, ast.ImportFrom)