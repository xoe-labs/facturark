# Thirdparty:
from facturark.signer import Canonicalizer
from lxml.etree import fromstring
from pytest import fixture


@fixture
def canonicalizer():
    canonicalizer = Canonicalizer()
    return canonicalizer


@fixture
def xml_document():
    return fromstring("<Invoice/>")


def test_canonicalizer_instantiation():
    assert canonicalizer is not None


def test_canonicalize(canonicalizer, xml_document):
    result = canonicalizer.canonicalize(xml_document)
    assert result == b"<Invoice></Invoice>"
