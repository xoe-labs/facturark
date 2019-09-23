# Thirdparty:
from lxml.etree import Element, QName, SubElement, tostring

# Localfolder:
from ...namespaces import NS
from ...utils import make_child
from .composer import Composer


class SignatureValueComposer(Composer):
    def compose(self, data_dict, root_name=None):
        root_name = root_name or self.root_name
        root = Element(QName(NS.ds, root_name), nsmap=vars(NS))

        root.text = data_dict["#text"]
        root.set("Id", data_dict["@attributes"]["Id"])

        return root
