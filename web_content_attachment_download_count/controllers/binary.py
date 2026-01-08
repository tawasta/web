import logging

from odoo import http
from odoo.http import request

from odoo.addons.web.controllers.binary import Binary

_logger = logging.getLogger(__name__)


class BinaryController(Binary):
    # pylint: disable=redefined-builtin,invalid-name
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
    ):
        """
        Bumps the ir.attachment record's download count while serving the attachment
        """

        response = super().content_common(
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
        )

        # Wrap in try/except to avoid any unforeseen download errors
        try:
            if id:
                related_attachment = (
                    request.env["ir.attachment"].sudo().search(domain=[("id", "=", id)])
                )

                related_attachment.sudo().write(
                    {"download_count": related_attachment.download_count + 1}
                )
        except Exception as e:
            _logger.error(
                "Error when attempting to increment "
                "attachment download count. Details:"
            )
            _logger.error(str(e))

        return response
