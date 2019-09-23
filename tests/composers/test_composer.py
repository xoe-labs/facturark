# Thirdparty:
from facturark.composers import Composer
from facturark.namespaces import NS
from lxml.etree import QName, fromstring
from pytest import fixture, raises


@fixture
def composer():
    return Composer()


def test_compose_not_implemented(composer):
    with raises(NotImplementedError):
        composer.compose({})


def test_composer_root_name():
    class SubComposer(Composer):
        pass

    composer = SubComposer()
    assert composer.root_name == "Sub"


def test_serialize(composer):
    def mock_compose(self, data_dict, root_name=None):
        return fromstring("<Root></Root>")

    composer.compose = mock_compose

    document = composer.serialize({})
    assert fromstring(document) is not None
    assert b"Root" in document
