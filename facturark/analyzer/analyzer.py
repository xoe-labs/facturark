from lxml.etree import fromstring, QName
from ..namespaces import NS


class Analyzer:

    def get_supplier_vat(self, document):
        supplier_vat = document.find(
            ('fe:AccountingSupplierParty/fe:Party/'
             'cac:PartyIdentification/cbc:ID'), vars(NS)).text
        return supplier_vat

    def get_document_number(self, document, without_prefix=False):
        invoice_number = document.find('cbc:ID', vars(NS)).text
        prefix_element = document.find(
            ('.//sts:DianExtensions/sts:InvoiceControl/'
             'sts:AuthorizedInvoices/sts:Prefix'), vars(NS))
        prefix = ''
        if without_prefix and prefix_element is not None:
            prefix = prefix_element.text
        invoice_number = invoice_number.replace(prefix, '')

        return invoice_number

    def get_issue_date(self, document):
        issue_date = document.find('cbc:IssueDate', vars(NS)).text
        issue_time = document.find('cbc:IssueTime', vars(NS)).text
        document_date = 'T'.join([issue_date, issue_time])

        return document_date

    def get_document_type(self, document):
        if document.tag == QName(NS.fe, 'Invoice'):
            return '1'
        elif document.tag == QName(NS.fe, 'CreditNote'):
            return '2'
        elif document.tag == QName(NS.fe, 'DebitNote'):
            return '3'
        return '4'

    def get_signing_time(self, document):
        signing_time = document.find(
            './/xades:SignedSignatureProperties/xades:SigningTime',
            vars(NS)).text
        return signing_time

    def get_software_identifier(self, document):
        software_identifier = document.find(
            './/sts:DianExtensions/sts:SoftwareProvider/sts:SoftwareID',
            vars(NS)).text
        return software_identifier

    def get_uuid(self, document):
        uuid = document.find(
            './/cbc:UUID', vars(NS)).text
        return uuid

    def get_supplier_type(self, document):
        return document.find(
            ('.//fe:AccountingSupplierParty/'
             'cbc:AdditionalAccountID'), vars(NS)).text

    def get_customer_type(self, document):
        return document.find(
            ('.//fe:AccountingCustomerParty/'
             'cbc:AdditionalAccountID'), vars(NS)).text

    def get_supplier_country(self, document):
        return document.find(
            ('.//fe:AccountingSupplierParty/fe:Party/fe:PhysicalLocation/'
             'fe:Address/cac:Country/cbc:IdentificationCode'), vars(NS)).text

    def get_customer_country(self, document):
        return document.find(
            ('.//fe:AccountingCustomerParty/fe:Party/fe:PhysicalLocation/'
             'fe:Address/cac:Country/cbc:IdentificationCode'), vars(NS)).text

    def get_document_currency(self, document):
        return document.find(
            ('.//cbc:DocumentCurrencyCode'), vars(NS)).text

    def get_invoice_type(self, document):
        element = document.find(('.//cbc:InvoiceTypeCode'), vars(NS))
        if element is not None:
            return element.text

    def get_supplier_identification_type(self, document):
        return document.find(
            ('.//fe:AccountingSupplierParty/fe:Party/cac:PartyIdentification/'
             'cbc:ID'), vars(NS)).attrib.get('schemeID')

    def get_customer_identification_type(self, document):
        return document.find(
            ('.//fe:AccountingCustomerParty/fe:Party/cac:PartyIdentification/'
             'cbc:ID'), vars(NS)).attrib.get('schemeID')

    def get_supplier_tax_scheme(self, document):
        return document.find(
            ('.//fe:AccountingSupplierParty/fe:Party/fe:PartyTaxScheme/'
             'cbc:TaxLevelCode'), vars(NS)).text
