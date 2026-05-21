# Copyright (c) 2026, IT Mabegroup and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EnrollmentDocument(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		document_type: DF.Literal["CIUDADANO", "PERMISO DE TRABAJO", "RESIDENTE", "ASILO POLITICO"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		verified: DF.Check
	# end: auto-generated types

	pass
