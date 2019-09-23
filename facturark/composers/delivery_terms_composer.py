# Thirdparty:
from lxml.etree import Element, QName

# Localfolder:
from ..namespaces import NS
from .composer import Composer


class DeliveryTermsComposer(Composer):
    def compose(self, data_dict, root_name=None):
        root_name = root_name or self.root_name
        root = Element(QName(NS.fe, root_name), nsmap=vars(NS))

        return root
