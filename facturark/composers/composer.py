# Thirdparty:
from lxml.etree import Element, QName, SubElement, tostring

# Localfolder:
from ..namespaces import NS
from ..utils import make_child


class Composer:
    def compose(self, data_dict, root_name=None):
        raise NotImplementedError(
            "The 'compose' method should be " "implemented by subclasses."
        )

    def serialize(self, data_dict, root_name=None):
        root_name = root_name or self.root_name
        root = self.compose(data_dict, root_name)
        document = tostring(
            root,
            method="xml",
            encoding="utf-8",
            pretty_print=True,
            xml_declaration=True,
        )
        return document

    @property
    def root_name(self):
        return self.__class__.__name__.replace("Composer", "")
