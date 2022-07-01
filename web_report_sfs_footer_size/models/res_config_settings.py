from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    web_footer_size = fields.Float(
        string="Web footer upper padding",
        related="company_id.web_footer_size",
        readonly=False,
    )
