# Thirdparty:
from lxml.etree import Element, QName

# Localfolder:
from ..namespaces import NS
from ..utils import make_child
from .composer import Composer


class PartyTaxSchemeComposer(Composer):
    def compose(self, data_dict, root_name="PartyTaxScheme"):
        root = Element(QName(NS.fe, root_name), nsmap=vars(NS))

        make_child(
            root,
            QName(NS.cbc, "TaxLevelCode"),
            data_dict.get("tax_level_code"),
            required=False,
        )
        make_child(root, QName(NS.cac, "TaxScheme"), required=False, empty=True)

        return root
