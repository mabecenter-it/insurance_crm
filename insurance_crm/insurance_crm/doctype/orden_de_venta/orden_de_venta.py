# Copyright (c) 2026, IT Mabegroup and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class OrdendeVenta(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.contacts.doctype.contact_email.contact_email import ContactEmail
		from frappe.contacts.doctype.contact_phone.contact_phone import ContactPhone
		from frappe.types import DF

		contacto: DF.Link | None
		correos_de_contacto: DF.Table[ContactEmail]
		estado_migratorio: DF.Literal[None]
		fecha_de_nacimiento: DF.Date | None
		naming_series: DF.Literal["ACA-.YYYY.-.#####"]
		nombre_completo: DF.Data | None
		numeros_de_contacto: DF.Table[ContactPhone]
	# end: auto-generated types

	pass
