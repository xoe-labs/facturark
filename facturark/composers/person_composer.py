# Thirdparty:
from lxml.etree import Element, QName, SubElement, tostring

# Localfolder:
from ..namespaces import NS
from ..utils import make_child
from .composer import Composer


class PersonComposer(Composer):
    def compose(self, data_dict, root_name="Person"):
        root = Element(QName(NS.fe, root_name), nsmap=vars(NS))

        make_child(root, QName(NS.cbc, "FirstName"), data_dict.get("first_name"))
        make_child(root, QName(NS.cbc, "FamilyName"), data_dict.get("family_name"))

        return root
