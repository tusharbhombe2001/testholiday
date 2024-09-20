frappe.ui.form.on('Quotation', {
    after_save: function(frm) {
        if (frm.doc.opportunity) {  // Check if Quotation has a linked Opportunity
            frappe.call({
                method: 'holiday.holiday.custom_methods.quotation_custom.update_opportunity_with_quotation',
                args: {
                    quotation_name: frm.doc.name
                },
                callback: function(r) {
                    if (!r.exc) {
                        // frappe.msgprint(__('Opportunity updated with Quotation details.'));
                    }
                }
            });
        }
    }
});
