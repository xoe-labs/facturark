# Stdlib:
from base64 import b64decode, b64encode


class Encoder:
    def __init__(self):
        pass

    def base64_encode(self, data):
        return b64encode(data)

    def base64_decode(self, data):
        return b64decode(data)
