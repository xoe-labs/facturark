# Stdlib:
import hashlib


class Hasher:
    def __init__(self):
        self.algorithms = {
            "http://www.w3.org/2000/09/xmldsig#sha1": "sha1",
            "http://www.w3.org/2000/09/xmldsig#rsa-sha1": "sha1",
            "http://www.w3.org/2001/04/xmlenc#sha256": "sha256",
            "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256": "sha256",
            "http://www.w3.org/2001/04/xmlenc#sha512": "sha512",
            "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512": "sha512",
        }

    def hash(self, data, algorithm="http://www.w3.org/2001/04/xmlenc#sha256"):
        if hasattr(algorithm, "encode"):
            algorithm = algorithm.encode("utf8")
        algorithm = algorithm.decode("utf-8")
        hash_name = self.algorithms.get(algorithm)
        hash_function = getattr(hashlib, hash_name)
        return hash_function(data).digest()
