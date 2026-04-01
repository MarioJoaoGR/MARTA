
import pytest
from unittest.mock import patch
from isort.main import main as isort_main

@pytest.mark.parametrize("argv, stdin", [
    (None, None),  # Test with no arguments and no standard input
    ([], None),     # Test with an empty list of arguments and no standard input
    (["file1.py"], None),  # Test with a single file argument
    (["--float-to-top", "file1.py"], None),  # Test with specific command line arguments
])
def test_isort_main(argv, stdin):
    with patch('sys.stdin', stdin) if stdin else patch('builtins.input', lambda _: ''):
        isort_main(argv=argv)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

isort/Test4DT_tests/test_isort_main_main_0_test_edge_case.py F.FF        [100%]

=================================== FAILURES ===================================
__________________________ test_isort_main[None-None] __________________________

argv = None, stdin = None

    @pytest.mark.parametrize("argv, stdin", [
        (None, None),  # Test with no arguments and no standard input
        ([], None),     # Test with an empty list of arguments and no standard input
        (["file1.py"], None),  # Test with a single file argument
        (["--float-to-top", "file1.py"], None),  # Test with specific command line arguments
    ])
    def test_isort_main(argv, stdin):
        with patch('sys.stdin', stdin) if stdin else patch('builtins.input', lambda _: ''):
>           isort_main(argv=argv)

isort/Test4DT_tests/test_isort_main_main_0_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/main.py:1062: in main
    arguments = parse_args(argv)
isort/isort/main.py:937: in parse_args
    arguments = {key: value for key, value in vars(parser.parse_args(argv)).items() if value}
/usr/local/lib/python3.11/argparse.py:1877: in parse_args
    self.error(msg % ' '.join(argv))
/usr/local/lib/python3.11/argparse.py:2640: in error
    self.exit(2, _('%(prog)s: error: %(message)s\n') % args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description="Sort Python import definitions alphabetically within logic...upgrade_guides/5.0.0.html", formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=False)
status = 2
message = '__main__.py: error: unrecognized arguments: /dev/null --rootdir /projects/F202407648IACDCF2/mario/isort --json-report --json-report-file=pytest_report.json\n'

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, _sys.stderr)
>       _sys.exit(status)
E       SystemExit: 2

/usr/local/lib/python3.11/argparse.py:2627: SystemExit
----------------------------- Captured stderr call -----------------------------
usage: __main__.py [-h] [-V] [--vn] [-v] [--only-modified] [--dedup-headings]
                   [-q] [-d] [--overwrite-in-place] [--show-config]
                   [--show-files] [--df] [-c] [--ws] [--sp SETTINGS_PATH]
                   [--cr CONFIG_ROOT] [--resolve-all-configs]
                   [--profile PROFILE] [--old-finders] [-j [JOBS]] [--ac]
                   [--interactive] [--format-error FORMAT_ERROR]
                   [--format-success FORMAT_SUCCESS] [--srx] [--filter-files]
                   [-s SKIP] [--extend-skip EXTEND_SKIP] [--sg SKIP_GLOB]
                   [--extend-skip-glob EXTEND_SKIP_GLOB] [--gitignore]
                   [--ext SUPPORTED_EXTENSIONS]
                   [--blocked-extension BLOCKED_EXTENSIONS]
                   [--dont-follow-links] [--filename FILENAME] [--allow-root]
                   [-a ADD_IMPORTS] [--append] [--af] [--rm REMOVE_IMPORTS]
                   [--float-to-top] [--dont-float-to-top] [--ca] [--cs] [-e]
                   [--ff] [--fgw [FORCE_GRID_WRAP]] [-i INDENT]
                   [--lbi LINES_BEFORE_IMPORTS] [--lai LINES_AFTER_IMPORTS]
                   [--lbt LINES_BETWEEN_TYPES] [--le LINE_ENDING] [--ls]
                   [--lss]
                   [-m {GRID,VERTICAL,HANGING_INDENT,VERTICAL_HANGING_INDENT,VERTICAL_GRID,VERTICAL_GRID_GROUPED,VERTICAL_GRID_GROUPED_NO_COMMA,NOQA,VERTICAL_HANGING_INDENT_BRACKET,VERTICAL_PREFIX_FROM_MODULE_IMPORT,HANGING_INDENT_WITH_PARENTHESES,BACKSLASH_GRID,0,1,2,3,4,5,6,7,8,9,10,11}]
                   [-n] [--nis] [--ot] [--dt] [--rr] [--reverse-sort]
                   [--sort-order SORT_ORDER] [--sl]
                   [--nsl SINGLE_LINE_EXCLUSIONS] [--tc] [--up]
                   [-l LINE_LENGTH] [--wl WRAP_LENGTH] [--case-sensitive]
                   [--remove-redundant-aliases] [--honor-noqa]
                   [--treat-comment-as-code TREAT_COMMENTS_AS_CODE]
                   [--treat-all-comment-as-code] [--formatter FORMATTER]
                   [--color] [--ext-format EXT_FORMAT] [--star-first]
                   [--split-on-trailing-comma] [--sd DEFAULT_SECTION]
                   [--only-sections] [--ds] [--fas] [--fss] [--hcss] [--srss]
                   [--fass] [-t FORCE_TO_TOP] [--combine-straight-imports]
                   [--nlb NO_LINES_BEFORE] [--src SRC_PATHS]
                   [-b KNOWN_STANDARD_LIBRARY]
                   [--extra-builtin EXTRA_STANDARD_LIBRARY]
                   [-f KNOWN_FUTURE_LIBRARY] [-o KNOWN_THIRD_PARTY]
                   [-p KNOWN_FIRST_PARTY]
                   [--known-local-folder KNOWN_LOCAL_FOLDER]
                   [--virtual-env VIRTUAL_ENV] [--conda-env CONDA_ENV]
                   [--py {all,2,27,3,310,311,312,313,314,36,37,38,39,auto}]
                   [files ...]
