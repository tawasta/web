from odoo import fields, models


class BaseDocumentLayout(models.Model):

    _inherit = "base.document.layout"

    web_footer_size = fields.Float(related="company_id.web_footer_size", readonly=True)
