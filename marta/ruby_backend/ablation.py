"""Optional generation ablations. Every default preserves ordinary MARTA."""
from dataclasses import asdict, dataclass

POLICY = "component-removal-v2"

@dataclass(frozen=True)
class AblationOptions:
    no_type_hints: bool = False
    no_method_retrieval: bool = False
    no_coverage_feedback: bool = False
    no_repair: bool = False
    no_planner_retrieval: bool = False
    no_error_retrieval: bool = False
    no_semantic_judge: bool = False

    def as_dict(self):
        return asdict(self)

    @property
    def enabled(self):
        return any(self.as_dict().values())

    @property
    def suffix(self):
        names = [name for name, value in self.as_dict().items() if value]
        return "_" + "_".join(names) if names else ""

    @property
    def planner_retrieval_enabled(self):
        return not (self.no_method_retrieval or self.no_planner_retrieval)

    @property
    def error_retrieval_enabled(self):
        return not (self.no_method_retrieval or self.no_error_retrieval)

    @property
    def method_index_enabled(self):
        return self.planner_retrieval_enabled or self.error_retrieval_enabled

    @property
    def semantic_judge_enabled(self):
        return not (self.no_type_hints or self.no_semantic_judge)

    @property
    def only_coverage_feedback_removed(self):
        return self.no_coverage_feedback and not any(
            value for name, value in self.as_dict().items() if name != "no_coverage_feedback")

    def attempts(self, maximum):
        return 1 if self.no_repair else maximum


def add_arguments(parser, *, underscores=False):
    help_text = {
        "no_type_hints": "Omit parameter-type hints from generation; keep the call-graph type index",
        "no_method_retrieval": "Omit related-method retrieval in planning and repair; keep class-based type hints",
        "no_coverage_feedback": "Keep all rounds but do not guide or skip generation using coverage",
        "no_repair": "One Dev attempt per round; keep syntax/RSpec validation and salvage",
        "no_planner_retrieval": "Omit related-method retrieval only in the Planner",
        "no_error_retrieval": "Omit retrieved method summaries/examples only in repair; keep failure diagnostics",
        "no_semantic_judge": "Omit class-embedding type refinement; keep structural parameter-type hints",
    }
    for name, description in help_text.items():
        flags = ["--" + name.replace("_", "-")]
        if underscores:
            flags.append("--" + name)
        parser.add_argument(*flags, dest=name, action="store_true", help=description)


def from_args(args):
    return AblationOptions(**{name: getattr(args, name, False)
                             for name in AblationOptions.__dataclass_fields__})
