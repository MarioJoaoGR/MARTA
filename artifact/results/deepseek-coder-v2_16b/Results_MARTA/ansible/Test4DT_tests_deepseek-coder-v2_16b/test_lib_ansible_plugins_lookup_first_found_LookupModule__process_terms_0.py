
import pytest
from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display_helpers import DisplayHelper

# Assuming the class and method are defined in a module named lookup_module
class LookupModule(LookupBase):
    def __init__(self, *args, **kwargs):
        super(LookupModule, self).__init__(*args, **kwargs)
    
    def _process_terms(self, terms, variables, kwargs):
        total_search = []
        skip = False
        for term in terms:
            if isinstance(term, dict):
                self.set_options(var_options=variables, direct=term)
            elif isinstance(term, str):
                self.set_options(var_options=variables, direct=kwargs)
            else:
                raise AnsibleLookupError("Invalid term supplied, can handle string, mapping or list of strings but got: %s for %s" % (type(term), term))
            
            files = self.get_option('files')
            paths = self.get_option('paths')
            skip = self.get_option('skip')
            filelist = _split_on(files, ',;') if files else []
            pathlist = _split_on(paths, ',:;') if paths else []
            
            for path in pathlist:
                for fn in filelist:
                    f = os.path.join(path, fn)
                    total_search.append(f)
        
        return total_search, skip

# Fixtures and test functions follow below
@pytest.fixture
def lookup_module():
    return LookupModule()

@pytest.fixture
def terms_valid():
    return [{'files': 'file1,file2', 'paths': 'dir1,dir2'}]

@pytest.fixture
def terms_none():
    return [None]

@pytest.fixture
def terms_invalid():
    return ['term1', 'invalid_term']

# Test for valid input with a simple mapping term
def test_valid_input_simple_mapping(lookup_module, terms_valid):
    result, _ = lookup_module._process_terms(terms_valid, {}, {})
    assert result == ['dir1/file1', 'dir1/file2', 'dir2/file1', 'dir2/file2']

# Test for None input to check error handling
def test_edge_case_none_input(lookup_module, terms_none):
    with pytest.raises(AnsibleLookupError) as excinfo:
        lookup_module._process_terms(terms_none, {}, {})
    assert 'Invalid term supplied' in str(excinfo.value)

# Test for invalid term type to check error handling
def test_invalid_input_type(lookup_module, terms_invalid):
    with pytest.raises(AnsibleLookupError) as excinfo:
        lookup_module._process_terms(terms_invalid, {}, {})
    assert 'Invalid term supplied' in str(excinfo.value)