__main__.py: error: unrecognized arguments: /dev/null --rootdir /projects/F202407648IACDCF2/mario/isort --json-report --json-report-file=pytest_report.json
_________________________ test_isort_main[argv2-None] __________________________

argv = ['file1.py'], stdin = None

    @pytest.mark.parametrize("argv, stdin", [
        (None, None),  # Test with no arguments and no standard input
        ([], None),     # Test with an empty list of arguments and no standard input
        (["file1.py"], None),  # Test with a single file argument
        (["--float-to-top", "file1.py"], None),  # Test with specific command line arguments
    ])
    def test_isort_main(argv, stdin):
        with patch('sys.stdin', stdin) if stdin else patch('builtins.input', lambda _: ''):
>           isort_main(argv=argv)

isort/Test4DT_tests/test_isort_main_main_0_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

argv = ['file1.py'], stdin = None

    def main(argv: Sequence[str] | None = None, stdin: TextIOWrapper | None = None) -> None:
        arguments = parse_args(argv)
        if arguments.get("show_version"):
            print(ASCII_ART)
            return
    
        show_config: bool = arguments.pop("show_config", False)
        show_files: bool = arguments.pop("show_files", False)
        if show_config and show_files:
            sys.exit("Error: either specify show-config or show-files not both.")
    
        if "settings_path" in arguments:
            if os.path.isfile(arguments["settings_path"]):
                arguments["settings_file"] = os.path.abspath(arguments["settings_path"])
                arguments["settings_path"] = os.path.dirname(arguments["settings_file"])
            else:
                arguments["settings_path"] = os.path.abspath(arguments["settings_path"])
    
        if "virtual_env" in arguments:
            venv = arguments["virtual_env"]
            arguments["virtual_env"] = os.path.abspath(venv)
            if not os.path.isdir(arguments["virtual_env"]):
                warn(f"virtual_env dir does not exist: {arguments['virtual_env']}", stacklevel=2)
    
        file_names = arguments.pop("files", [])
        if not file_names and not show_config:
            print(QUICK_GUIDE)
            if arguments:
                sys.exit("Error: arguments passed in without any paths or content.")
            return
        if "settings_path" not in arguments:
            arguments["settings_path"] = (
                arguments.get("filename", None) or os.getcwd()
                if file_names == ["-"]
                else os.path.abspath(file_names[0] if file_names else ".")
            )
            if not os.path.isdir(arguments["settings_path"]):
                arguments["settings_path"] = os.path.dirname(arguments["settings_path"])
    
        config_dict = arguments.copy()
        ask_to_apply = config_dict.pop("ask_to_apply", False)
        jobs = config_dict.pop("jobs", None)
        check = config_dict.pop("check", False)
        show_diff = config_dict.pop("show_diff", False)
        write_to_stdout = config_dict.pop("write_to_stdout", False)
        deprecated_flags = config_dict.pop("deprecated_flags", False)
        remapped_deprecated_args = config_dict.pop("remapped_deprecated_args", False)
        stream_filename = config_dict.pop("filename", None)
        ext_format = config_dict.pop("ext_format", None)
        allow_root = config_dict.pop("allow_root", None)
        resolve_all_configs = config_dict.pop("resolve_all_configs", False)
        wrong_sorted_files = False
        all_attempt_broken = False
        no_valid_encodings = False
    
        config_trie: Trie | None = None
        if resolve_all_configs:
            config_trie = find_all_configs(config_dict.pop("config_root", "."))
    
        if "src_paths" in config_dict:
            config_dict["src_paths"] = {
                Path(src_path).resolve() for src_path in config_dict.get("src_paths", ())
            }
    
        config = Config(**config_dict)
        if show_config:
            print(json.dumps(config.__dict__, indent=4, separators=(",", ": "), default=_preconvert))
            return
        if file_names == ["-"]:
            file_path = Path(stream_filename) if stream_filename else None
            if show_files:
                sys.exit("Error: can't show files for streaming input.")
    
            input_stream = sys.stdin if stdin is None else stdin
            if check:
                incorrectly_sorted = not api.check_stream(
                    input_stream=input_stream,
                    config=config,
                    show_diff=show_diff,
                    file_path=file_path,
                    extension=ext_format,
                )
    
                wrong_sorted_files = incorrectly_sorted
            else:
                try:
                    api.sort_stream(
                        input_stream=input_stream,
                        output_stream=sys.stdout,
                        config=config,
                        show_diff=show_diff,
                        file_path=file_path,
                        extension=ext_format,
                        raise_on_skip=False,
                    )
                except FileSkipped:
                    sys.stdout.write(input_stream.read())
        elif "/" in file_names and not allow_root:
            printer = create_terminal_printer(
                color=config.color_output, error=config.format_error, success=config.format_success
            )
            printer.error("it is dangerous to operate recursively on '/'")
            printer.error("use --allow-root to override this failsafe")
            sys.exit(1)
        else:
            if stream_filename:
                printer = create_terminal_printer(
                    color=config.color_output, error=config.format_error, success=config.format_success
                )
                printer.error("Filename override is intended only for stream (-) sorting.")
                sys.exit(1)
            skipped: list[str] = []
            broken: list[str] = []
    
            if config.filter_files:
                filtered_files = []
                for file_name in file_names:
                    if config.is_skipped(Path(file_name)):
                        skipped.append(str(Path(file_name).resolve()))
                    else:
                        filtered_files.append(file_name)
                file_names = filtered_files
    
            file_names = files.find(file_names, config, skipped, broken)
            if show_files:
                for file_name in file_names:
                    print(file_name)
                return
            num_skipped = 0
            num_broken = 0
            num_invalid_encoding = 0
            if config.verbose:
                print(ASCII_ART)
    
            if jobs:
                import multiprocessing  # noqa: PLC0415
    
                executor = multiprocessing.Pool(jobs if jobs > 0 else multiprocessing.cpu_count())
                attempt_iterator = executor.imap(
                    functools.partial(
                        sort_imports,
                        config=config,
                        check=check,
                        ask_to_apply=ask_to_apply,
                        show_diff=show_diff,
                        write_to_stdout=write_to_stdout,
                        extension=ext_format,
                        config_trie=config_trie,
                    ),
                    file_names,
                )
            else:
                # https://github.com/python/typeshed/pull/2814
                attempt_iterator = (
                    sort_imports(  # type: ignore
                        file_name,
                        config=config,
                        check=check,
                        ask_to_apply=ask_to_apply,
                        show_diff=show_diff,
                        write_to_stdout=write_to_stdout,
                        extension=ext_format,
                        config_trie=config_trie,
                    )
                    for file_name in file_names
                )
    
            # If any files passed in are missing considered as error, should be removed
            is_no_attempt = True
            any_encoding_valid = False
            for sort_attempt in attempt_iterator:
                if not sort_attempt:
                    continue  # pragma: no cover - shouldn't happen, satisfies type constraint
                incorrectly_sorted = sort_attempt.incorrectly_sorted
                if arguments.get("check", False) and incorrectly_sorted:
                    wrong_sorted_files = True
                if sort_attempt.skipped:
                    num_skipped += (
                        1  # pragma: no cover - shouldn't happen, due to skip in iter_source_code
                    )
    
                if not sort_attempt.supported_encoding:
                    num_invalid_encoding += 1
                else:
                    any_encoding_valid = True
    
                is_no_attempt = False
    
            num_skipped += len(skipped)
            if num_skipped and not config.quiet:
                if config.verbose:
                    for was_skipped in skipped:
                        print(
                            f"{was_skipped} was skipped as it's listed in 'skip' setting, "
                            "matches a glob in 'skip_glob' setting, or is in a .gitignore file with "
                            "--skip-gitignore enabled."
                        )
                print(f"Skipped {num_skipped} files")
    
            num_broken += len(broken)
            if num_broken and not config.quiet:
                if config.verbose:
                    for was_broken in broken:
                        warn(
                            f"{was_broken} was broken path, make sure it exists correctly", stacklevel=2
                        )
                print(f"Broken {num_broken} paths")
    
            if num_broken > 0 and is_no_attempt:
                all_attempt_broken = True
            if num_invalid_encoding > 0 and not any_encoding_valid:
                no_valid_encodings = True
    
        if not config.quiet and (remapped_deprecated_args or deprecated_flags):
            if remapped_deprecated_args:
                warn(
                    "W0502: The following deprecated single dash CLI flags were used and translated: "
                    f"{', '.join(remapped_deprecated_args)}!",
                    stacklevel=2,
                )
            if deprecated_flags:
                warn(
                    "W0501: The following deprecated CLI flags were used and ignored: "
                    f"{', '.join(deprecated_flags)}!",
                    stacklevel=2,
                )
            warn(
                "W0500: Please see the 5.0.0 Upgrade guide: "
                "https://pycqa.github.io/isort/docs/upgrade_guides/5.0.0.html",
                stacklevel=2,
            )
    
        if wrong_sorted_files:
            sys.exit(1)
    
        if all_attempt_broken:
