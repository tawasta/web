from odoo import fields, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    download_count = fields.Integer(
        help="Tracks how many times this attachment has been downloaded",
    )
