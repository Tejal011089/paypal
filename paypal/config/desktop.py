# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"paypal": {
			"color": "grey",
			"icon": "icon-money",
			"type": "module",
			"label": _("paypal")
		}
	}
