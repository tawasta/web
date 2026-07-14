import uuid

from werkzeug import urls

from odoo import fields, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    link_url = fields.Char("Public Link URL", readonly=1, compute="_compute_link_url")

    def _compute_link_url(self):
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        for attachment in self:
            link_url = urls.url_join(
                base_url,
                attachment.local_url.replace("image", "content"),
            )
            if not attachment.public:
                access_token = attachment.access_token
                if not access_token:
                    attachment.sudo().update({"access_token": str(uuid.uuid4())})
                link_url += f"&access_token={attachment.access_token}"
            attachment.link_url = link_url
