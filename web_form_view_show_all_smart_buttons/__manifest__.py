##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2020 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    "name": "Form view show all smart buttons",
    "summary": "Show all smart buttons on form view",
    "version": "17.0.1.1.0",
    "category": "Web",
    "website": "https://gitlab.com/tawasta/odoo/web",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["web"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "web_form_view_show_all_smart_buttons/static/src/views/" "buttonbox.esm.js",
            "web_form_view_show_all_smart_buttons/static/src/views/" "button_box.scss",
            "web_form_view_show_all_smart_buttons/static/src/views/" "button_box.xml",
        ]
    },
}
