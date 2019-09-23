# Thirdparty:
from lxml.etree import Element, QName, tostring

# Localfolder:
from ..namespaces import NS
from ..utils import make_child
from .composer import Composer


class LocationComposer(Composer):
    def __init__(self, address_composer):
        self.address_composer = address_composer

    def compose(self, data_dict, root_name=None):
        root_name = root_name or self.root_name
        root = Element(QName(NS.fe, root_name), nsmap=vars(NS))

        address_dict = data_dict.get("address")
        root.append(self.address_composer.compose(address_dict))

        return root
