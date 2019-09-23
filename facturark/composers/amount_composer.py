# Thirdparty:
from lxml.etree import Element, QName, SubElement, tostring

# Localfolder:
from ..namespaces import NS
from ..utils import make_child
from .composer import Composer


class AmountComposer(Composer):
    def compose(self, data_dict, root_name=None):
        root_name = root_name or self.root_name
        root = Element(QName(NS.cbc, root_name), nsmap=vars(NS))

        root.text = data_dict["#text"]
        root.set("currencyID", data_dict["@attributes"]["currencyID"])

        return root
