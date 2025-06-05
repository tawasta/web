##############################################################################
#
#    Author: Futural Oy
#    Copyright 2019 Futural Oy (https://futural.fi)
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
    "name": "Custom X2Many 2D Matrix Renderer",
    "summary": "Override and extend the 2D matrix renderer for x2many fields",
    "version": "17.0.1.0.0",
    "category": "Web",
    "website": "https://github.com/tawasta/web",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["web_widget_x2many_2d_matrix"],
    "assets": {
        "web.assets_backend": [
            "x2many_2d_matrix_renderer_patch/static/src/components/x2many_2d_matrix_field/x2many_2d_matrix_field.esm.js",
            "x2many_2d_matrix_renderer_patch/static/src/components/x2many_2d_matrix_field/x2many_2d_matrix_field.xml",
            "x2many_2d_matrix_renderer_patch/static/src/components/x2many_2d_matrix_renderer/x2many_2d_matrix_renderer.esm.js",
            "x2many_2d_matrix_renderer_patch/static/src/components/x2many_2d_matrix_renderer/x2many_2d_matrix_renderer.xml",
            (
                "remove",
                "web_widget_x2many_2d_matrix/static/src/components/x2many_2d_matrix_renderer/x2many_2d_matrix_renderer.esm.js",
            ),
            (
                "remove",
                "web_widget_x2many_2d_matrix/static/src/components/x2many_2d_matrix_field/x2many_2d_matrix_field.esm.js",
            ),
        ],
    },
}
