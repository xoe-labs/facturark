# Stdlib:
import io
import os

# Thirdparty:
from facturark.analyzer import Analyzer
from facturark.imager import Imager
from pytest import fixture


@fixture
def imager():
    analyzer = Analyzer()
    return Imager(analyzer)


@fixture
def document():
    filename = "signed_invoice.xml"
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, "..", "data", filename)
    with io.open(file_path, "rb") as f:
        return f.read()
