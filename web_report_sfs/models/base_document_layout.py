from odoo import fields, models


class BaseDocumentLayoutInherit(models.TransientModel):
    _inherit = "base.document.layout"

    company_registry = fields.Char(related="company_id.company_registry", readonly=True)
