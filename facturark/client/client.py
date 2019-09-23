# Stdlib:
from base64 import b64encode
from datetime import datetime
from random import randint

# Thirdparty:
import zeep
from dateutil import parser
from lxml.etree import fromstring, tostring

# Localfolder:
from .transports import SoapTransport
from .username import UsernameToken
from .utils import make_document_name, make_zip_file_bytes


class Client:
    def __init__(self, analyzer, username, password, wsdl_url, plugins=[]):
        self.analyzer = analyzer
        self.client = zeep.Client(
            wsdl_url,
            wsse=UsernameToken(username, password),
            transport=SoapTransport(),
            plugins=[],
        )

    def send(self, document):
        document = fromstring(document)
        kind = self.analyzer.get_document_type(document)
        vat = self.analyzer.get_supplier_vat(document)
        invoice_number = self.analyzer.get_document_number(document)
        invoice_number_without_prefix = self.analyzer.get_document_number(
            document, without_prefix=True
        )
        issue_date = self.analyzer.get_issue_date(document)
        issue_date = datetime.strptime(issue_date, "%Y-%m-%dT%H:%M:%S")

        filename = make_document_name(vat, invoice_number_without_prefix, kind)
        zip_file_bytes = make_zip_file_bytes(filename, tostring(document))

        response = self.client.service.EnvioFacturaElectronica(
            vat, invoice_number, issue_date, zip_file_bytes
        )

        return zeep.helpers.serialize_object(response)

    def query(self, document):
        document = fromstring(document)

        document_type = self.analyzer.get_document_type(document)
        document_number = self.analyzer.get_document_number(document)
        vat = self.analyzer.get_supplier_vat(document)
        creation_date = self.analyzer.get_signing_time(document)
        creation_date = datetime.strptime(
            creation_date.split(".")[0], "%Y-%m-%dT%H:%M:%S"
        )

        software_identifier = self.analyzer.get_software_identifier(document)
        uuid = self.analyzer.get_uuid(document)

        with self.client.settings(strict=False):
            response = self.client.service.ConsultaResultadoValidacionDocumentos(
                document_type,
                document_number,
                vat,
                creation_date,
                software_identifier,
                uuid,
            )

        return zeep.helpers.serialize_object(response)

    def compose(self, document):
        document = fromstring(document)
        vat = self.analyzer.get_supplier_vat(document)
        invoice_number = self.analyzer.get_document_number(document)
        issue_date = self.analyzer.get_issue_date(document)
        issue_date = datetime.strptime(issue_date, "%Y-%m-%dT%H:%M:%S")

        root = self.client.create_message(
            self.client.service,
            "EnvioFacturaElectronica",
            vat,
            invoice_number,
            issue_date,
            tostring(document),
        )

        return root

    def serialize(self, document):
        root = self.compose(document)
        request_document = tostring(root, pretty_print=True)

        return request_document
