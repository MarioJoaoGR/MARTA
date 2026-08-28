
import pytest
from unittest.mock import patch
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata
from importlib import import_module
import sys

class _AnsibleInternalRedirectLoader:
    """
    A class to handle internal redirection of module imports for Ansible collections.

    This class is responsible for redirecting the import of modules within a specific Ansible collection, based on predefined metadata. It takes the full name of the module and a list of paths as input parameters. The function checks if the module belongs to the 'ansible' package, retrieves its metadata from the 'ansible.builtin' collection, and then looks up the import redirection information. If a redirect is found, it sets the internal `_redirect` attribute; otherwise, it raises an ImportError.

    Parameters:
        fullname (str): The fully qualified name of the module to be imported, which should include both the namespace and the module name separated by dots.
            For example, 'ansible.network.network_cli' would be a valid `fullname`.
        path_list (list): A list of paths where the module can be located. This parameter is not used in this class but is part of the constructor signature for consistency with other import loaders.

    Raises:
        ImportError: If the specified module does not belong to the 'ansible' package, or if there is no redirection information available.

    Example:
        To redirect the import of a module from the 'ansible.network.network_cli' namespace:
        
        >>> loader = _AnsibleInternalRedirectLoader('ansible.network.network_cli', [])
        This will set up the internal state to handle redirects for the specified module, allowing it to be imported according to its redirection rules defined in the metadata of the 'ansible.builtin' collection.
    """
    def __init__(self, fullname, path_list):
        self._redirect = None

        split_name = fullname.split('.')
        toplevel_pkg = split_name[0]
        module_to_load = split_name[-1]

        if toplevel_pkg != 'ansible':
            raise ImportError('not interested')

        builtin_meta = _get_collection_metadata('ansible.builtin')

        routing_entry = _nested_dict_get(builtin_meta, ['import_redirection', fullname])
        if routing_entry:
            self._redirect = routing_entry.get('redirect')

        if not self._redirect:
            raise ImportError('not redirected, go ask path_hook')

    def load_module(self, fullname):
        # since we're delegating to other loaders, this should only be called for internal redirects where we answered
        # find_module with this loader, in which case we'll just directly import the redirection target, insert it into
        # sys.modules under the name it was requested by, and return the original module.

        # should never see this
        if not self._redirect:
            raise ValueError('no redirect found for {0}'.format(fullname))

        # FIXME: smuggle redirection context, provide warning/error that we tried and failed to redirect
        mod = import_module(self._redirect)
        sys.modules[fullname] = mod
        return mod


def test_invalid_input():
    with pytest.raises(ImportError):
        loader = _AnsibleInternalRedirectLoader('invalid.namespace.module', [])

def test_none_input():
    with pytest.raises(AttributeError):
        loader = _AnsibleInternalRedirectLoader(None, [])