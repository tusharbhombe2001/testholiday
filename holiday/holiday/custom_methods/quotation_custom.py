import frappe
from datetime import datetime

@frappe.whitelist()
def update_opportunity_with_quotation(quotation_name):
    quotation_doc = frappe.get_doc('Quotation', quotation_name)

    if quotation_doc.opportunity:  
        
        opportunity_doc = frappe.get_doc('Opportunity', quotation_doc.opportunity)
        
        exists = False
        for row in opportunity_doc.custom_item_list_2:  
            if row.quotation_id == quotation_doc.name:
                exists = True
                break

        if not exists:
            creation_date = quotation_doc.creation.date()
            creation_time = quotation_doc.creation.time()
            opportunity_doc.append('custom_item_list_2', {
                'quotation_id': quotation_doc.name,
                'current_destination': quotation_doc.custom_destination_city,
                'date': creation_date ,
                'time' : creation_time
                
            })

            
            opportunity_doc.save()
