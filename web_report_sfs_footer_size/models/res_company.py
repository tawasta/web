
from odoo import fields, models


class ResCompany(models.Model):

    _inherit = 'res.company'

    web_footer_size = fields.Float(string="Web footer upper padding")
