# Stdlib:
import io
import os

# Thirdparty:
from facturark.analyzer import Analyzer
from facturark.client import Client
from pytest import fixture


@fixture
def analyzer():
    analyzer = Analyzer()
    return analyzer


@fixture
def client(analyzer):
    username = "USER"
    password = "PASS"
    test_url = "tests/data/electronic_invoice.wsdl"

    return Client(analyzer, username, password, test_url)


@fixture
def document():
    filename = "signed_invoice.xml"
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, "..", "data", filename)
    with io.open(file_path, "rb") as f:
        return f.read()


@fixture
def request_dict(document):
    return dict(document=document)


@fixture
def query_dict(document):
    return dict(document=document)
