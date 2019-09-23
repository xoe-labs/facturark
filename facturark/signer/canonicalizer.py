# Thirdparty:
from lxml.etree import fromstring, tostring


class Canonicalizer:
    def canonicalize(self, element):
        document = tostring(element, method="c14n", with_comments=False)
        return document

    def parse(self, document):
        element = fromstring(document)
        return element
