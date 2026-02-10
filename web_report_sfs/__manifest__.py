##############################################################################
#
#    Author: Futural Oy
#    Copyright 2020 Futural Oy (https://futural.fi)
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
    "name": "Report layout standard formatting",
    "summary": "Alter report layout to be similar to SFS 2487 standard formatting",
    "version": "19.0.1.0.0",
    "category": "Web",
    "website": "https://github.com/tawasta/web",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base", "web"],
    "data": [
        "data/report_paperformat.xml",
        "data/company_paperformat.xml",
        "views/report_templates.xml",
        "views/res_config_settings.xml",
    ],
}
