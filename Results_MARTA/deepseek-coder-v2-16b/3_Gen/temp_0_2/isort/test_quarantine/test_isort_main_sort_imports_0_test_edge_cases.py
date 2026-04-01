
import pytest
from isort.main import sort_imports
from isort.api import Config
from isort.exceptions import FileSkipped, ISortError, UnsupportedEncoding
from warnings import warn
import sys

@pytest.mark.parametrize("file_name, config, check, ask_to_apply, write_to_stdout, kwargs", [
    ('example.py', Config(), True, False, False, {}),
    ('script.py', Config(sections=["standard_libs", "custom_libs"], float_to_top=True), False, True, False, {}),
    ('another_file.py', Config(), False, False, True, {})
])
def test_sort_imports(file_name, config, check, ask_to_apply, write_to_stdout, kwargs):
    result = sort_imports(file_name, config, check=check, ask_to_apply=ask_to_apply, write_to_stdout=write_to_stdout, **kwargs)
    
    if check:
        assert isinstance(result, SortAttempt)
        if file_name == 'example.py':
            assert result.incorrectly_sorted is True
            assert result.skipped is False
        elif file_name == 'script.py':
            assert result.incorrectly_sorted is True
            assert result.skipped is False
        else:
            assert result.incorrectly_sorted is not None
            assert result.skipped is not None
    else:
        if file_name == 'another_file.py' and write_to_stdout:
            # Assuming the function writes to stdout correctly for this test
            pass
        else:
            assert result is None or isinstance(result, SortAttempt)

class SortAttempt:
    def __init__(self, incorrectly_sorted, skipped, success):
        self.incorrectly_sorted = incorrectly_sorted
        self.skipped = skipped
        self.success = success

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py FF [ 66%]
.                                                                        [100%]

=================================== FAILURES ===================================
________ test_sort_imports[example.py-config0-True-False-False-kwargs0] ________

file_name = 'example.py'
config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.bzr', '.eggs', '.svn', '.hg', 'dist', 'buck-out',...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
check = True, ask_to_apply = False, write_to_stdout = False, kwargs = {}

    @pytest.mark.parametrize("file_name, config, check, ask_to_apply, write_to_stdout, kwargs", [
        ('example.py', Config(), True, False, False, {}),
        ('script.py', Config(sections=["standard_libs", "custom_libs"], float_to_top=True), False, True, False, {}),
        ('another_file.py', Config(), False, False, True, {})
    ])
    def test_sort_imports(file_name, config, check, ask_to_apply, write_to_stdout, kwargs):
        result = sort_imports(file_name, config, check=check, ask_to_apply=ask_to_apply, write_to_stdout=write_to_stdout, **kwargs)
    
        if check:
>           assert isinstance(result, SortAttempt)
E           assert False
E            +  where False = isinstance(None, SortAttempt)

isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py:18: AssertionError
________ test_sort_imports[script.py-config1-False-True-False-kwargs1] _________

file_name = 'script.py'
config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.bzr', '.eggs', '.svn', '.hg', 'dist', 'buck-out',...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
check = False, ask_to_apply = True, write_to_stdout = False, kwargs = {}
incorrectly_sorted = False, skipped = False

    def sort_imports(
        file_name: str,
        config: Config,
        check: bool = False,
        ask_to_apply: bool = False,
        write_to_stdout: bool = False,
        **kwargs: Any,
    ) -> SortAttempt | None:
        incorrectly_sorted: bool = False
        skipped: bool = False
        try:
            if check:
                try:
                    incorrectly_sorted = not api.check_file(file_name, config=config, **kwargs)
                except FileSkipped:
                    skipped = True
                return SortAttempt(incorrectly_sorted, skipped, True)
    
            try:
>               incorrectly_sorted = not api.sort_file(
                    file_name,
                    config=config,
                    ask_to_apply=ask_to_apply,
                    write_to_stdout=write_to_stdout,
                    **kwargs,
                )

