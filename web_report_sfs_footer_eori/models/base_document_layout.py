from odoo import fields, models


class BaseDocumentLayout(models.TransientModel):

    _inherit = "base.document.layout"

    eori = fields.Char(related="company_id.eori", readonly=True)
