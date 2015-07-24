# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "paypal"
app_title = "paypal"
app_publisher = "software company"
app_description = "Paypal Payment Gateway"
app_icon = "icon-money"
app_color = "grey"
app_email = "tejal.s@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/paypal/css/paypal.css"
# app_include_js = "/assets/paypal/js/paypal.js"

# include js, css files in header of web template
# web_include_css = "/assets/paypal/css/paypal.css"
# web_include_js = "/assets/paypal/js/paypal.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

fixtures = ['Custom Field', 'Property Setter']

# Installation
# ------------

# before_install = "paypal.install.before_install"
# after_install = "paypal.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "paypal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"paypal.tasks.all"
# 	],
# 	"daily": [
# 		"paypal.tasks.daily"
# 	],
# 	"hourly": [
# 		"paypal.tasks.hourly"
# 	],
# 	"weekly": [
# 		"paypal.tasks.weekly"
# 	]
# 	"monthly": [
# 		"paypal.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "paypal.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "paypal.event.get_events"
# }

