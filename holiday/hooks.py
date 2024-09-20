app_name = "holiday"
app_title = "Holiday"
app_publisher = "tushar"
app_description = "app to customize the Opportunity doctype"
app_email = "tushar@mail.hybrowlabs.com"
app_license = "mit"

# Apps
# ------------------


doctype_js = {
    "Quotation": [
        "public/js/button.js",
        "public/js/quotation_custom.js"
    ],
    "Opportunity": "public/js/custom.js"
}

doc_events = {
    "Quotation": {
        "on_submit": "holiday.custom_methods.quotation_custom.update_opportunity_with_quotation"
    }
}



fixtures = [
            {"dt":"Custom Field", "filters": [["name", "in",("Opportunity-custom_item_list_2","Opportunity-custom_section_break_l9vsj","Opportunity-custom_final_destination","Opportunity-custom_column_break_oahu0","Opportunity-custom_preferred_destination_","Opportunity-custom_destinations","Opportunity-custom_item_list_1","Opportunity-custom_item_list","Opportunity-custom_address_country","Opportunity-custom_destination_country","Opportunity-custom_departure_counrty","Opportunity-custom_pax_details","Opportunity-custom_section_break_uqsgp","Opportunity-custom_column_break_ipvko","Opportunity-custom_address_state","Opportunity-custom_address_city","Opportunity-custom_traveller_details","Opportunity-custom_city_wise_travelling_details","Opportunity-custom_end_date","Opportunity-custom_start_date","Opportunity-custom_column_break_la1gn","Opportunity-custom_night_countsv","Opportunity-custom_destination_city","Opportunity-custom_column_break_ic7ib","Opportunity-custom_total_travel_days","Opportunity-custom_departure_city","Opportunity-custom_travel_details","Opportunity-custom_preferred_mode_of_travel","Opportunity-custom_preferred_destination_city","Opportunity-custom_column_break_fvdpn","Opportunity-custom_number_of_travellers_adults__c","Opportunity-custom_preferred_departure_city","Opportunity-custom_column_break_dm3vs","Opportunity-custom_preferred_hotel_type","Opportunity-custom_travel_start_date","Opportunity-custom_preferred_travel_details_","Quotation-custom_item_list","Quotation-custom_traveller_details_section","Quotation-custom_traveller_details_tab","Quotation-custom_end_date","Quotation-custom_start_date","Quotation-custom_column_break_5v9gu","Quotation-custom_night_counts","Quotation-custom_destination_country","Quotation-custom_destination_city","Quotation-custom_column_break_p9uob","Quotation-custom_total_travel_days","Quotation-custom_departure_counrty_","Quotation-custom_departure_city","Quotation-custom_section_break_ce3fg","Quotation-custom_destination"),]]},
            {"dt":"Property Setter", "filters": [["name", "in",("Opportunity-status-options"),]]}
]

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "holiday",
# 		"logo": "/assets/holiday/logo.png",
# 		"title": "Holiday",
# 		"route": "/holiday",
# 		"has_permission": "holiday.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/holiday/css/holiday.css"
# app_include_js = "/assets/holiday/js/holiday.js"

# include js, css files in header of web template
# web_include_css = "/assets/holiday/css/holiday.css"
# web_include_js = "/assets/holiday/js/holiday.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "holiday/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "holiday/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "holiday.utils.jinja_methods",
# 	"filters": "holiday.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "holiday.install.before_install"
# after_install = "holiday.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "holiday.uninstall.before_uninstall"
# after_uninstall = "holiday.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "holiday.utils.before_app_install"
# after_app_install = "holiday.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "holiday.utils.before_app_uninstall"
# after_app_uninstall = "holiday.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "holiday.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"holiday.tasks.all"
# 	],
# 	"daily": [
# 		"holiday.tasks.daily"
# 	],
# 	"hourly": [
# 		"holiday.tasks.hourly"
# 	],
# 	"weekly": [
# 		"holiday.tasks.weekly"
# 	],
# 	"monthly": [
# 		"holiday.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "holiday.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "holiday.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "holiday.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["holiday.utils.before_request"]
# after_request = ["holiday.utils.after_request"]

# Job Events
# ----------
# before_job = ["holiday.utils.before_job"]
# after_job = ["holiday.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"holiday.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

