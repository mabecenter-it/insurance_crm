# Copyright (c) 2026, IT Mabegroup and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HouseholdMember(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		birth_date: DF.Data | None
		estado_migratorio: DF.Data | None
		first_name: DF.Link
		fumador: DF.Check
		gender: DF.Literal[None]
		last_name: DF.Data | None
		needs_coverage: DF.Check
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		relationship: DF.Literal["ESPOSO(A)", "HIJO(A)", "NIETO(A)", "MADRE", "PADRE", "ABUELO(A)"]
		segundo_nombre: DF.Data | None
		social_security_number: DF.Data | None
	# end: auto-generated types

	pass
