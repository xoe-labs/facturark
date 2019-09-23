# -*- coding: utf-8 -*-
# Thirdparty:
from facturark.composers import (
    AddressComposer,
    DespatchComposer,
    LocationComposer,
    PartyComposer,
    PartyLegalEntityComposer,
    PartyTaxSchemeComposer,
    PersonComposer,
)
from facturark.namespaces import NS
from lxml.etree import QName
from pytest import fixture


@fixture
def composer():
    party_tax_scheme_composer = PartyTaxSchemeComposer()
    party_legal_entity_composer = PartyLegalEntityComposer()
    person_composer = PersonComposer()
    address_composer = AddressComposer()
    location_composer = LocationComposer(address_composer)
    party_composer = PartyComposer(
        party_tax_scheme_composer,
        party_legal_entity_composer,
        person_composer,
        location_composer,
    )
    return DespatchComposer(address_composer, party_composer)


@fixture
def data_dict():
    return {
        "despatch_address": {
            "department": "Cauca",
            "city_name": "Popayán",
            "address_line": {"line": "Cra 22 # 33 - 44"},
            "country": {"identification_code": "CO"},
        },
        "despatch_party": {
            "party_identification": {
                "id": {
                    "@attributes": {
                        "schemeAgencyID": "123",
                        "schemeAgencyName": "CIA",
                        "schemeID": "007",
                    },
                    "#text": "900555666",
                }
            },
            "party_tax_schemes": [{"tax_level_code": "0"}],
            "party_legal_entity": {"registration_name": "800777555"},
            "physical_location": {
                "address": {
                    "department": "Valle",
                    "city_name": "Cali",
                    "country": {"identification_code": "CO"},
                }
            },
        },
    }


def test_compose(composer, data_dict, schema):
    despatch = composer.compose(data_dict)

    assert despatch.tag == QName(NS.fe, "Despatch").text

    schema.assertValid(despatch)
