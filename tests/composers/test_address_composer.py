# -*- coding: utf-8 -*-
# Thirdparty:
from facturark.composers import AddressComposer
from facturark.namespaces import NS
from lxml.etree import QName
from pytest import fixture


@fixture
def composer():
    return AddressComposer()


@fixture
def data_dict():
    return {
        "department": "Cauca",
        "city_name": "Popayán",
        "address_line": {"line": "Cra 22 # 33 - 44"},
        "country": {"identification_code": "CO"},
    }


def test_compose(composer, data_dict, schema):
    address = composer.compose(data_dict)

    assert address.prefix == "fe"
    assert address.findtext(QName(NS.cbc, "Department")) == "Cauca"
    assert address.findtext(QName(NS.cbc, "CityName")) == "Popayán"
    address_line = address.find(QName(NS.cac, "AddressLine"))
    assert address_line.findtext(QName(NS.cbc, "Line")) == "Cra 22 # 33 - 44"
    country = address.find(QName(NS.cac, "Country"))
    assert country.findtext(QName(NS.cbc, "IdentificationCode")) == "CO"
    schema.assertValid(address)
