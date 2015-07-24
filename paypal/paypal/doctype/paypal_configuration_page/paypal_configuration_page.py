# -*- coding: utf-8 -*-
# Copyright (c) 2015, software company and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PaypalConfigurationPage(Document):
	pass

@frappe.whitelist()
def make_paypal_payment_entry(sales_invoice,paypal_amount,client_id,client_secret):
	if not client_id and client_secret:
		frappe.throw("Please specify paypal account credentials in Paypal Configuration Page")
	else:
		payment=create_paypal_payment(sales_invoice,paypal_amount,client_id,client_secret)

	generate_payer_id(payment)
	return payment.id

def create_paypal_payment(sales_invoice,paypal_amount,client_id,client_secret):
	import paypalrestsdk
	paypalrestsdk.configure({
		'mode': 'sandbox',
		'client_id': client_id,
		'client_secret': client_secret
	})
	payment = paypalrestsdk.Payment({
	"intent": "sale",
	"payer": {
		"payment_method": "paypal" },
	"redirect_urls": {
		"return_url": "https://devtools-paypal.com/guide/pay_paypal/python?success=true.get_parameters",
		"cancel_url": "https://devtools-paypal.com/guide/pay_paypal/python?cancel=true" },
	"transactions": [{
		"item_list": {
			"items": [{
				"name": sales_invoice,
				"sku": sales_invoice,
				"price": paypal_amount,
				"currency": "USD",
				"quantity": 1 }]},
			"amount": {
				"total": paypal_amount,
				"currency": "USD" },
			"description": "This is the payment transaction description." }]})

	payment_status=payment.create()
	frappe.errprint(payment_status)
	frappe.errprint(payment)
	return payment
	
def generate_payer_id(payment):
	import webbrowser
	if payment:
		for link in payment.links:
			if link.method == "REDIRECT":
				redirect_url = str(link.href)
				frappe.errprint(redirect_url)
				new=2
				u = webbrowser.open(redirect_url,new)

@frappe.whitelist()
def execute_paypal_payment_entry(sales_invoice,paypal_amount,client_id,client_secret,payment_id,payer_id):
	import paypalrestsdk
	if payment_id and payer_id:
		payment=create_paypal_payment(sales_invoice,paypal_amount,client_id,client_secret)
		payment = paypalrestsdk.Payment.find(payment_id)
		# url='https://api.sandbox.paypal.com/v1/payments/payment/'+payment_id
		# frappe.errprint(url)
		# import requests
		# response=requests.get(url)
		# frappe.errprint(response)
		status=payment.execute({"payer_id": payment_id})
		frappe.errprint(status)

		if status==True:
			frappe.msgprint("Payment Completed for Payment Id: '%s' Payment Status: approved"%payment_id)
		else:
			frappe.errprint(payment.error)


@frappe.whitelist(allow_guest=True)
def get_parameters():
	frappe.errprint("in get parameters")