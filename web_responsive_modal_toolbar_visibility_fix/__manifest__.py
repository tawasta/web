##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2024- Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
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
    "name": "Web Responsive: Modal WYSIWYG Toolbar Visibility Fix",
    "summary": "Bring the WYSIWYG toolbar to top",
    "version": "17.0.1.0.0",
    "category": "Web",
    "website": "https://gitlab.com/tawasta/odoo/web",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["web_responsive"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "/web_responsive_modal_toolbar_visibility_fix/static/src/scss/web_responsive_modal_toolbar_visibility_fix.scss"
        ]
    },
}
