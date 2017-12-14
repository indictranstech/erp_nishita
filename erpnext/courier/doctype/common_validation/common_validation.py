# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe,re
from frappe import _
from frappe.model.document import Document

class CommonValidation(Document):
    pass

@frappe.whitelist()
def validation_check(doc,method):
    validation_type_check(doc)
    pass

@frappe.whitelist()
def validation_type_check(doc):
    if(doc.doctype=="Country List"):
        country_code=doc.country_code
        country_name=doc.country_name
        dox_zone_code=doc.dox_zone_code
        non_dox_zone_code=doc.non_dox_zone_code
        bulk_zone_code=doc.bulk_zone_code
        if ((len(country_code)>4) | (country_code.isalpha() != 1)):
            frappe.throw(_("Enter Valid 3 Digit Country Code"))
        if (country_name.isalpha() != 1):
            frappe.throw(_("Enter Valid Country Name"))
        if (dox_zone_code > 999):
            frappe.throw(_("Enter Valid 3 Digit Dox Zone Code"))
        if (non_dox_zone_code > 999):
            frappe.throw(_("Enter Valid 3 Digit Non Dox Zone Code"))
        if ((bulk_zone_code.isalnum() != 1) | (len(bulk_zone_code)>2)):
            frappe.throw(_("Enter Valid Bulk Zone Code"))
    if (doc.doctype == "State"):
        state_code=doc.state_code
        state_name=doc.state_name
        if((state_code.isalpha()!=1) | (len(state_code)>3)):
            frappe.throw(_("Enter Valid 3 Digit State Code"))
        if ((state_name.isalpha() != 1)):
            frappe.throw(_("Enter Valid State Name"))
    if (doc.doctype == "District"):
        district_name=doc.district_name
        if ((district_name.isalpha() != 1)):
            frappe.throw(_("Enter Valid District Master"))
    if(doc.doctype=="Taluk"):
        taluk_name=doc.taluk_name
        if ((taluk_name.isalpha() != 1)):
            frappe.throw(_("Enter Valid Taluk Name"))
    if (doc.doctype == "Hub"):
        hub_name = doc.hub_name
        hub_code=doc.hub_code
        hub_email_id=doc.hub_email_id
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', hub_email_id)
        if (hub_name.isalpha() != 1):
            frappe.throw(_("Enter Valid Hub Name"))
        if (hub_code.isalnum() != 1):
            frappe.throw(_("Enter Valid Hub Code"))
        if match==None:
            frappe.throw(_("Enter Valid Email Id"))
    if(doc.doctype=="Contact Details"):
        contact_person=doc.contact_person
        contact_email=doc.contact_email
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', contact_email)
        if(contact_person.isalpha() !=1 ):
            frappe.throw(_("Enter Valid Contact Person Name"))
        if match==None:
            frappe.throw(_("Enter Valid Contact Email Id"))
    if(doc.doctype=="Destination"):
        destination_name=doc.destination_name
        destination_code=doc.destination_code
        destination_email_id=doc.destination_email_id
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', destination_email_id)
        if match==None:
            frappe.throw(_("Enter Valid Destination Email Id"))
        if (destination_name.isalpha()!=1):
            frappe.throw(_("Enter Valid Destination Name"))
        if (len(destination_code) > 9):
            frappe.throw(_("Enter Valid Destination Code"))
    if(doc.doctype=="Manifest"):
        manifest_id=doc.manifest_id
        manifest_code=doc.manifest_code
        code_name=doc.code_name
        maximum_documents_per_packet=doc.maximum_documents_per_packet
        if(manifest_code>999999999):
            frappe.throw(_("Enter Valid 9 Digit Manifest Code"))
        if(manifest_id>9999):
            frappe.throw(_("Enter Valid 4 Digit Manifest ID"))
        if(code_name.isalpha()!=1):
            frappe.throw(_("Enter Valid Code Name"))
        if(maximum_documents_per_packet>999):
            frappe.throw(_("Enter Valid Manifest Documents Per Packet"))
    if (doc.doctype == "Pincode"):
        pincode = doc.pincode
        if (pincode > 999999):
            frappe.throw(_("Enter Valid 6 Digit Pincode"))
    if (doc.doctype == "Region"):
        region_name = doc.region_name
        if (region_name.isalpha() != 1):
            frappe.throw(_("Enter Valid Region Name"))
    if(doc.doctype=="Content"):
        content_name=doc.content_name
        content_category=doc.content_category
        if (content_name.isalnum() != 1):
            frappe.throw(_("Enter Valid Content Name"))
    if (doc.doctype == "Other Charges"):
        particulars = doc.particulars
        if (particulars.isalpha() != 1):
            frappe.throw(_("Enter Valid Particulars"))
    if (doc.doctype == "Branch List"):
        branch_code = doc.branch_code
        branch_name=doc.branch_name
        if (branch_code.isalnum() != 1):
            frappe.throw(_("Enter Valid Branch Code"))
        if (branch_name.isalpha() != 1):
            frappe.throw(_("Enter Valid Branch Name"))
    if (doc.doctype == "Delivery Line"):
        delivery_line = doc.delivery_line
        delivery_line_code=doc.delivery_line_code
        if (delivery_line.isalnum() != 1):
            frappe.throw(_("Enter Valid Delivery Line"))
        if (delivery_line_code.isalnum() != 1):
            frappe.throw(_("Enter Valid Delivery Line Code"))
    if(doc.doctype=="NonDelivery and Return Reason"):
        non_delivery_reason=doc.non_delivery_reason
        non_delivery_code=doc.non_delivery_code
        if(non_delivery_reason.isalpha()!=1):
            frappe.throw(_("Enter Valid Non Delivery Reason"))
        if ((non_delivery_code.isalpha() != 1) | (len(non_delivery_code) <2 | len(non_delivery_code)>4)):
            frappe.throw(_("Enter Valid Non Delivery Code"))
    if (doc.doctype == "Agent"):
        agent_code = doc.agent_code
        agent_name = doc.agent_name
        if (agent_code.isalnum() != 1):
            frappe.throw(_("Enter Valid Agent Code"))
        if (agent_name.isalnum() != 1):
            frappe.throw(_("Enter Valid Agent Name"))
    if(doc.doctype=="Complaint Status"):
        particulars=doc.particulars
        if(particulars.isalnum()!=1):
            frappe.throw(_("Enter Valid Particulars"))
    if(doc.doctype=="Products"):
        product_name=doc.product_name
        if (product_name.isalnum() != 1):
            frappe.throw(_("Enter Valid Product Name"))
    if(doc.doctype=="Packing Type"):
        packing_type=doc.product_name
        if (packing_type.isalnum() != 1):
            frappe.throw(_("Enter Valid Packing Type"))
    if(doc.doctype=="Cost Master"):
        cost_name=doc.cost_name
        if(cost_name.isalpha()!=1):
            frappe.throw(_("Enter Valid Cost Name"))
    pass

@frappe.whitelist()
def save_check(doc,method):
    frappe.msgprint(doc.doctype)
    pass