# Thirdparty:
from facturark.signer.composers.composer import Composer
from lxml.etree import QName, fromstring
from pytest import fixture, raises


@fixture
def composer():
    return Composer()


def test_compose_not_implemented(composer):
    with raises(NotImplementedError):
        composer.compose({})
