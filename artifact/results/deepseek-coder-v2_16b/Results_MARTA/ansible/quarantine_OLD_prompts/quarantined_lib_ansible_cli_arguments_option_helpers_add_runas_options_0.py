
import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_runas_options, add_runas_prompt_options
import ansible.constants as C

@pytest.fixture(scope="module")
def parser():
    parser = ArgumentParser()
    add_runas_options(parser)
    return parser




def test_default_values(parser):
    args = parser.parse_args([])
    assert not args.become
    assert args.become_method == C.DEFAULT_BECOME_METHOD
    assert args.become_user is None

@pytest.mark.parametrize("arg, expected", [
    ("--become", True),
    (["--become"], True),
])
def test_add_runas_options_with_become(parser, arg, expected):
    with pytest.raises(SystemExit) as e:
        parser.parse_args([arg])
    assert e.type == SystemExit
    args = parser.parse_args([arg])
    assert getattr(args, 'become', False) == expected

@pytest.mark.parametrize("arg, expected", [
    ("--become-method", "sudo"),
    (["--become-method", "sudo"], "sudo"),
])
def test_add_runas_options_with_become_method(parser, arg, expected):
    args = parser.parse_args([arg])
    assert getattr(args, 'become_method', None) == expected

@pytest.mark.parametrize("arg, expected", [
    ("--become-user", "root"),
    (["--become-user", "root"], "root"),
])
def test_add_runas_options_with_become_user(parser, arg, expected):
    args = parser.parse_args([arg])
    assert getattr(args, 'become_user', None) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 7 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py . [ 14%]
FFFFFF                                                                   [100%]

=================================== FAILURES ===================================
______________ test_add_runas_options_with_become[--become-True] _______________

parser = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
arg = '--become', expected = True

    @pytest.mark.parametrize("arg, expected", [
        ("--become", True),
        (["--become"], True),
    ])
    def test_add_runas_options_with_become(parser, arg, expected):
>       with pytest.raises(SystemExit) as e:
E       Failed: DID NOT RAISE <class 'SystemExit'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py:27: Failed
________________ test_add_runas_options_with_become[arg1-True] _________________

parser = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
arg = ['--become'], expected = True

    @pytest.mark.parametrize("arg, expected", [
        ("--become", True),
        (["--become"], True),
    ])
    def test_add_runas_options_with_become(parser, arg, expected):
        with pytest.raises(SystemExit) as e:
>           parser.parse_args([arg])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
args = Namespace(become=False, become_method='sudo', become_user=None, become_ask_pass=False, become_password_file=None)
namespace = None

    def parse_args(self, args=None, namespace=None):
        args, argv = self.parse_known_args(args, namespace)
        if argv:
            msg = _('unrecognized arguments: %s')
>           self.error(msg % ' '.join(argv))
E           TypeError: sequence item 0: expected str instance, list found

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1836: TypeError
_______ test_add_runas_options_with_become_method[--become-method-sudo] ________

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
args = ['--become-method']
namespace = Namespace(become=False, become_method='sudo', become_user=None, become_ask_pass=False, become_password_file=None)

    def parse_known_args(self, args=None, namespace=None):
        if args is None:
            # args default to the system args
            args = _sys.argv[1:]
        else:
            # make sure that args are mutable
            args = list(args)
    
        # default Namespace built from parser defaults
        if namespace is None:
            namespace = Namespace()
    
        # add any action defaults that aren't present
        for action in self._actions:
            if action.dest is not SUPPRESS:
                if not hasattr(namespace, action.dest):
                    if action.default is not SUPPRESS:
                        setattr(namespace, action.dest, action.default)
    
        # add any parser defaults that aren't present
        for dest in self._defaults:
            if not hasattr(namespace, dest):
                setattr(namespace, dest, self._defaults[dest])
    
        # parse the arguments and exit if there are any errors
        if self.exit_on_error:
            try:
