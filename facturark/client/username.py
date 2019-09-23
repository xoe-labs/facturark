# Stdlib:
import base64
import datetime
import hashlib
import os

# Thirdparty:
from zeep.wsse import utils


class UsernameToken:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def apply(self, envelope, headers):
        security = utils.get_security_header(envelope)

        token = utils.WSSE.UsernameToken()
        security.append(token)

        # Extra values
        nonce = os.urandom(16)
        timestamp = datetime.datetime.utcnow().isoformat()

        # Create the sub elements of the UsernameToken element
        elements = [
            utils.WSSE.Username(self.username),
            utils.WSSE.Password(
                hashlib.sha256(self.password.encode("utf-8")).hexdigest()
            ),
            utils.WSSE.Nonce(base64.b64encode(nonce).decode("utf-8")),
            utils.WSU.Created(timestamp),
        ]

        token.extend(elements)
        return envelope, headers

    def verify(self, envelope):
        pass
