frappe.ui.form.on('Quotation', {
    refresh(frm) {
    
        if (frm.doc.status === 'Draft') {
            frm.add_custom_button(__('Mark As Booked'), function(){
             
                frm.set_df_property('status', 'read_only', 0);
                frm.set_value('status', 'Ordered');

         
                frm.save().then(() => {
                    
                    frm.set_df_property('status', 'read_only', 1);
                    frm.refresh();
                });
            });
        } else {
            frm.remove_custom_button('Mark As Booked');
        }
    }
});