isort/isort/main.py:95: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/api.py:435: in sort_file
    changed = sort_stream(
isort/isort/api.py:212: in sort_stream
    changed = core.process(
isort/isort/core.py:101: in process
    parsed = parse.file_contents(current, config=config)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

contents = '# isort: skip\nimport os\nimport sys\nprint("Hello, World!")'
config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.bzr', '.eggs', '.svn', '.hg', 'dist', 'buck-out',...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

    def file_contents(contents: str, config: Config = DEFAULT_CONFIG) -> ParsedContent:
        """Parses a python file taking out and categorizing imports."""
        line_separator: str = config.line_ending or _infer_line_separator(contents)
        in_lines = contents.splitlines()
        if contents and contents[-1] in ("\n", "\r"):
            in_lines.append("")
    
        out_lines = []
        original_line_count = len(in_lines)
        if config.old_finders:
            from .deprecated.finders import FindersManager  # noqa: PLC0415
    
            finder = FindersManager(config=config).find
        else:
            finder = partial(place.module, config=config)
    
        line_count = len(in_lines)
    
        place_imports: dict[str, list[str]] = {}
        import_placements: dict[str, str] = {}
        as_map: dict[str, dict[str, list[str]]] = {
            "straight": defaultdict(list),
            "from": defaultdict(list),
        }
        imports: OrderedDict[str, dict[str, Any]] = OrderedDict()
        verbose_output: list[str] = []
    
        for section in chain(config.sections, config.forced_separate):
            imports[section] = {"straight": OrderedDict(), "from": OrderedDict()}
        categorized_comments: CommentsDict = {
            "from": {},
            "straight": {},
            "nested": {},
            "above": {"straight": {}, "from": {}},
        }
    
        trailing_commas: set[str] = set()
    
        index = 0
        import_index = -1
        in_quote = ""
        while index < line_count:
            line = in_lines[index]
            index += 1
            statement_index = index
            (skipping_line, in_quote) = skip_line(
                line, in_quote=in_quote, index=index, section_comments=config.section_comments
            )
    
            if (
                line in config.section_comments or line in config.section_comments_end
            ) and not skipping_line:
                if import_index == -1:  # pragma: no branch
                    import_index = index - 1
                continue
    
            if "isort:imports-" in line and line.startswith("#"):
                section = line.split("isort:imports-")[-1].split()[0].upper()
                place_imports[section] = []
                import_placements[line] = section
            elif "isort: imports-" in line and line.startswith("#"):
                section = line.split("isort: imports-")[-1].split()[0].upper()
                place_imports[section] = []
                import_placements[line] = section
    
            if skipping_line:
                out_lines.append(line)
                continue
    
            lstripped_line = line.lstrip()
            if (
                config.float_to_top
                and import_index == -1
                and line
                and not in_quote
                and not lstripped_line.startswith("#")
                and not lstripped_line.startswith("'''")
                and not lstripped_line.startswith('"""')
            ):
                if not lstripped_line.startswith("import") and not lstripped_line.startswith("from"):
                    import_index = index - 1
                    while import_index and not in_lines[import_index - 1]:
                        import_index -= 1
                else:
                    commentless = line.split("#", 1)[0].strip()
                    if (
                        ("isort:skip" in line or "isort: skip" in line)
                        and "(" in commentless
                        and ")" not in commentless
                    ):
                        import_index = index
    
                        starting_line = line
                        while "isort:skip" in starting_line or "isort: skip" in starting_line:
                            commentless = starting_line.split("#", 1)[0]
                            if (
                                "(" in commentless
                                and not commentless.rstrip().endswith(")")
                                and import_index < line_count
                            ):
                                while import_index < line_count and not commentless.rstrip().endswith(
                                    ")"
                                ):
                                    commentless = in_lines[import_index].split("#", 1)[0]
                                    import_index += 1
                            else:
                                import_index += 1
    
                            if import_index >= line_count:
                                break
    
                            starting_line = in_lines[import_index]
    
            line, *end_of_line_comment = line.split("#", 1)
            if ";" in line:
                statements = [line.strip() for line in line.split(";")]
            else:
                statements = [line]
            if end_of_line_comment:
                statements[-1] = f"{statements[-1]}#{end_of_line_comment[0]}"
    
            for statement in statements:
                line, raw_line = normalize_line(statement)
                type_of_import = import_type(line, config) or ""
                raw_lines = [raw_line]
                if not type_of_import:
                    out_lines.append(raw_line)
                    continue
    
                if import_index == -1:
                    import_index = index - 1
                nested_comments = {}
                import_string, comment = parse_comments(line)
                comments = [comment] if comment else []
                line_parts = [part for part in strip_syntax(import_string).strip().split(" ") if part]
                if type_of_import == "from" and len(line_parts) == 2 and comments:
                    nested_comments[line_parts[-1]] = comments[0]
    
                if "(" in line.split("#", 1)[0] and index < line_count:
                    while not line.split("#")[0].strip().endswith(")") and index < line_count:
                        line, new_comment = parse_comments(in_lines[index])
                        index += 1
                        if new_comment:
                            comments.append(new_comment)
                        stripped_line = strip_syntax(line).strip()
                        if (
                            type_of_import == "from"
                            and stripped_line
                            and " " not in stripped_line.replace(" as ", "")
                            and new_comment
                        ):
                            nested_comments[stripped_line] = comments[-1]
                        import_string += line_separator + line
                        raw_lines.append(line)
                else:
                    while line.strip().endswith("\\"):
                        line, new_comment = parse_comments(in_lines[index])
                        line = line.lstrip()
                        index += 1
                        if new_comment:
                            comments.append(new_comment)
    
                        # Still need to check for parentheses after an escaped line
                        if (
                            "(" in line.split("#")[0]
                            and ")" not in line.split("#")[0]
                            and index < line_count
                        ):
                            stripped_line = strip_syntax(line).strip()
                            if (
                                type_of_import == "from"
                                and stripped_line
                                and " " not in stripped_line.replace(" as ", "")
                                and new_comment
                            ):
                                nested_comments[stripped_line] = comments[-1]
                            import_string += line_separator + line
                            raw_lines.append(line)
    
                            while not line.split("#")[0].strip().endswith(")") and index < line_count:
                                line, new_comment = parse_comments(in_lines[index])
                                index += 1
                                if new_comment:
                                    comments.append(new_comment)
                                stripped_line = strip_syntax(line).strip()
                                if (
                                    type_of_import == "from"
                                    and stripped_line
                                    and " " not in stripped_line.replace(" as ", "")
                                    and new_comment
                                ):
                                    nested_comments[stripped_line] = comments[-1]
                                import_string += line_separator + line
                                raw_lines.append(line)
    
                        stripped_line = strip_syntax(line).strip()
                        if (
                            type_of_import == "from"
                            and stripped_line
                            and " " not in stripped_line.replace(" as ", "")
                            and new_comment
                        ):
                            nested_comments[stripped_line] = comments[-1]
                        if import_string.strip().endswith(
                            (" import", " cimport")
                        ) or line.strip().startswith(("import ", "cimport ")):
                            import_string += line_separator + line
                        else:
                            import_string = import_string.rstrip().rstrip("\\") + " " + line.lstrip()
    
                if type_of_import == "from":
                    cimports: bool
                    import_string = (
                        import_string.replace("import(", "import (")
                        .replace("\\", " ")
                        .replace("\n", " ")
                    )
                    if "import " not in import_string:
                        out_lines.extend(raw_lines)
                        continue
    
                    if " cimport " in import_string:
                        parts = import_string.split(" cimport ")
                        cimports = True
    
                    else:
                        parts = import_string.split(" import ")
                        cimports = False
    
                    from_import = parts[0].split(" ")
                    import_string = (" cimport " if cimports else " import ").join(
                        [from_import[0] + " " + "".join(from_import[1:]), *parts[1:]]
                    )
    
                just_imports = [
                    item.replace("{|", "{ ").replace("|}", " }")
                    for item in strip_syntax(import_string).split()
                ]
    
                attach_comments_to: list[Any] | None = None
                direct_imports = just_imports[1:]
                straight_import = True
                top_level_module = ""
                if "as" in just_imports and (just_imports.index("as") + 1) < len(just_imports):
                    straight_import = False
                    while "as" in just_imports:
                        nested_module = None
                        as_index = just_imports.index("as")
                        if type_of_import == "from":
                            nested_module = just_imports[as_index - 1]
                            top_level_module = just_imports[0]
                            module = top_level_module + "." + nested_module
                            as_name = just_imports[as_index + 1]
                            direct_imports.remove(nested_module)
                            direct_imports.remove(as_name)
                            direct_imports.remove("as")
                            if nested_module == as_name and config.remove_redundant_aliases:
                                pass
                            elif as_name not in as_map["from"][module]:  # pragma: no branch
                                as_map["from"][module].append(as_name)
    
                            full_name = f"{nested_module} as {as_name}"
                            associated_comment = nested_comments.get(full_name)
                            if associated_comment:
                                categorized_comments["nested"].setdefault(top_level_module, {})[
                                    full_name
                                ] = associated_comment
                                if associated_comment in comments:  # pragma: no branch
                                    comments.pop(comments.index(associated_comment))
                        else:
                            module = just_imports[as_index - 1]
                            as_name = just_imports[as_index + 1]
                            if module == as_name and config.remove_redundant_aliases:
                                pass
                            elif as_name not in as_map["straight"][module]:
                                as_map["straight"][module].append(as_name)
    
                        if comments and attach_comments_to is None:
                            if nested_module and config.combine_as_imports:
                                attach_comments_to = categorized_comments["from"].setdefault(
                                    f"{top_level_module}.__combined_as__", []
                                )
                            else:
                                if type_of_import == "from" or (
                                    config.remove_redundant_aliases and as_name == module.split(".")[-1]
                                ):
                                    attach_comments_to = categorized_comments["straight"].setdefault(
                                        module, []
                                    )
                                else:
                                    attach_comments_to = categorized_comments["straight"].setdefault(
                                        f"{module} as {as_name}", []
                                    )
                        del just_imports[as_index : as_index + 2]
    
                if type_of_import == "from":
                    import_from = just_imports.pop(0)
                    placed_module = finder(import_from)
                    if config.verbose and not config.only_modified:
                        print(f"from-type place_module for {import_from} returned {placed_module}")
    
                    elif config.verbose:
                        verbose_output.append(
                            f"from-type place_module for {import_from} returned {placed_module}"
                        )
                    if placed_module == "":
                        warn(
                            f"could not place module {import_from} of line {line} --"
                            " Do you need to define a default section?",
                            stacklevel=2,
                        )
    
                    if placed_module and placed_module not in imports:
                        raise MissingSection(import_module=import_from, section=placed_module)
    
                    root = imports[placed_module][type_of_import]  # type: ignore
                    for import_name in just_imports:
                        associated_comment = nested_comments.get(import_name)
                        if associated_comment:
                            categorized_comments["nested"].setdefault(import_from, {})[import_name] = (
                                associated_comment
                            )
                            if associated_comment in comments:  # pragma: no branch
                                comments.pop(comments.index(associated_comment))
                    if (
                        config.force_single_line
                        and comments
                        and attach_comments_to is None
                        and len(just_imports) == 1
                    ):
                        nested_from_comments = categorized_comments["nested"].setdefault(
                            import_from, {}
                        )
                        existing_comment = nested_from_comments.get(just_imports[0], "")
                        nested_from_comments[just_imports[0]] = (
                            f"{existing_comment}{'; ' if existing_comment else ''}{'; '.join(comments)}"
                        )
                        comments = []
    
                    if comments and attach_comments_to is None:
                        attach_comments_to = categorized_comments["from"].setdefault(import_from, [])
    
                    if len(out_lines) > max(import_index, 1) - 1:
                        last = out_lines[-1].rstrip() if out_lines else ""
                        while (
                            last.startswith("#")
                            and not last.endswith('"""')
                            and not last.endswith("'''")
                            and "isort:imports-" not in last
                            and "isort: imports-" not in last
                            and not config.treat_all_comments_as_code
                            and last.strip() not in config.treat_comments_as_code
                        ):
                            categorized_comments["above"]["from"].setdefault(import_from, []).insert(
                                0, out_lines.pop(-1)
                            )
                            if out_lines:
                                last = out_lines[-1].rstrip()
                            else:
                                last = ""
                        if statement_index - 1 == import_index:  # pragma: no cover
                            import_index -= len(
                                categorized_comments["above"]["from"].get(import_from, [])
                            )
    
                    if import_from not in root:
                        root[import_from] = OrderedDict(
                            (module, module in direct_imports) for module in just_imports
                        )
                    else:
                        root[import_from].update(
                            (module, root[import_from].get(module, False) or module in direct_imports)
                            for module in just_imports
                        )
    
                    if comments and attach_comments_to is not None:
                        attach_comments_to.extend(comments)
    
                    if (
                        just_imports
                        and just_imports[-1]
                        and "," in import_string.split(just_imports[-1])[-1]
                    ):
                        trailing_commas.add(import_from)
                else:
                    if comments and attach_comments_to is not None:
                        attach_comments_to.extend(comments)
                        comments = []
    
                    for module in just_imports:
                        if comments:
                            categorized_comments["straight"][module] = comments
                            comments = []
    
                        if len(out_lines) > max(import_index, +1, 1) - 1:
                            last = out_lines[-1].rstrip() if out_lines else ""
                            while (
                                last.startswith("#")
                                and not last.endswith('"""')
                                and not last.endswith("'''")
                                and "isort:imports-" not in last
                                and "isort: imports-" not in last
                                and not config.treat_all_comments_as_code
                                and last.strip() not in config.treat_comments_as_code
                            ):
                                categorized_comments["above"]["straight"].setdefault(module, []).insert(
                                    0, out_lines.pop(-1)
                                )
                                if out_lines:
                                    last = out_lines[-1].rstrip()
                                else:
                                    last = ""
                            if index - 1 == import_index:
                                import_index -= len(
                                    categorized_comments["above"]["straight"].get(module, [])
                                )
                        placed_module = finder(module)
                        if config.verbose and not config.only_modified:
                            print(f"else-type place_module for {module} returned {placed_module}")
    
                        elif config.verbose:
                            verbose_output.append(
                                f"else-type place_module for {module} returned {placed_module}"
                            )
                        if placed_module == "":
                            warn(
                                f"could not place module {module} of line {line} --"
                                " Do you need to define a default section?",
                                stacklevel=2,
                            )
                            imports.setdefault("", {"straight": OrderedDict(), "from": OrderedDict()})
    
                        if placed_module and placed_module not in imports:
>                           raise MissingSection(import_module=module, section=placed_module)
E                           isort.exceptions.MissingSection: Found os import while parsing, but THIRDPARTY was not included in the `sections` setting of your config. Please add it before continuing
E                           See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.

isort/isort/parse.py:577: MissingSection

During handling of the above exception, another exception occurred:

file_name = 'script.py'
config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.bzr', '.eggs', '.svn', '.hg', 'dist', 'buck-out',...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
check = False, ask_to_apply = True, write_to_stdout = False, kwargs = {}

    @pytest.mark.parametrize("file_name, config, check, ask_to_apply, write_to_stdout, kwargs", [
        ('example.py', Config(), True, False, False, {}),
        ('script.py', Config(sections=["standard_libs", "custom_libs"], float_to_top=True), False, True, False, {}),
        ('another_file.py', Config(), False, False, True, {})
    ])
    def test_sort_imports(file_name, config, check, ask_to_apply, write_to_stdout, kwargs):
>       result = sort_imports(file_name, config, check=check, ask_to_apply=ask_to_apply, write_to_stdout=write_to_stdout, **kwargs)

isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_name = 'script.py'
config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.bzr', '.eggs', '.svn', '.hg', 'dist', 'buck-out',...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
check = False, ask_to_apply = True, write_to_stdout = False, kwargs = {}
incorrectly_sorted = False, skipped = False

    def sort_imports(
        file_name: str,
        config: Config,
        check: bool = False,
        ask_to_apply: bool = False,
        write_to_stdout: bool = False,
        **kwargs: Any,
    ) -> SortAttempt | None:
        incorrectly_sorted: bool = False
        skipped: bool = False
        try:
            if check:
                try:
                    incorrectly_sorted = not api.check_file(file_name, config=config, **kwargs)
                except FileSkipped:
                    skipped = True
                return SortAttempt(incorrectly_sorted, skipped, True)
    
            try:
                incorrectly_sorted = not api.sort_file(
                    file_name,
                    config=config,
                    ask_to_apply=ask_to_apply,
                    write_to_stdout=write_to_stdout,
                    **kwargs,
                )
            except FileSkipped:
                skipped = True
            return SortAttempt(incorrectly_sorted, skipped, True)
        except (OSError, ValueError) as error:
            warn(f"Unable to parse file {file_name} due to {error}", stacklevel=2)
            return None
        except UnsupportedEncoding:
            if config.verbose:
                warn(f"Encoding not supported for {file_name}", stacklevel=2)
            return SortAttempt(incorrectly_sorted, skipped, False)
        except ISortError as error:
            _print_hard_fail(config, message=str(error))
>           sys.exit(1)
E           SystemExit: 1

isort/isort/main.py:114: SystemExit
----------------------------- Captured stderr call -----------------------------
ERROR: Found os import while parsing, but THIRDPARTY was not included in the `sections` setting of your config. Please add it before continuing
See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.
=============================== warnings summary ===============================
isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py:11
  /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py:11: UserWarning: `sections` setting includes standard_libs, but no known_standard_libs is defined. The following known_SECTION config options are defined: .
    ('script.py', Config(sections=["standard_libs", "custom_libs"], float_to_top=True), False, True, False, {}),

isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py:11
  /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py:11: UserWarning: `sections` setting includes custom_libs, but no known_custom_libs is defined. The following known_SECTION config options are defined: .
    ('script.py', Config(sections=["standard_libs", "custom_libs"], float_to_top=True), False, True, False, {}),

Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py::test_sort_imports[example.py-config0-True-False-False-kwargs0]
  /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py:15: UserWarning: Unable to parse file example.py due to [Errno 2] No such file or directory: '/projects/F202407648IACDCF2/mario/example.py'
    result = sort_imports(file_name, config, check=check, ask_to_apply=ask_to_apply, write_to_stdout=write_to_stdout, **kwargs)

Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py::test_sort_imports[another_file.py-config2-False-False-True-kwargs2]
  /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py:15: UserWarning: Unable to parse file another_file.py due to [Errno 2] No such file or directory: '/projects/F202407648IACDCF2/mario/another_file.py'
    result = sort_imports(file_name, config, check=check, ask_to_apply=ask_to_apply, write_to_stdout=write_to_stdout, **kwargs)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py::test_sort_imports[example.py-config0-True-False-False-kwargs0]
FAILED isort/Test4DT_tests/test_isort_main_sort_imports_0_test_edge_cases.py::test_sort_imports[script.py-config1-False-True-False-kwargs1]
=================== 2 failed, 1 passed, 4 warnings in 0.20s ====================
"""