# Localfolder:
from ..analyzer import Analyzer
from .reviewer import Reviewer
from .validator import Validator


def resolve_validator():
    analyzer = Analyzer()
    reviewer = Reviewer(analyzer)
    return Validator(reviewer)
