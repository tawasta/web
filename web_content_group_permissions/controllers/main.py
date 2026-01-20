import logging

from odoo import _, http
from odoo.exceptions import AccessDenied
from odoo.http import request

from odoo.addons.web.controllers.binary import Binary

_logger = logging.getLogger(__name__)


class BinaryGroupPermissions(Binary):
    # pylint: disable=redefined-builtin
    @http.route(
        [
            "/web/content",
            "/web/content/<string:xmlid>",
            "/web/content/<string:xmlid>/<string:filename>",
            "/web/content/<int:id>",
            "/web/content/<int:id>/<string:filename>",
            "/web/content/<string:model>/<int:id>/<string:field>",
            "/web/content/<string:model>/<int:id>/<string:field>/<string:filename>",
        ],
        type="http",
        auth="public",
    )
    def content_common(
        self,
        xmlid=None,
        model="ir.attachment",
        id=None,
        field="raw",
        filename=None,
        filename_field="name",
        mimetype=None,
        unique=False,
        download=False,
        access_token=None,
        nocache=False,
        **kw,
    ):
        # Vain jos kyseessä on nimenomaan ir.attachment ja id on annettu
        if model == "ir.attachment" and id:
            attachment = request.env["ir.attachment"].sudo().browse(int(id))
            if attachment.exists():
                allowed_groups = attachment.visibility_group_ids
                user = request.env.user

                # Jos ryhmiä on asetettu, käyttäjän pitää kuulua vähintään yhteen niistä
                if allowed_groups and not (allowed_groups & user.groups_id):
                    _logger.info(
                        "Access Denied to ir.attachment record %s for user %s",
                        attachment.name,
                        user.name,
                    )
                    raise AccessDenied(
                        _("You don't have permission to access the requested resource.")
                    )

        # Kutsu parenttia Odoo 17:n parametreilla
        return super().content_common(
            xmlid=xmlid,
            model=model,
            id=id,
            field=field,
            filename=filename,
            filename_field=filename_field,
            mimetype=mimetype,
            unique=unique,
            download=download,
            access_token=access_token,
            nocache=nocache,
            **kw,
        )
