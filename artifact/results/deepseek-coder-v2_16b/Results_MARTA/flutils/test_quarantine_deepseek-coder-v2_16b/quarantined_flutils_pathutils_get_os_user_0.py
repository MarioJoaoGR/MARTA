
import pytest
import getpass
import pwd
from flutils.pathutils import get_os_user




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_username ______________________________

name = 'foo'

    def get_os_user(name: _STR_OR_INT_OR_NONE = None) -> pwd.struct_passwd:
        """Return an user object representing an operating system user.
    
        Args:
            name (:obj:`str` or :obj:`int`, optional): The "login name" or
                ``uid``.  Defaults to the current user's "login name".
        Raises:
            OSError: If the given ``name`` does not exist as a "login
                name" for this operating system.
            OSError: If the given ``name`` is an ``uid`` and it does not
                exist.
    
        :rtype:
            :obj:`struct_passwd <pwd>`
    
            * A tuple like object.
    
        Example:
            >>> from flutils.pathutils import get_os_user
            >>> get_os_user('foo')
            pwd.struct_passwd(pw_name='foo', pw_passwd='********', pw_uid=1001,
            pw_gid=2001, pw_gecos='Foo Bar', pw_dir='/home/foo',
            pw_shell='/usr/local/bin/bash')
        """
        if isinstance(name, int):
            try:
                return pwd.getpwuid(name)
            except KeyError:
                raise OSError(
                    'The given uid: %r, is not a valid uid for this operating '
                    'system.' % name
                )
        if name is None:
            name = getpass.getuser()
        try:
>           return pwd.getpwnam(name)
E           KeyError: "getpwnam(): name not found: 'foo'"

/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/pathutils.py:496: KeyError

During handling of the above exception, another exception occurred:

    def test_valid_username():
>       user = get_os_user('foo')

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = 'foo'

    def get_os_user(name: _STR_OR_INT_OR_NONE = None) -> pwd.struct_passwd:
        """Return an user object representing an operating system user.
    
        Args:
            name (:obj:`str` or :obj:`int`, optional): The "login name" or
                ``uid``.  Defaults to the current user's "login name".
        Raises:
            OSError: If the given ``name`` does not exist as a "login
                name" for this operating system.
            OSError: If the given ``name`` is an ``uid`` and it does not
                exist.
    
        :rtype:
            :obj:`struct_passwd <pwd>`
    
            * A tuple like object.
    
        Example:
            >>> from flutils.pathutils import get_os_user
            >>> get_os_user('foo')
            pwd.struct_passwd(pw_name='foo', pw_passwd='********', pw_uid=1001,
            pw_gid=2001, pw_gecos='Foo Bar', pw_dir='/home/foo',
            pw_shell='/usr/local/bin/bash')
        """
        if isinstance(name, int):
            try:
                return pwd.getpwuid(name)
            except KeyError:
                raise OSError(
                    'The given uid: %r, is not a valid uid for this operating '
                    'system.' % name
                )
        if name is None:
            name = getpass.getuser()
        try:
            return pwd.getpwnam(name)
        except KeyError:
>           raise OSError(
                'The given name: %r, is not a valid "login name" '
                'for this operating system.' % name
            )
E           OSError: The given name: 'foo', is not a valid "login name" for this operating system.

/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/pathutils.py:498: OSError
________________________________ test_valid_uid ________________________________

name = 1001

    def get_os_user(name: _STR_OR_INT_OR_NONE = None) -> pwd.struct_passwd:
        """Return an user object representing an operating system user.
    
        Args:
            name (:obj:`str` or :obj:`int`, optional): The "login name" or
                ``uid``.  Defaults to the current user's "login name".
        Raises:
            OSError: If the given ``name`` does not exist as a "login
                name" for this operating system.
            OSError: If the given ``name`` is an ``uid`` and it does not
                exist.
    
        :rtype:
            :obj:`struct_passwd <pwd>`
    
            * A tuple like object.
    
        Example:
            >>> from flutils.pathutils import get_os_user
            >>> get_os_user('foo')
            pwd.struct_passwd(pw_name='foo', pw_passwd='********', pw_uid=1001,
            pw_gid=2001, pw_gecos='Foo Bar', pw_dir='/home/foo',
            pw_shell='/usr/local/bin/bash')
        """
        if isinstance(name, int):
            try:
>               return pwd.getpwuid(name)
E               KeyError: 'getpwuid(): uid not found: 1001'

/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/pathutils.py:487: KeyError

During handling of the above exception, another exception occurred:

    def test_valid_uid():
        uid = 1001
>       user = get_os_user(uid)

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = 1001

    def get_os_user(name: _STR_OR_INT_OR_NONE = None) -> pwd.struct_passwd:
        """Return an user object representing an operating system user.
    
        Args:
            name (:obj:`str` or :obj:`int`, optional): The "login name" or
                ``uid``.  Defaults to the current user's "login name".
        Raises:
            OSError: If the given ``name`` does not exist as a "login
                name" for this operating system.
            OSError: If the given ``name`` is an ``uid`` and it does not
                exist.
    
        :rtype:
            :obj:`struct_passwd <pwd>`
    
            * A tuple like object.
    
        Example:
            >>> from flutils.pathutils import get_os_user
            >>> get_os_user('foo')
            pwd.struct_passwd(pw_name='foo', pw_passwd='********', pw_uid=1001,
            pw_gid=2001, pw_gecos='Foo Bar', pw_dir='/home/foo',
            pw_shell='/usr/local/bin/bash')
        """
        if isinstance(name, int):
            try:
                return pwd.getpwuid(name)
            except KeyError:
>               raise OSError(
                    'The given uid: %r, is not a valid uid for this operating '
                    'system.' % name
                )
E               OSError: The given uid: 1001, is not a valid uid for this operating system.

/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/pathutils.py:489: OSError
__________________________ test_default_current_user ___________________________

    def test_default_current_user():
>       with pytest.raises(OSError):
E       Failed: DID NOT RAISE <class 'OSError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py:19: Failed
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(OSError):
E       Failed: DID NOT RAISE <class 'OSError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py:23: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py::test_valid_username
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py::test_valid_uid
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py::test_default_current_user
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_get_os_user_0.py::test_none_input
============================== 4 failed in 0.08s ===============================
"""