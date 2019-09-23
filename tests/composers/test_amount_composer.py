# Thirdparty:
from facturark.composers import AmountComposer
from facturark.namespaces import NS
from lxml.etree import QName
from pytest import fixture


@fixture
def composer():
    return AmountComposer()


@fixture
def data_dict():
    return {"@attributes": {"currencyID": "COP"}, "#text": "999999.00"}


def test_compose(composer, data_dict, schema):
    amount = composer.compose(data_dict, "LineExtensionAmount")

    assert amount.tag == QName(NS.cbc, "LineExtensionAmount").text
    assert amount.text == "999999.00"
    assert amount.attrib == data_dict["@attributes"]

    schema.assertValid(amount)
