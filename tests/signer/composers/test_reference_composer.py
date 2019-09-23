# -*- coding: utf-8 -*-
# Thirdparty:
from facturark.namespaces import NS
from facturark.signer.composers import ReferenceComposer
from lxml.etree import QName, fromstring, tostring
from pytest import fixture


@fixture
def composer():
    return ReferenceComposer()


@fixture
def data_dict():
    return {
        "transforms": [
            {
                "@attributes": {
                    "Algorithm": (
                        "http://www.w3.org/2000/09/" "xmldsig#enveloped-signature"
                    )
                }
            }
        ],
        "digest_method": {
            "@attributes": {"Algorithm": "http://www.w3.org/2000/09/xmldsig#sha1"}
        },
        "digest_value": "6F5KPfMMBWPbl8ImvaG9z9NFSLE=",
    }


def test_compose(composer, data_dict, schema):
    reference = composer.compose(data_dict)

    assert reference.prefix == "ds"
    assert reference.tag == QName(NS.ds, "Reference").text
    schema.assertValid(reference)
