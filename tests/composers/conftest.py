# Thirdparty:
from facturark.utils import parse_xsd
from pytest import fixture


@fixture(scope="session")
def schema():
    return parse_xsd("XSD/DIAN/DIAN_UBL.xsd")
