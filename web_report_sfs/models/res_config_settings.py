from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    web_address_size = fields.Integer(
        string="Web address upper padding",
        related="company_id.web_address_size",
        readonly=False,
    )
