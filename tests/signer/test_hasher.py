# Thirdparty:
from facturark.signer import Hasher
from pytest import fixture


@fixture
def hasher():
    hasher = Hasher()
    return hasher


def test_hasher_instantiation(hasher):
    assert hasher is not None


def test_hasher_hash(hasher):
    data = b"<Invoice></Invoice>"
    result = hasher.hash(data, "http://www.w3.org/2000/09/xmldsig#sha1")
    assert result == (b'\xdbK\x0cn\x9f"\xe3}\x8an\x1b\xd6\x19\x11O\xcas\xf1\xf3+')
