
import pytest
from docstring_parser.google import GoogleParser, Section







"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 7 items

../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py F [ 14%]
FFFFFF                                                                   [100%]

=================================== FAILURES ===================================
___________________ test_parse_custom_sections_without_colon ___________________

    def test_parse_custom_sections_without_colon():
        parser = GoogleParser(
            sections=[
                Section(title="Introduction", key="introduction", type="singular"),
                Section(title="Conclusion", key="conclusion", type="singular")
            ],
            title_colon=False
        )
        docstring_text_custom = """
        Introduction
            This is the introduction section.
    
        Conclusion
            This is the conclusion section.
        """
>       parsed_doc_custom = parser.parse(docstring_text_custom)

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:264: in parse
    ret.meta.append(self._build_meta(part, title))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <docstring_parser.google.GoogleParser object at 0x7f89bc611ed0>
text = 'This is the introduction section.', title = 'Introduction'

    def _build_meta(self, text: str, title: str) -> DocstringMeta:
        """Build docstring element.
    
        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """
    
        section = self.sections[title]
    
        if (
            section.type == SectionType.SINGULAR_OR_MULTIPLE
            and not MULTIPLE_PATTERN.match(text)
        ) or section.type == SectionType.SINGULAR:
            return self._build_single_meta(section, text)
    
        # Split spec and description
>       before, desc = text.split(":", 1)
E       ValueError: not enough values to unpack (expected 2, got 1)

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:106: ValueError
____________________________ test_parse_with_colon _____________________________

    def test_parse_with_colon():
        parser = GoogleParser(
            sections=[
                Section(title="Introduction", key="introduction", type="singular"),
                Section(title="Conclusion", key="conclusion", type="singular")
            ],
            title_colon=True
        )
        docstring_text_custom = """
        Introduction:
            This is the introduction section.
    
        Conclusion:
            This is the conclusion section.
        """
>       parsed_doc_custom = parser.parse(docstring_text_custom)

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:264: in parse
    ret.meta.append(self._build_meta(part, title))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <docstring_parser.google.GoogleParser object at 0x7f89bc48bca0>
text = 'This is the introduction section.', title = 'Introduction'

    def _build_meta(self, text: str, title: str) -> DocstringMeta:
        """Build docstring element.
    
        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """
    
        section = self.sections[title]
    
        if (
            section.type == SectionType.SINGULAR_OR_MULTIPLE
            and not MULTIPLE_PATTERN.match(text)
        ) or section.type == SectionType.SINGULAR:
            return self._build_single_meta(section, text)
    
        # Split spec and description
>       before, desc = text.split(":", 1)
E       ValueError: not enough values to unpack (expected 2, got 1)

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:106: ValueError
__________________ test_parse_with_short_and_long_description __________________

    def test_parse_with_short_and_long_description():
        parser = GoogleParser(
            sections=[
                Section(title="Introduction", key="introduction", type="singular"),
                Section(title="Conclusion", key="conclusion", type="singular")
            ],
            title_colon=True
        )
        docstring_text_custom = """
        Short description.
    
        Long description that explains in more detail what the function does.
    
        Introduction:
            This is the introduction section.
    
        Conclusion:
            This is the conclusion section.
        """
>       parsed_doc_custom = parser.parse(docstring_text_custom)

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py:64: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:264: in parse
    ret.meta.append(self._build_meta(part, title))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <docstring_parser.google.GoogleParser object at 0x7f89bc613160>
text = 'This is the introduction section.', title = 'Introduction'

    def _build_meta(self, text: str, title: str) -> DocstringMeta:
        """Build docstring element.
    
        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """
    
        section = self.sections[title]
    
        if (
            section.type == SectionType.SINGULAR_OR_MULTIPLE
            and not MULTIPLE_PATTERN.match(text)
        ) or section.type == SectionType.SINGULAR:
            return self._build_single_meta(section, text)
    
        # Split spec and description
>       before, desc = text.split(":", 1)
E       ValueError: not enough values to unpack (expected 2, got 1)

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:106: ValueError
________________ test_parse_with_no_colon_and_multiple_sections ________________

    def test_parse_with_no_colon_and_multiple_sections():
        parser = GoogleParser(
            sections=[
                Section(title="Introduction", key="introduction", type="singular"),
                Section(title="Conclusion", key="conclusion", type="singular")
            ],
            title_colon=False
        )
        docstring_text_custom = """
        Introduction
            This is the introduction section.
    
        Conclusion
            This is the conclusion section.
        """
>       parsed_doc_custom = parser.parse(docstring_text_custom)

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py:86: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:264: in parse
    ret.meta.append(self._build_meta(part, title))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <docstring_parser.google.GoogleParser object at 0x7f89bc71bcd0>
