# Copyright (c) 2026, IT Mabegroup and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Poliza(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		carrier: DF.Link | None
		effective_date: DF.Date | None
		enrollment: DF.Link | None
		gross_premium: DF.Currency
		member_responsibility: DF.Currency
		renewal_date: DF.Date | None
		subsidy_amount: DF.Currency
		termination_date: DF.Date | None
	# end: auto-generated types

	def validate(self):
		self.calculate_member_responsibility()
		self.validate_member_responsibility()
		self.validate_dates()
		self.validate_carrier()

	def calculate_member_responsibility(self):
		gross_premium = self.gross_premium or 0
		subsidy_amount = self.subsidy_amount or 0

		self.member_responsibility = gross_premium - subsidy_amount

	def validate_member_responsibility(self):
		if self.member_responsibility < 0:
			frappe.throw(_("Member Responsibility cannot be negative."))

	def validate_dates(self):
		if self.effective_date and self.termination_date and self.effective_date >= self.termination_date:
			frappe.throw(_("Effective Date must be before Termination Date."))

	def validate_carrier(self):
		if not self.enrollment:
			return

		enrollment_carrier = frappe.db.get_value("Orden de venta", self.enrollment, "carrier")

		if enrollment_carrier != self.carrier:
			frappe.throw(_("Carrier must match the Enrollment carrier."))

	def on_submit(self):
		if self.enrollment:
			frappe.db.set_value("Orden de venta", self.enrollment, "status", "Active")
