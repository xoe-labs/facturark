# -*- coding: utf-8 -*-
# Thirdparty:
from facturark.namespaces import NS
from facturark.signer.composers import ObjectComposer
from lxml.etree import QName
from pytest import fixture


@fixture
def composer():
    return ObjectComposer()


@fixture
def data_dict():
    return {
        "qualifying_properties": {
            "signed_properties": {"signed_signature_properties": {}}
        }
    }


def test_compose(composer, data_dict, schema):
    key_info = composer.compose(data_dict)

    assert key_info.prefix == "ds"
    assert key_info.tag == QName(NS.ds, "Object").text

    schema.assertValid(key_info)
