from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    web_tree_view_limit = fields.Integer(
        string="General Tree view limit",
        help="Change the number of records shown on all tree views per page",
    )
