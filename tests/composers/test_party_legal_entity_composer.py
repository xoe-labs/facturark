# Thirdparty:
from facturark.composers import PartyLegalEntityComposer
from facturark.namespaces import NS
from lxml.etree import QName
from pytest import fixture


@fixture
def composer():
    return PartyLegalEntityComposer()


@fixture
def data_dict():
    return {"registration_name": "800777555"}


def test_compose(composer, data_dict, schema):
    party_legal_entity = composer.compose(data_dict)

    assert party_legal_entity.tag == QName(NS.fe, "PartyLegalEntity").text
    assert party_legal_entity.findtext(QName(NS.cbc, "RegistrationName")) == "800777555"
    schema.assertValid(party_legal_entity)