>           sys.exit(1)
E           SystemExit: 1

isort/isort/main.py:1297: SystemExit
----------------------------- Captured stdout call -----------------------------
Broken 1 paths
_________________________ test_isort_main[argv3-None] __________________________

argv = ['--float-to-top', 'file1.py'], stdin = None

    @pytest.mark.parametrize("argv, stdin", [
        (None, None),  # Test with no arguments and no standard input
        ([], None),     # Test with an empty list of arguments and no standard input
        (["file1.py"], None),  # Test with a single file argument
        (["--float-to-top", "file1.py"], None),  # Test with specific command line arguments
    ])
    def test_isort_main(argv, stdin):
        with patch('sys.stdin', stdin) if stdin else patch('builtins.input', lambda _: ''):
>           isort_main(argv=argv)

isort/Test4DT_tests/test_isort_main_main_0_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

argv = ['--float-to-top', 'file1.py'], stdin = None

    def main(argv: Sequence[str] | None = None, stdin: TextIOWrapper | None = None) -> None:
        arguments = parse_args(argv)
        if arguments.get("show_version"):
            print(ASCII_ART)
            return
    
        show_config: bool = arguments.pop("show_config", False)
        show_files: bool = arguments.pop("show_files", False)
        if show_config and show_files:
            sys.exit("Error: either specify show-config or show-files not both.")
    
        if "settings_path" in arguments:
            if os.path.isfile(arguments["settings_path"]):
                arguments["settings_file"] = os.path.abspath(arguments["settings_path"])
                arguments["settings_path"] = os.path.dirname(arguments["settings_file"])
            else:
                arguments["settings_path"] = os.path.abspath(arguments["settings_path"])
    
        if "virtual_env" in arguments:
            venv = arguments["virtual_env"]
            arguments["virtual_env"] = os.path.abspath(venv)
            if not os.path.isdir(arguments["virtual_env"]):
                warn(f"virtual_env dir does not exist: {arguments['virtual_env']}", stacklevel=2)
    
        file_names = arguments.pop("files", [])
        if not file_names and not show_config:
            print(QUICK_GUIDE)
            if arguments:
                sys.exit("Error: arguments passed in without any paths or content.")
            return
        if "settings_path" not in arguments:
            arguments["settings_path"] = (
                arguments.get("filename", None) or os.getcwd()
                if file_names == ["-"]
                else os.path.abspath(file_names[0] if file_names else ".")
            )
            if not os.path.isdir(arguments["settings_path"]):
                arguments["settings_path"] = os.path.dirname(arguments["settings_path"])
    
        config_dict = arguments.copy()
        ask_to_apply = config_dict.pop("ask_to_apply", False)
        jobs = config_dict.pop("jobs", None)
        check = config_dict.pop("check", False)
        show_diff = config_dict.pop("show_diff", False)
        write_to_stdout = config_dict.pop("write_to_stdout", False)
        deprecated_flags = config_dict.pop("deprecated_flags", False)
        remapped_deprecated_args = config_dict.pop("remapped_deprecated_args", False)
        stream_filename = config_dict.pop("filename", None)
        ext_format = config_dict.pop("ext_format", None)
        allow_root = config_dict.pop("allow_root", None)
        resolve_all_configs = config_dict.pop("resolve_all_configs", False)
        wrong_sorted_files = False
        all_attempt_broken = False
        no_valid_encodings = False
    
        config_trie: Trie | None = None
        if resolve_all_configs:
            config_trie = find_all_configs(config_dict.pop("config_root", "."))
    
        if "src_paths" in config_dict:
            config_dict["src_paths"] = {
                Path(src_path).resolve() for src_path in config_dict.get("src_paths", ())
            }
    
        config = Config(**config_dict)
        if show_config:
            print(json.dumps(config.__dict__, indent=4, separators=(",", ": "), default=_preconvert))
            return
        if file_names == ["-"]:
            file_path = Path(stream_filename) if stream_filename else None
            if show_files:
                sys.exit("Error: can't show files for streaming input.")
    
            input_stream = sys.stdin if stdin is None else stdin
            if check:
                incorrectly_sorted = not api.check_stream(
                    input_stream=input_stream,
                    config=config,
                    show_diff=show_diff,
                    file_path=file_path,
                    extension=ext_format,
                )
    
                wrong_sorted_files = incorrectly_sorted
            else:
                try:
                    api.sort_stream(
                        input_stream=input_stream,
                        output_stream=sys.stdout,
                        config=config,
                        show_diff=show_diff,
                        file_path=file_path,
                        extension=ext_format,
                        raise_on_skip=False,
                    )
                except FileSkipped:
                    sys.stdout.write(input_stream.read())
        elif "/" in file_names and not allow_root:
            printer = create_terminal_printer(
                color=config.color_output, error=config.format_error, success=config.format_success
            )
            printer.error("it is dangerous to operate recursively on '/'")
            printer.error("use --allow-root to override this failsafe")
            sys.exit(1)
        else:
            if stream_filename:
                printer = create_terminal_printer(
                    color=config.color_output, error=config.format_error, success=config.format_success
                )
                printer.error("Filename override is intended only for stream (-) sorting.")
                sys.exit(1)
            skipped: list[str] = []
            broken: list[str] = []
    
            if config.filter_files:
                filtered_files = []
                for file_name in file_names:
                    if config.is_skipped(Path(file_name)):
                        skipped.append(str(Path(file_name).resolve()))
                    else:
                        filtered_files.append(file_name)
                file_names = filtered_files
    
            file_names = files.find(file_names, config, skipped, broken)
            if show_files:
                for file_name in file_names:
                    print(file_name)
                return
            num_skipped = 0
            num_broken = 0
            num_invalid_encoding = 0
            if config.verbose:
                print(ASCII_ART)
    
            if jobs:
                import multiprocessing  # noqa: PLC0415
    
                executor = multiprocessing.Pool(jobs if jobs > 0 else multiprocessing.cpu_count())
                attempt_iterator = executor.imap(
                    functools.partial(
                        sort_imports,
                        config=config,
                        check=check,
                        ask_to_apply=ask_to_apply,
                        show_diff=show_diff,
                        write_to_stdout=write_to_stdout,
                        extension=ext_format,
                        config_trie=config_trie,
                    ),
                    file_names,
                )
            else:
                # https://github.com/python/typeshed/pull/2814
                attempt_iterator = (
                    sort_imports(  # type: ignore
                        file_name,
                        config=config,
                        check=check,
                        ask_to_apply=ask_to_apply,
                        show_diff=show_diff,
                        write_to_stdout=write_to_stdout,
                        extension=ext_format,
                        config_trie=config_trie,
                    )
                    for file_name in file_names
                )
    
            # If any files passed in are missing considered as error, should be removed
            is_no_attempt = True
            any_encoding_valid = False
            for sort_attempt in attempt_iterator:
                if not sort_attempt:
                    continue  # pragma: no cover - shouldn't happen, satisfies type constraint
                incorrectly_sorted = sort_attempt.incorrectly_sorted
                if arguments.get("check", False) and incorrectly_sorted:
                    wrong_sorted_files = True
                if sort_attempt.skipped:
                    num_skipped += (
                        1  # pragma: no cover - shouldn't happen, due to skip in iter_source_code
                    )
    
                if not sort_attempt.supported_encoding:
                    num_invalid_encoding += 1
                else:
                    any_encoding_valid = True
    
                is_no_attempt = False
    
            num_skipped += len(skipped)
            if num_skipped and not config.quiet:
                if config.verbose:
                    for was_skipped in skipped:
                        print(
                            f"{was_skipped} was skipped as it's listed in 'skip' setting, "
                            "matches a glob in 'skip_glob' setting, or is in a .gitignore file with "
                            "--skip-gitignore enabled."
                        )
                print(f"Skipped {num_skipped} files")
    
            num_broken += len(broken)
            if num_broken and not config.quiet:
                if config.verbose:
                    for was_broken in broken:
                        warn(
                            f"{was_broken} was broken path, make sure it exists correctly", stacklevel=2
                        )
                print(f"Broken {num_broken} paths")
    
            if num_broken > 0 and is_no_attempt:
                all_attempt_broken = True
            if num_invalid_encoding > 0 and not any_encoding_valid:
                no_valid_encodings = True
    
        if not config.quiet and (remapped_deprecated_args or deprecated_flags):
            if remapped_deprecated_args:
                warn(
                    "W0502: The following deprecated single dash CLI flags were used and translated: "
                    f"{', '.join(remapped_deprecated_args)}!",
                    stacklevel=2,
                )
            if deprecated_flags:
                warn(
                    "W0501: The following deprecated CLI flags were used and ignored: "
                    f"{', '.join(deprecated_flags)}!",
                    stacklevel=2,
                )
            warn(
                "W0500: Please see the 5.0.0 Upgrade guide: "
                "https://pycqa.github.io/isort/docs/upgrade_guides/5.0.0.html",
                stacklevel=2,
            )
    
        if wrong_sorted_files:
            sys.exit(1)
    
        if all_attempt_broken:
>           sys.exit(1)
E           SystemExit: 1

isort/isort/main.py:1297: SystemExit
----------------------------- Captured stdout call -----------------------------
Broken 1 paths
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main_main_0_test_edge_case.py::test_isort_main[None-None]
FAILED isort/Test4DT_tests/test_isort_main_main_0_test_edge_case.py::test_isort_main[argv2-None]
FAILED isort/Test4DT_tests/test_isort_main_main_0_test_edge_case.py::test_isort_main[argv3-None]
========================= 3 failed, 1 passed in 0.26s ==========================
"""