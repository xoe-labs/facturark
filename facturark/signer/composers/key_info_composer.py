# Thirdparty:
from lxml.etree import Element, QName, SubElement, tostring

# Localfolder:
from ...namespaces import NS
from ...utils import make_child
from .composer import Composer


class KeyInfoComposer(Composer):
    def compose(self, data_dict, root_name=None):
        root_name = root_name or self.root_name
        root = Element(QName(NS.ds, root_name), nsmap=vars(NS))

        key_info_id = data_dict.get("@attributes", {}).get("Id")
        root.set("Id", key_info_id)

        X509_data_dict = data_dict["X509_data"]
        X509_data = make_child(root, QName(NS.ds, "X509Data"), empty=True)
        make_child(
            X509_data,
            QName(NS.ds, "X509Certificate"),
            X509_data_dict["X509_certificate"].strip(),
        )

        return root
