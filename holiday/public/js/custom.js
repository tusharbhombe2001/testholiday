
frappe.ui.form.on('Opportunity', {
    before_save: function(frm) {
        if (!frm.confirmed_save) {
            frappe.confirm(
                'Are you sure you want to convert this Lead to Opportunity.',
                function() {
                    // If "Yes" is clicked, set the flag and trigger the save again
                    frm.confirmed_save = true;
                    frm.save();
                },
                function() {
                    // If "No" is clicked, prevent the save
                    frappe.validated = false;
                }
            );
            // Prevent the initial save until user confirms
            frappe.validated = false;
        }
    }
});





