
import os
import tempfile
import shutil
import pytest
from unittest.mock import patch
from zipfile import ZipFile, BadZipFile
from cookiecutter.zipfile import unzip, InvalidZipRepository

# Helper function to create a zip file for testing
def create_zip_file(path, files=None):
    with ZipFile(path, 'w') as zf:
        if files is None:
            files = {'test.txt': b'Test content'}
        for filename, content in files.items():
            zf.writestr(filename, content)

# Helper function to create a password-protected zip file
def create_password_protected_zip_file(path, password):
    with ZipFile(path, 'w') as zf:
        zf.setpassword(password.encode('utf-8'))
        zf.writestr('test.txt', b'Test content')

@pytest.fixture(scope='function')
def temp_dir():
    dir_path = tempfile.mkdtemp()
    yield dir_path
    shutil.rmtree(dir_path)

@pytest.fixture(scope='function')
def local_zip(temp_dir):
    zip_path = os.path.join(temp_dir, 'repo.zip')
    create_zip_file(zip_path)
    return zip_path

@pytest.fixture(scope='function')
def password_protected_local_zip(temp_dir):
    zip_path = os.path.join(temp_dir, 'protected_repo.zip')
    create_password_protected_zip_file(zip_path, 'mysecretpassword')
    return zip_path

@pytest.fixture(scope='function')
def invalid_zip(temp_dir):
    zip_path = os.path.join(temp_dir, 'invalid.zip')
    with open(zip_path, 'wb') as f:
        f.write(b'Invalid content')
    return zip_path

@pytest.fixture(scope='function')
def empty_zip(temp_dir):
    zip_path = os.path.join(temp_dir, 'empty.zip')
    create_zip_file(zip_path, {})
    return zip_path

@pytest.fixture(scope='function')
def no_top_level_zip(temp_dir):
    zip_path = os.path.join(temp_dir, 'no_top_level.zip')
    create_zip_file(zip_path, {'file.txt': b'Test content'})
    return zip_path















"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 15 items

../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py F [  6%]
FFFFFFFFFFFFFF                                                           [100%]

=================================== FAILURES ===================================
_____________________________ test_happy_path_url ______________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f5abc59d570>
temp_dir = '/tmp/tmpkob5x_tn'

    def test_happy_path_url(monkeypatch, temp_dir):
        zip_uri = 'https://example.com/repo.zip'
        local_zip_path = os.path.join(temp_dir, 'repo.zip')
        create_zip_file(local_zip_path)
    
        def mock_get(*args, **kwargs):
            response = requests.Response()
            response.status_code = 200
            with open(local_zip_path, 'rb') as f:
                response._content = f.read()
            return response
    
>       monkeypatch.setattr(requests, 'get', mock_get)
E       NameError: name 'requests' is not defined

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:73: NameError
____________________________ test_happy_path_local _____________________________

local_zip = '/tmp/tmpfb59plrp/repo.zip'

    def test_happy_path_local(local_zip):
>       unzip_path = unzip(local_zip, is_url=False, clone_to_dir=temp_dir, no_input=True)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:78: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/zipfile.py:27: in unzip
    clone_to_dir = os.path.expanduser(clone_to_dir)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = <function temp_dir at 0x7f5abc595cf0>

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
>       path = os.fspath(path)
E       TypeError: expected str, bytes or os.PathLike object, not function

/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:232: TypeError
_________________________ test_password_protected_zip __________________________

password_protected_local_zip = '/tmp/tmpi709gkpj/protected_repo.zip'

    def test_password_protected_zip(password_protected_local_zip):
>       with patch('cookiecutter.utils.read_repo_password', return_value='mysecretpassword'):

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:82: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7f5abc603ee0>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'cookiecutter.utils' from '/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/utils.py'> does not have the attribute 'read_repo_password'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
____________________________ test_invalid_zip_file _____________________________

invalid_zip = '/tmp/tmp_wkhgbkd/invalid.zip'

    def test_invalid_zip_file(invalid_zip):
        with pytest.raises(InvalidZipRepository):
>           unzip(invalid_zip, is_url=False, clone_to_dir=temp_dir, no_input=True)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:88: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/zipfile.py:27: in unzip
    clone_to_dir = os.path.expanduser(clone_to_dir)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = <function temp_dir at 0x7f5abc595cf0>

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
>       path = os.fspath(path)
E       TypeError: expected str, bytes or os.PathLike object, not function

/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:232: TypeError
_____________________________ test_empty_zip_file ______________________________

