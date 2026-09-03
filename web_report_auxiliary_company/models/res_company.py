from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    is_aux_company = fields.Boolean(
        string="Is Auxiliary company", store=True, copy=False
    )
