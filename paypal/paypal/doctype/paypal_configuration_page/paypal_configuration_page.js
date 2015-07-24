// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt


// paypal payment entry method 
cur_frm.cscript.make_payment = function(doc,cdt,cdn) {
	// console.log(cur_frm.doc.client_secret)
	if(cur_frm.doc.client_secret && cur_frm.doc.client_id){
		return frappe.call({
			method: "paypal.paypal.doctype.paypal_configuration_page.paypal_configuration_page.make_paypal_payment_entry",
			args: {
				"sales_invoice": cur_frm.doc.sales_invoice_name,
				"paypal_amount":cur_frm.doc.paypal_amount,
				"client_id":cur_frm.doc.client_id,
				"client_secret":cur_frm.doc.client_secret
			},
			callback: function(r) {
				console.log(r.message);
				doc.payment_id=r.message
				refresh_field('payment_id')
				
			}
		});

	}
}

cur_frm.cscript.execute_payment = function(doc,cdt,cdn) {
	if (cur_frm.doc.payer_id && cur_frm.doc.payment_id) {
		return frappe.call({
			method: "paypal.paypal.doctype.paypal_configuration_page.paypal_configuration_page.execute_paypal_payment_entry",
			args: {
				"sales_invoice": cur_frm.doc.sales_invoice_name,
				"paypal_amount":cur_frm.doc.paypal_amount,
				"client_id":cur_frm.doc.client_id,
				"client_secret":cur_frm.doc.client_secret,
				"payment_id": cur_frm.doc.payment_id,
				"payer_id": cur_frm.doc.payer_id	
			},
			callback: function(r) {
				//console.log(r.message)	
			}
		});

	}
}
