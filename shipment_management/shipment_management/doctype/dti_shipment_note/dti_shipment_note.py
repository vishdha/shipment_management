# -*- coding: utf-8 -*-
# Copyright (c) 2015, DigiThinkit Inc. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.file_manager import *


class DTIShipmentNote(Document):
	# Temporarily Disabled	

	def before_submit(self):
		for box in self.box_list:
			if not box.tracking_number:
				frappe.throw(_("Please enter Tracking Number"))

	# def on_submit(self):

	# 	from shipment_management.config.app_config import SupportedProviderList
	# 	from shipment_management.shipment import ShipmentNoteOperationalStatus

	# 	if self.shipment_provider != SupportedProviderList.Fedex:
	# 		frappe.throw(_("Please specify shipment provider!"))

	# 	if self.shipment_provider == SupportedProviderList.Fedex:
	# 		from shipment_management.provider_fedex import create_fedex_shipment
	# 		create_fedex_shipment(self)

	# 		frappe.db.set(self, 'shipment_note_status', ShipmentNoteOperationalStatus.Created)
	# 		frappe.db.set(self, 'fedex_status', ShipmentNoteOperationalStatus.InProgress)

	# def on_cancel(self):

	# 	from shipment_management.config.app_config import SupportedProviderList
	# 	from shipment_management.shipment import ShipmentNoteOperationalStatus

	# 	if self.shipment_provider == SupportedProviderList.Fedex:

	# 		try:
	# 			from shipment_management.provider_fedex import delete_fedex_shipment
	# 			delete_fedex_shipment(self)
	# 			frappe.msgprint(_("Shipment {} has been canceled!".format(self.name)))

	# 			frappe.db.set(self, 'shipment_note_status', ShipmentNoteOperationalStatus.Cancelled)
	# 			frappe.db.set(self, 'fedex_status', ShipmentNoteOperationalStatus.Cancelled)

	# 			from shipment_management.email_controller import get_content_cancel, send_email

	# 			message = get_content_cancel(self)

	# 			send_email(message=message,
	# 					   subject="Shipment to %s [%s] - Cancelled" % (self.recipient_company_name, self.name),
	# 					   recipient_list=self.contact_email.split(","))

	# 		except Exception, error:
	# 			frappe.throw(_(error))
