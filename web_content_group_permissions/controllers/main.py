##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2021- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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

# 1. Standard library imports:
import logging

# 3. Odoo imports (openerp):
from odoo import _, http
from odoo.exceptions import AccessDenied
from odoo.http import request

# 4. Imports from Odoo modules:
from odoo.addons.web.controllers.main import Binary

# 2. Known third party imports:


# 5. Local imports in the relative form:

# 6. Unknown third party imports:

_logger = logging.getLogger(__name__)


class BinaryGroupPermissions(Binary):
    # disable pylint error as id definition is needed in inheritance
    # pylint: disable=W0622
    @http.route(['/web/content',
        '/web/content/<string:xmlid>',
        '/web/content/<string:xmlid>/<string:filename>',
        '/web/content/<int:id>',
        '/web/content/<int:id>/<string:filename>',
        '/web/content/<int:id>-<string:unique>',
        '/web/content/<int:id>-<string:unique>/<string:filename>',
        '/web/content/<int:id>-<string:unique>/<path:extra>/<string:filename>',
        '/web/content/<string:model>/<int:id>/<string:field>',
        '/web/content/<string:model>/<int:id>/<string:field>/<string:filename>'], type='http', auth="public")
    def content_common(self, xmlid=None, model='ir.attachment', id=None, field='datas',
                       filename=None, filename_field='name', unique=None, mimetype=None,
                       download=None, data=None, token=None, access_token=None, **kw):

        attachment_id = request.env["ir.attachment"].sudo().search([["id", "=", id]])
        allowed_groups = attachment_id.visibility_group_ids
        user_id = request.env.user
        if allowed_groups and all(
            user_id not in allowed_group.users for allowed_group in allowed_groups
        ):
            _logger.info(
                "Access Denied to ir.attachment record %s for user %s",
                attachment_id.name,
                user_id.name,
            )
            raise AccessDenied(
                _("You don't have permission to access the requested resource.")
            )

        return super(BinaryGroupPermissions, self).content_common(
            xmlid,
            model,
            id,
            field,
            filename,
            filename_field,
            unique,
            mimetype,
            download,
            data,
            token,
            access_token,
            **kw
        )