empty_zip = '/tmp/tmp9wwujvlh/empty.zip'

    def test_empty_zip_file(empty_zip):
        with pytest.raises(InvalidZipRepository):
>           unzip(empty_zip, is_url=False, clone_to_dir=temp_dir, no_input=True)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:92: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/zipfile.py:27: in unzip
    clone_to_dir = os.path.expanduser(clone_to_dir)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = <function temp_dir at 0x7f5abc595cf0>

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
>       path = os.fspath(path)
E       TypeError: expected str, bytes or os.PathLike object, not function

/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:232: TypeError
_________________________ test_no_top_level_directory __________________________

no_top_level_zip = '/tmp/tmppks2pu1z/no_top_level.zip'

    def test_no_top_level_directory(no_top_level_zip):
        with pytest.raises(InvalidZipRepository):
>           unzip(no_top_level_zip, is_url=False, clone_to_dir=temp_dir, no_input=True)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/zipfile.py:27: in unzip
    clone_to_dir = os.path.expanduser(clone_to_dir)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = <function temp_dir at 0x7f5abc595cf0>

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
>       path = os.fspath(path)
E       TypeError: expected str, bytes or os.PathLike object, not function

/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:232: TypeError
____________________________ test_missing_password _____________________________

password_protected_local_zip = '/tmp/tmp3vxd_576/protected_repo.zip'

    def test_missing_password(password_protected_local_zip):
        with pytest.raises(InvalidZipRepository):
>           unzip(password_protected_local_zip, is_url=False, clone_to_dir=temp_dir, no_input=True)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:100: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/zipfile.py:27: in unzip
    clone_to_dir = os.path.expanduser(clone_to_dir)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = <function temp_dir at 0x7f5abc595cf0>

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
>       path = os.fspath(path)
E       TypeError: expected str, bytes or os.PathLike object, not function

/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:232: TypeError
____________________________ test_invalid_password _____________________________

password_protected_local_zip = '/tmp/tmperk3iqd3/protected_repo.zip'

    def test_invalid_password(password_protected_local_zip):
>       with patch('cookiecutter.utils.read_repo_password', return_value='wrongpassword'):

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:103: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7f5abc467190>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'cookiecutter.utils' from '/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/utils.py'> does not have the attribute 'read_repo_password'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
______________________________ test_no_user_input ______________________________

password_protected_local_zip = '/tmp/tmp47b8z76m/protected_repo.zip'

    def test_no_user_input(password_protected_local_zip):
        with pytest.raises(InvalidZipRepository):
>           unzip(password_protected_local_zip, is_url=False, clone_to_dir=temp_dir, no_input=True)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:109: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/zipfile.py:27: in unzip
    clone_to_dir = os.path.expanduser(clone_to_dir)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = <function temp_dir at 0x7f5abc595cf0>

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
>       path = os.fspath(path)
E       TypeError: expected str, bytes or os.PathLike object, not function

/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:232: TypeError
_______________________ test_existing_zip_file_no_delete _______________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f5abc466e30>
temp_dir = '/tmp/tmprkianmk5', local_zip = '/tmp/tmprkianmk5/repo.zip'

    def test_existing_zip_file_no_delete(monkeypatch, temp_dir, local_zip):
        zip_uri = 'https://example.com/repo.zip'
    
        def mock_get(*args, **kwargs):
            response = requests.Response()
            response.status_code = 200
            with open(local_zip, 'rb') as f:
                response._content = f.read()
            return response
    
>       monkeypatch.setattr(requests, 'get', mock_get)
E       NameError: name 'requests' is not defined

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:121: NameError
________________________ test_existing_zip_file_delete _________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f5abc4dff70>
temp_dir = '/tmp/tmpl7cwkoq5', local_zip = '/tmp/tmpl7cwkoq5/repo.zip'

    def test_existing_zip_file_delete(monkeypatch, temp_dir, local_zip):
        zip_uri = 'https://example.com/repo.zip'
    
        def mock_get(*args, **kwargs):
            response = requests.Response()
            response.status_code = 200
            with open(local_zip, 'rb') as f:
                response._content = f.read()
            return response
    
