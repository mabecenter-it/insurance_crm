# Copyright (c) 2026, IT Mabegroup and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ACAEnrollment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		aptc_eligible: DF.Check
		contact: DF.Link | None
		effective_date: DF.Date | None
		household_size: DF.Int
		income: DF.Currency
		naming_series: DF.Literal["ACA-.YYYY.-.#####"]
		policy_status: DF.Literal["", "Sin Digitar", "Pending Documents", "Submitted", "Approved", "Active", "Cancelled", "Expired", "Renewal Pending"]
		state: DF.Literal["", "AZ", "CA", "FL", "GA", "IL", "IN", "LA", "MA", "NC", "NE", "NJ", "OH", "SC", "TN", "TX", "WI"]
		taxes: DF.Literal["", "Single", "Married Filing Jointly", "Married Filing Separately", "Head of Household"]
	# end: auto-generated types

	pass
