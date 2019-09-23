# Thirdparty:
from facturark.composers import ItemComposer
from facturark.namespaces import NS
from lxml.etree import QName
from pytest import fixture


@fixture
def composer():
    return ItemComposer()


@fixture
def data_dict():
    return {"description": "Line 1"}


def test_compose(composer, data_dict, schema):
    price = composer.compose(data_dict)

    assert price.tag == QName(NS.fe, "Item").text
    assert price.findtext(QName(NS.cbc, "Description")) == "Line 1"
    schema.assertValid(price)