>       monkeypatch.setattr(requests, 'get', mock_get)
E       NameError: name 'requests' is not defined

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:135: NameError
_______________________ test_existing_zip_file_no_prompt _______________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f5abc3b6dd0>
temp_dir = '/tmp/tmp04sywfqn', local_zip = '/tmp/tmp04sywfqn/repo.zip'

    def test_existing_zip_file_no_prompt(monkeypatch, temp_dir, local_zip):
        zip_uri = 'https://example.com/repo.zip'
    
        def mock_get(*args, **kwargs):
            response = requests.Response()
            response.status_code = 200
            with open(local_zip, 'rb') as f:
                response._content = f.read()
            return response
    
>       monkeypatch.setattr(requests, 'get', mock_get)
E       NameError: name 'requests' is not defined

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:149: NameError
_______________________________ test_invalid_uri _______________________________

    def test_invalid_uri():
        zip_uri = 'invalid://example.com/repo.zip'
>       with pytest.raises(requests.exceptions.InvalidURL):
E       NameError: name 'requests' is not defined

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:155: NameError
__________________________ test_missing_clone_to_dir ___________________________

local_zip = '/tmp/tmphdq72ko1/repo.zip'

    def test_missing_clone_to_dir(local_zip):
        with pytest.raises(InvalidZipRepository):
>           unzip(local_zip, is_url=False, clone_to_dir=None, no_input=True)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:160: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/zipfile.py:27: in unzip
    clone_to_dir = os.path.expanduser(clone_to_dir)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = None

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
>       path = os.fspath(path)
E       TypeError: expected str, bytes or os.PathLike object, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:232: TypeError
__________________________ test_invalid_clone_to_dir ___________________________

local_zip = '/tmp/tmpstmsjqlk/repo.zip'

    def test_invalid_clone_to_dir(local_zip):
        invalid_path = '/invalid/path'
        with pytest.raises((PermissionError, FileNotFoundError)):
>           unzip(local_zip, is_url=False, clone_to_dir=invalid_path, no_input=True)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py:165: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

zip_uri = '/tmp/tmpstmsjqlk/repo.zip', is_url = False
clone_to_dir = '/invalid/path', no_input = True, password = None

    def unzip(zip_uri, is_url, clone_to_dir='.', no_input=False, password=None):
        """Download and unpack a zipfile at a given URI.
    
        This will download the zipfile to the cookiecutter repository,
        and unpack into a temporary directory.
    
        :param zip_uri: The URI for the zipfile.
        :param is_url: Is the zip URI a URL or a file?
        :param clone_to_dir: The cookiecutter repository directory
            to put the archive into.
        :param no_input: Suppress any prompts
        :param password: The password to use when unpacking the repository.
        """
        # Ensure that clone_to_dir exists
        clone_to_dir = os.path.expanduser(clone_to_dir)
        make_sure_path_exists(clone_to_dir)
    
        if is_url:
            # Build the name of the cached zipfile,
            # and prompt to delete if it already exists.
            identifier = zip_uri.rsplit('/', 1)[1]
            zip_path = os.path.join(clone_to_dir, identifier)
    
            if os.path.exists(zip_path):
                download = prompt_and_delete(zip_path, no_input=no_input)
            else:
                download = True
    
            if download:
                # (Re) download the zipfile
                r = requests.get(zip_uri, stream=True)
                with open(zip_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
        else:
            # Just use the local zipfile as-is.
            zip_path = os.path.abspath(zip_uri)
    
        # Now unpack the repository. The zipfile will be unpacked
        # into a temporary directory
        try:
            zip_file = ZipFile(zip_path)
    
            if len(zip_file.namelist()) == 0:
                raise InvalidZipRepository('Zip repository {} is empty'.format(zip_uri))
    
            # The first record in the zipfile should be the directory entry for
            # the archive. If it isn't a directory, there's a problem.
            first_filename = zip_file.namelist()[0]
            if not first_filename.endswith('/'):
>               raise InvalidZipRepository(
                    'Zip repository {} does not include '
                    'a top-level directory'.format(zip_uri)
                )
E               cookiecutter.exceptions.InvalidZipRepository: Zip repository /tmp/tmpstmsjqlk/repo.zip does not include a top-level directory

/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/zipfile.py:64: InvalidZipRepository
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_happy_path_url
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_happy_path_local
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_password_protected_zip
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_invalid_zip_file
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_empty_zip_file
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_no_top_level_directory
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_missing_password
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_invalid_password
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_no_user_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_existing_zip_file_no_delete
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_existing_zip_file_delete
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_existing_zip_file_no_prompt
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_invalid_uri
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_missing_clone_to_dir
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_zipfile_unzip_0.py::test_invalid_clone_to_dir
============================== 15 failed in 0.36s ==============================
"""