>               namespace, args = self._parse_known_args(args, namespace)

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1866: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2079: in _parse_known_args
    start_index = consume_optional(start_index)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2009: in consume_optional
    arg_count = match_argument(action, selected_patterns)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
action = _StoreAction(option_strings=['--become-method'], dest='become_method', nargs=None, const=None, default='sudo', type=No...rivilege escalation method to use (default=sudo), use `ansible-doc -t become -l` to list valid choices.', metavar=None)
arg_strings_pattern = ''

    def _match_argument(self, action, arg_strings_pattern):
        # match the pattern for this action to the arg strings
        nargs_pattern = self._get_nargs_pattern(action)
        match = _re.match(nargs_pattern, arg_strings_pattern)
    
        # raise an exception if we weren't able to find a match
        if match is None:
            nargs_errors = {
                None: _('expected one argument'),
                OPTIONAL: _('expected at most one argument'),
                ONE_OR_MORE: _('expected at least one argument'),
            }
            msg = nargs_errors.get(action.nargs)
            if msg is None:
                msg = ngettext('expected %s argument',
                               'expected %s arguments',
                               action.nargs) % action.nargs
>           raise ArgumentError(action, msg)
E           argparse.ArgumentError: argument --become-method: expected one argument

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2174: ArgumentError

During handling of the above exception, another exception occurred:

parser = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
arg = '--become-method', expected = 'sudo'

    @pytest.mark.parametrize("arg, expected", [
        ("--become-method", "sudo"),
        (["--become-method", "sudo"], "sudo"),
    ])
    def test_add_runas_options_with_become_method(parser, arg, expected):
>       args = parser.parse_args([arg])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1833: in parse_args
    args, argv = self.parse_known_args(args, namespace)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1869: in parse_known_args
    self.error(str(err))
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2594: in error
    self.exit(2, _('%(prog)s: error: %(message)s\n') % args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
status = 2
message = '__main__.py: error: argument --become-method: expected one argument\n'

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, _sys.stderr)
>       _sys.exit(status)
E       SystemExit: 2

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2581: SystemExit
----------------------------- Captured stderr call -----------------------------
usage: __main__.py [-h] [-b] [--become-method BECOME_METHOD]
                   [--become-user BECOME_USER]
                   [-K | --become-password-file BECOME_PASSWORD_FILE]
__main__.py: error: argument --become-method: expected one argument
_____________ test_add_runas_options_with_become_method[arg1-sudo] _____________

parser = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
arg = ['--become-method', 'sudo'], expected = 'sudo'

    @pytest.mark.parametrize("arg, expected", [
        ("--become-method", "sudo"),
        (["--become-method", "sudo"], "sudo"),
    ])
    def test_add_runas_options_with_become_method(parser, arg, expected):
>       args = parser.parse_args([arg])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
args = Namespace(become=False, become_method='sudo', become_user=None, become_ask_pass=False, become_password_file=None)
namespace = None

    def parse_args(self, args=None, namespace=None):
        args, argv = self.parse_known_args(args, namespace)
        if argv:
            msg = _('unrecognized arguments: %s')
>           self.error(msg % ' '.join(argv))
E           TypeError: sequence item 0: expected str instance, list found

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1836: TypeError
_________ test_add_runas_options_with_become_user[--become-user-root] __________

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
args = ['--become-user']
namespace = Namespace(become=False, become_method='sudo', become_user=None, become_ask_pass=False, become_password_file=None)

    def parse_known_args(self, args=None, namespace=None):
        if args is None:
            # args default to the system args
            args = _sys.argv[1:]
        else:
            # make sure that args are mutable
            args = list(args)
    
        # default Namespace built from parser defaults
        if namespace is None:
            namespace = Namespace()
    
        # add any action defaults that aren't present
        for action in self._actions:
            if action.dest is not SUPPRESS:
                if not hasattr(namespace, action.dest):
                    if action.default is not SUPPRESS:
                        setattr(namespace, action.dest, action.default)
    
        # add any parser defaults that aren't present
        for dest in self._defaults:
            if not hasattr(namespace, dest):
                setattr(namespace, dest, self._defaults[dest])
    
        # parse the arguments and exit if there are any errors
        if self.exit_on_error:
            try:
>               namespace, args = self._parse_known_args(args, namespace)

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1866: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2079: in _parse_known_args
    start_index = consume_optional(start_index)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2009: in consume_optional
    arg_count = match_argument(action, selected_patterns)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
action = _StoreAction(option_strings=['--become-user'], dest='become_user', nargs=None, const=None, default=None, type=<class 'str'>, choices=None, required=False, help='run operations as this user (default=root)', metavar=None)
arg_strings_pattern = ''

    def _match_argument(self, action, arg_strings_pattern):
        # match the pattern for this action to the arg strings
        nargs_pattern = self._get_nargs_pattern(action)
        match = _re.match(nargs_pattern, arg_strings_pattern)
    
        # raise an exception if we weren't able to find a match
        if match is None:
            nargs_errors = {
                None: _('expected one argument'),
                OPTIONAL: _('expected at most one argument'),
                ONE_OR_MORE: _('expected at least one argument'),
            }
            msg = nargs_errors.get(action.nargs)
            if msg is None:
                msg = ngettext('expected %s argument',
                               'expected %s arguments',
                               action.nargs) % action.nargs
>           raise ArgumentError(action, msg)
E           argparse.ArgumentError: argument --become-user: expected one argument

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2174: ArgumentError

During handling of the above exception, another exception occurred:

parser = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
arg = '--become-user', expected = 'root'

    @pytest.mark.parametrize("arg, expected", [
        ("--become-user", "root"),
        (["--become-user", "root"], "root"),
    ])
    def test_add_runas_options_with_become_user(parser, arg, expected):
>       args = parser.parse_args([arg])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py:46: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1833: in parse_args
    args, argv = self.parse_known_args(args, namespace)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1869: in parse_known_args
    self.error(str(err))
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2594: in error
    self.exit(2, _('%(prog)s: error: %(message)s\n') % args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
status = 2
message = '__main__.py: error: argument --become-user: expected one argument\n'

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, _sys.stderr)
>       _sys.exit(status)
E       SystemExit: 2

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2581: SystemExit
----------------------------- Captured stderr call -----------------------------
usage: __main__.py [-h] [-b] [--become-method BECOME_METHOD]
                   [--become-user BECOME_USER]
                   [-K | --become-password-file BECOME_PASSWORD_FILE]
__main__.py: error: argument --become-user: expected one argument
______________ test_add_runas_options_with_become_user[arg1-root] ______________

parser = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
arg = ['--become-user', 'root'], expected = 'root'

    @pytest.mark.parametrize("arg, expected", [
        ("--become-user", "root"),
        (["--become-user", "root"], "root"),
    ])
    def test_add_runas_options_with_become_user(parser, arg, expected):
>       args = parser.parse_args([arg])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py:46: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
args = Namespace(become=False, become_method='sudo', become_user=None, become_ask_pass=False, become_password_file=None)
namespace = None

    def parse_args(self, args=None, namespace=None):
        args, argv = self.parse_known_args(args, namespace)
        if argv:
            msg = _('unrecognized arguments: %s')
>           self.error(msg % ' '.join(argv))
E           TypeError: sequence item 0: expected str instance, list found

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1836: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py::test_add_runas_options_with_become[--become-True]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py::test_add_runas_options_with_become[arg1-True]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py::test_add_runas_options_with_become_method[--become-method-sudo]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py::test_add_runas_options_with_become_method[arg1-sudo]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py::test_add_runas_options_with_become_user[--become-user-root]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_0.py::test_add_runas_options_with_become_user[arg1-root]
========================= 6 failed, 1 passed in 0.88s ==========================
"""