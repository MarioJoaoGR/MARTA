"""Optional generation ablations. Every default preserves ordinary MARTA."""
from dataclasses import asdict, dataclass

POLICY = "component-removal-v1"

@dataclass(frozen=True)
class AblationOptions:
    no_type_hints: bool = False
    no_method_retrieval: bool = False
    no_coverage_feedback: bool = False
    no_repair: bool = False

    def as_dict(self):
        return asdict(self)

    @property
    def enabled(self):
        return any(self.as_dict().values())

    @property
    def suffix(self):
        names = [name for name, value in self.as_dict().items() if value]
        return "_" + "_".join(names) if names else ""

    def attempts(self, maximum):
        return 1 if self.no_repair else maximum


def add_arguments(parser, *, underscores=False):
    help_text = {
        "no_type_hints": "Omit parameter-type hints from generation; keep the call-graph type index",
        "no_method_retrieval": "Omit related-method retrieval in planning and repair; keep class-based type hints",
        "no_coverage_feedback": "Keep all rounds but do not guide or skip generation using coverage",
        "no_repair": "One Dev attempt per round; keep syntax/RSpec validation and salvage",
    }
    for name, description in help_text.items():
        flags = ["--" + name.replace("_", "-")]
        if underscores:
            flags.append("--" + name)
        parser.add_argument(*flags, dest=name, action="store_true", help=description)


def from_args(args):
    return AblationOptions(**{name: getattr(args, name, False)
                             for name in AblationOptions.__dataclass_fields__})
