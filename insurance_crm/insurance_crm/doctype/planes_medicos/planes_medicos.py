# Copyright (c) 2026, IT Mabegroup and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PlanesMedicos(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		carrier: DF.Link | None
		categoria: DF.Literal["Gold", "Expanded Bronze", "Silver"]
		nombre_plan: DF.Data | None
		plan_id: DF.Data | None
	# end: auto-generated types

	pass
