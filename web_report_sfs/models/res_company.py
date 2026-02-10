from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    web_address_size = fields.Integer(string="Web address upper padding")
