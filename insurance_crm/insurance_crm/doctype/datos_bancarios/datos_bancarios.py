# Copyright (c) 2026, IT Mabegroup and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DatosBancarios(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		automaticos: DF.Literal["SI", "NO", "SLEF"]
		cuenta: DF.Data | None
		código_de_seguridad: DF.Data | None
		dia_autopay: DF.Data | None
		dirección_de_pago: DF.Data | None
		direccíon_tarjeta: DF.Data | None
		fecha_de_vencimiento_tarjeta: DF.Data | None
		nombre_del_banco: DF.Data | None
		número_tarjeta: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		ruta: DF.Data | None
		tarjeta: DF.Literal["D\u00c9BITO", "CR\u00c9DITO"]
		tipo_de_cuenta: DF.Literal["PERSONAL", "NEGOCIO"]
		tipo_tarjeta: DF.Literal["AMERICAN EXPRESS", "MASTERCARD", "VISA", "DISCOVERY"]
		titular: DF.Data
		zipcode: DF.Data | None
		últimos_4_digitos_de_la_cuenta: DF.Data | None
		últimos_4_digitos_de_la_tarjeta: DF.Data | None
	# end: auto-generated types

	pass
