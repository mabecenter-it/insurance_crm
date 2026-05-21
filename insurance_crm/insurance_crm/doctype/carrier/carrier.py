# Copyright (c) 2026, IT Mabegroup and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Carrier(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		active: DF.Check
		carrier_name: DF.Data
		payer_id: DF.Data | None
		support_phone: DF.Phone | None
		website: DF.Data | None
	# end: auto-generated types

	pass