text = 'This is the introduction section.', title = 'Introduction'

    def _build_meta(self, text: str, title: str) -> DocstringMeta:
        """Build docstring element.
    
        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """
    
        section = self.sections[title]
    
        if (
            section.type == SectionType.SINGULAR_OR_MULTIPLE
            and not MULTIPLE_PATTERN.match(text)
        ) or section.type == SectionType.SINGULAR:
            return self._build_single_meta(section, text)
    
        # Split spec and description
>       before, desc = text.split(":", 1)
E       ValueError: not enough values to unpack (expected 2, got 1)

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:106: ValueError
_________________ test_parse_with_colon_and_multiple_sections __________________

    def test_parse_with_colon_and_multiple_sections():
        parser = GoogleParser(
            sections=[
                Section(title="Introduction", key="introduction", type="singular"),
                Section(title="Conclusion", key="conclusion", type="singular")
            ],
            title_colon=True
        )
        docstring_text_custom = """
        Introduction:
            This is the introduction section.
    
        Conclusion:
            This is the conclusion section.
        """
>       parsed_doc_custom = parser.parse(docstring_text_custom)

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py:106: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:264: in parse
    ret.meta.append(self._build_meta(part, title))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <docstring_parser.google.GoogleParser object at 0x7f89bc5cf700>
text = 'This is the introduction section.', title = 'Introduction'

    def _build_meta(self, text: str, title: str) -> DocstringMeta:
        """Build docstring element.
    
        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """
    
        section = self.sections[title]
    
        if (
            section.type == SectionType.SINGULAR_OR_MULTIPLE
            and not MULTIPLE_PATTERN.match(text)
        ) or section.type == SectionType.SINGULAR:
            return self._build_single_meta(section, text)
    
        # Split spec and description
>       before, desc = text.split(":", 1)
E       ValueError: not enough values to unpack (expected 2, got 1)

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:106: ValueError
_________________ test_parse_with_no_colon_and_single_section __________________

    def test_parse_with_no_colon_and_single_section():
        parser = GoogleParser(
            sections=[
                Section(title="Introduction", key="introduction", type="singular")
            ],
            title_colon=False
        )
        docstring_text_custom = """
        Introduction
            This is the introduction section.
        """
>       parsed_doc_custom = parser.parse(docstring_text_custom)

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py:122: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:264: in parse
    ret.meta.append(self._build_meta(part, title))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <docstring_parser.google.GoogleParser object at 0x7f89bdd9bb20>
text = 'This is the introduction section.', title = 'Introduction'

    def _build_meta(self, text: str, title: str) -> DocstringMeta:
        """Build docstring element.
    
        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """
    
        section = self.sections[title]
    
        if (
            section.type == SectionType.SINGULAR_OR_MULTIPLE
            and not MULTIPLE_PATTERN.match(text)
        ) or section.type == SectionType.SINGULAR:
            return self._build_single_meta(section, text)
    
        # Split spec and description
>       before, desc = text.split(":", 1)
E       ValueError: not enough values to unpack (expected 2, got 1)

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:106: ValueError
___________________ test_parse_with_colon_and_single_section ___________________

    def test_parse_with_colon_and_single_section():
        parser = GoogleParser(
            sections=[
                Section(title="Introduction", key="introduction", type="singular")
            ],
            title_colon=True
        )
        docstring_text_custom = """
        Introduction:
            This is the introduction section.
        """
>       parsed_doc_custom = parser.parse(docstring_text_custom)

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py:137: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:264: in parse
    ret.meta.append(self._build_meta(part, title))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <docstring_parser.google.GoogleParser object at 0x7f89bc48b040>
text = 'This is the introduction section.', title = 'Introduction'

    def _build_meta(self, text: str, title: str) -> DocstringMeta:
        """Build docstring element.
    
        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """
    
        section = self.sections[title]
    
        if (
            section.type == SectionType.SINGULAR_OR_MULTIPLE
            and not MULTIPLE_PATTERN.match(text)
        ) or section.type == SectionType.SINGULAR:
            return self._build_single_meta(section, text)
    
        # Split spec and description
>       before, desc = text.split(":", 1)
E       ValueError: not enough values to unpack (expected 2, got 1)

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/google.py:106: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py::test_parse_custom_sections_without_colon
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py::test_parse_with_colon
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py::test_parse_with_short_and_long_description
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py::test_parse_with_no_colon_and_multiple_sections
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py::test_parse_with_colon_and_multiple_sections
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py::test_parse_with_no_colon_and_single_section
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser_parse_2.py::test_parse_with_colon_and_single_section
============================== 7 failed in 0.12s ===============================
"""