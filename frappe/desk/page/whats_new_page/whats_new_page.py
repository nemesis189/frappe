# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe
import requests
from datetime import datetime

@frappe.whitelist(allow_guest=True)
def get_whats_new_posts():
	host = "https://test-st.frappe.cloud"
	post_list = []

	try:
		res = requests.get(host + '/api/method/frappe.desk.doctype.whats_new.whats_new.fetch_latest_posts')
	except:
		frappe.throw('Error in establishing connection with host')

	data = res.json()
	post_list = data.get("message")[0] or []
	event_list = data.get("message")[1] or []

	return post_list, event_list
